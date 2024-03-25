"""
This is a boilerplate pipeline 'model_development'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, pipeline, node
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline as SklearnPipeline

def define_model(params, transformer):
    random_forest = RandomForestClassifier(
        n_estimators=params["n_estimators"],
        max_depth=params["max_depth"],
        random_state=params["random_state_forest"]
    )
    pipe = SklearnPipeline([
        ("preprocessing", transformer),
        ("model", random_forest)
    ])
    return pipe

def upsample(X_train, y_train):
    zeros = y_train.value_counts()[0]
    ones = y_train.value_counts()[1]
    if zeros > ones:
        training_data = X_train.copy()
        training_data["outcome"] = y_train
        training_data = pd.concat([training_data, training_data[training_data.outcome == 1].sample(zeros - ones, replace=True)])
        X_train = training_data.drop("outcome", axis=1)
        y_train = training_data["outcome"]
    elif ones > zeros:
        training_data = X_train.copy()
        training_data["outcome"] = y_train
        training_data = pd.concat([training_data, training_data[training_data.outcome == 0].sample(ones - zeros, replace=True)])
        X_train = training_data.drop("outcome", axis=1)
        y_train = training_data["outcome"]
    return X_train, y_train

def train_model(X_train, y_train, model):
    model.fit(X_train, y_train.values.ravel())
    return model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=define_model,
            inputs=["params:random-forest", "transformer"],
            outputs="untrained-model",
            name="define_model",
            tags=["training"]
        ),
        node(
            func=upsample,
            inputs=["X_train", "y_train"],
            outputs=["X_train_resampled", "y_train_resampled"],
            name="upsample",
            tags=["training"]
        ),
        node(
            func=train_model,
            inputs=["X_train_resampled", "y_train_resampled", "untrained-model"],
            outputs="model",
            name="train_model",
            tags=["training"]
        )
    ])
