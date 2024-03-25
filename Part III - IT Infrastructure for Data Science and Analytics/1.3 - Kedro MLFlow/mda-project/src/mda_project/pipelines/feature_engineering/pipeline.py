"""
This is a boilerplate pipeline 'feature_engineering'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, pipeline, node
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def specify_transfomer(params: dict):
    transformer = ColumnTransformer(
        transformers=[
            ("drop", "drop", params["drop-features"]),
            ('num', StandardScaler(), params["num-features"]),
            ('cat', OneHotEncoder(handle_unknown='infrequent_if_exist'), params["cat-features"])
        ]
    )
    return transformer


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=specify_transfomer,
            inputs=["params:transformer"],
            outputs="transformer",
            name="specify_transfomer",
            tags=["training"]
        )
    ])
