FROM python:alpine

RUN pip install Flask

COPY welcome_app /root/welcome_app

WORKDIR /root/welcome_app

CMD python app.py