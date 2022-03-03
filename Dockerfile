FROM python:alpine

WORKDIR /fileupload

ADD . /fileupload

RUN pip3 install -r requirements.txt

CMD ["python", "upload.py"]