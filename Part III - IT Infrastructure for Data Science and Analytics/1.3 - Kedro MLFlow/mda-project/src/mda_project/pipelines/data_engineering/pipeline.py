"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, pipeline, node

import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(params: dict):
    data = pd.read_parquet("https://kuleuven-mda.s3.eu-central-1.amazonaws.com/credit_applications.parquet.gzip")
    data = data[data.submission_time < pd.Timestamp("now")]
    data = data.tail(params["size"])
    return data

def split_data(data: pd.DataFrame, params: dict):
    X = data.drop("outcome", axis=1)
    y = data["outcome"]
    return train_test_split(X, 
                            y, 
                            test_size=params["test-size"], 
                            random_state=params["seed"]
                            )

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=load_data,
            inputs="params:data-feed",
            outputs="applications",
            name="load_data",
            tags=["preprocessing"]
        ),
        node(
            func=split_data,
            inputs=["applications", "params:split"],
            outputs=["X_train", "X_test", "y_train", "y_test"],
            name="split_data",
            tags=["preprocessing"]
        )
    ])
