# Запуск контейнера через docker run -it -p 8000:8000 web-app

FROM python:3.9-buster

WORKDIR /var/app

#RUN pwd
RUN ls -la

COPY web/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY web .

#RUN pwd
#RUN ls -la

CMD uvicorn app:app --host=0.0.0.0