FROM python:3.11

WORKDIR /
COPY . .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 4000

CMD ["py", "__main__.py", "--prod"]
