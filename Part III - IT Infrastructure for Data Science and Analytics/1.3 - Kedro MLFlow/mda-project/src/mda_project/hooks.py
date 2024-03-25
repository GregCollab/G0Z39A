from kedro.framework.hooks import hook_impl
import mlflow
import pandas as pd
import pickle

class ProjectHooks:

    @hook_impl
    def after_context_created(self, context, **kwargs):
        mlflow.set_tracking_uri("http://ec2-52-59-215-2.eu-central-1.compute.amazonaws.com:5000")
        mlflow.set_experiment("kedro-mlflow")
        mlflow.start_run()


    @hook_impl
    def after_pipeline_run(self, run_params) -> None:
        mlflow.end_run()


    @hook_impl
    def before_node_run(node, catalog, inputs, is_async, session_id):
        for key, value in inputs.items():
            if "params" in key:
                for k, v in value.items():
                    mlflow.log_param(k, v)

    @hook_impl
    def after_dataset_saved(self, dataset_name, data, node):
        if isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
            mlflow.log_artifact(f"data/{dataset_name}.csv")
        elif dataset_name == "model":
            x = pd.read_csv("data/X_train.csv")
            y = pd.read_csv("data/y_train.csv")
            signature = mlflow.models.infer_signature(x, y)
            model = pickle.load(open("data/model.pkl", 'rb'))
            mlflow.sklearn.log_model(
                model, 
                artifact_path="data/model.pkl",
                signature=signature)
        elif dataset_name == "metrics":
            for key, value in data.items():
                mlflow.log_metric(key, value)
            x = pd.read_csv("data/X_test.csv")
            y = pd.read_csv("data/y_test.csv")
            x["label"] = y
            model_uri = f"runs:/{mlflow.active_run().info.run_id}/data/model.pkl"
            mlflow.evaluate(
                model_uri, x, targets="label", 
                model_type="classifier", evaluators=["default"])
    
    



        
