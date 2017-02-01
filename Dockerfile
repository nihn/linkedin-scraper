FROM python:3.6.0-slim

COPY requirements.txt .
RUN apt-get update && apt-get install -y build-essential libxml2 libssl-dev && \
    pip install -r requirements.txt && \
    apt-get purge -y build-essential libxml2 libssl-dev

WORKDIR /opt/linkedin_scraper
