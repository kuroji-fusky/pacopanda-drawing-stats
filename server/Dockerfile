FROM python:3.11

WORKDIR /

COPY requirements.txt /requirements.txt
COPY server/main.py /server.py
COPY data/scraper.py /scraper.py

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 4000

ENTRYPOINT ["py", "server.py", "--prod"]
