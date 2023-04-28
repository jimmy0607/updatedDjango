FROM python:3.9

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
COPY ./ /code/

RUN pip install -r requirements.txt


