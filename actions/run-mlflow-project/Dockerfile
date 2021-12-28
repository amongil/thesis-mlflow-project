FROM python:3.9

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY run_mlflow_project.py /run_mlflow_project.py
ADD thesis_mlflow_project/ /thesis_mlflow_project
RUN chmod u+x /run_mlflow_project.py

ENTRYPOINT ["python",  "/run_mlflow_project.py"]
