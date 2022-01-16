FROM python:3.9
ENV PYTHONUNBUFFERED=1
RUN apt-get -y update
RUN apt-get -y install vim
WORKDIR /django
COPY . /django
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt
