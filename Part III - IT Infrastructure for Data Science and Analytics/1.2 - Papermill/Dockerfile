FROM python:3.10

COPY . .

RUN pip install papermill
RUN pip install --upgrade pip ipython ipykernel
RUN ipython kernel install --name "python3" --user

CMD python script.py