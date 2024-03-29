import os
import sys

import mlflow


if __name__ == "__main__":
    project_uri = os.path.join(os.path.dirname(os.path.abspath(__file__)), "thesis-mlflow-project")
    params = {"alpha": sys.argv[1], "l1_ratio": sys.argv[2]}

    mlflow.run(
        project_uri,
        parameters=params,
        backend="kubernetes",
        backend_config="thesis-mlflow-project/kubernetes_config.json",
    )
