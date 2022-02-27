
FROM ubuntu

RUN  apt update && \
     apt install -y \
     python3 python3-dev python3-pip curl && \
     python3 -m pip install requests && \
     python3 -m pip install response &&\
     python3 -m pip install urllib3

ADD client.py /client/

WORKDIR /client/

