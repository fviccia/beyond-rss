FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY fetch_feeds.py fetch_feeds.py

CMD ["python", "fetch_feeds.py"]
