FROM python:3.11

WORKDIR /api

COPY ./requirements.txt /api/requirements.txt
COPY ./app /api/app
COPY ./parinton /api/parinton

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 4000

ENTRYPOINT ["py", "server.py", "--prod"]
