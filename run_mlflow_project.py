import os
import warnings
import argparse
from urllib.parse import urlparse

import mlflow


if __name__ == "__main__":
    warnings.filterwarnings("ignore")

    parser = argparse.ArgumentParser()
    parser.add_argument("--alpha")
    parser.add_argument("--l1-ratio")
    args = parser.parse_args()

    project_uri = os.path.join(os.path.dirname(os.path.abspath(__file__)), "thesis-mlflow-project")
    params = {"alpha": args.alpha, "l1_ratio": args.l1_ratio}

    # Run MLflow project and create a reproducible conda environment
    # on a local host
    mlflow.run(
        project_uri,
        parameters=params,
        backend="kubernetes",
        backend_config="thesis-mlflow-project/kubernetes_config.json",
    )
