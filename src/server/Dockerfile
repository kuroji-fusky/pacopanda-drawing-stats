FROM python:3.11

WORKDIR /

COPY requirements.txt /requirements.txt
COPY server.py /server.py
COPY scraper.py /scraper.py
COPY parinton/ /parinton/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 4000

ENTRYPOINT ["py", "server.py", "--prod"]
