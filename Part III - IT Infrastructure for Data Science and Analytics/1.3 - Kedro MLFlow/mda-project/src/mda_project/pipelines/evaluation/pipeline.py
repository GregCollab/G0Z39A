"""
This is a boilerplate pipeline 'evaluation'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, pipeline, node
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score


def evaluate_model(X_test, y_test, model):
    y_pred = model.predict(X_test)
    return {
        "accuracy": accuracy_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "f1": f1_score(y_test, y_pred)
    }

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=evaluate_model,
            inputs=["X_test", "y_test", "model"],
            outputs="metrics",
            name="evaluate_model",
            tags=["evaluation"]
        )
    ])
