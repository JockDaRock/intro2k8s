FROM python:alpine

RUN pip install Flask

COPY welcome_app /root/welcome_app

WORKDIR /root/welcome_app

CMD python app.py

LABEL "cisco.cpuarch"="x86_64" \
      "cisco.resources.profile"="custom" \
      "cisco.resources.cpu"="50" \
      "cisco.resources.memory"="50" \
      "cisco.resources.disk"="10" \
      "cisco.resources.network.0.interface-name"="eth0"
