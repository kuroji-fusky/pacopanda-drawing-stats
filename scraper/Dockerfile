FROM python:3.10.4-buster

WORKDIR /scraper

COPY . .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt

CMD [ "python", "main.py" ]