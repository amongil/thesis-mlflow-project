FROM python:3.9

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY run_mlflow_project.py /run_mlflow_project

ENTRYPOINT ["python",  "mlflow_tracking_get_runs.py"]
