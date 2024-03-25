import papermill as pm

for name in ["Jan", "Ruben", "Gregory"]:
    pm.execute_notebook(
        "notebook.ipynb",
        f"output_{name}.ipynb",
        parameters=dict(name=name),
        progress_bar=False
    )