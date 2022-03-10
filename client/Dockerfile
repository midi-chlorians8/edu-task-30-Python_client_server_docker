FROM python:3.9-slim-bullseye
ADD client.py /client/
COPY requirements.txt /client
WORKDIR /client/
RUN pip install -r requirements.txt
#RUN pip install requests && \
#pip install response &&\
#pip install urllib3

CMD ["python","client.py","http://localhost:2000"]

