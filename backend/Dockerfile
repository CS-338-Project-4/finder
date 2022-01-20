FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY main.py routes.py .

# TODO: Remove "--reload" for production
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
