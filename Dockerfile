FROM python:3.8.11

EXPOSE 8000

WORKDIR /app
COPY . /app

RUN chmod +x entrypoint.sh
RUN pip install -r requirements.txt

ENTRYPOINT ["/app/entrypoint.sh"]