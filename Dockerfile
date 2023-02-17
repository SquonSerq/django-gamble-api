FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt-get update
WORKDIR /gamble_api
COPY requirements.txt /gamble_api/
RUN pip install -r requirements.txt
COPY ./gamble_api /gamble_api/