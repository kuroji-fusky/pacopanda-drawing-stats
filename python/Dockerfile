FROM python:3.11

WORKDIR /api

COPY ./requirements.txt /api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /api/app

COPY ./parinton /api/parinton

EXPOSE 4000
ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
