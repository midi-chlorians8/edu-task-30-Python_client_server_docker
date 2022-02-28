FROM python:3.9-slim-bullseye

RUN pip install requests && \
pip install response &&\
pip install urllib3

WORKDIR /client/
ADD client.py /client/

CMD ["python","client.py","http://localhost:2000"]

