FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /fiyat
WORKDIR /fiyat
ADD requirements.txt /fiyat/
RUN pip  install -r requirements.txt
ADD . /fiyat/
