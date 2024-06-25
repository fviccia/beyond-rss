FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY process_feeds.py process_feeds.py

CMD ["python", "process_feeds.py"]
