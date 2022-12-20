FROM python:3.8
MAINTAINER xxx
WORKDIR /soft
COPY ./requirements.txt /soft/requirements.txt
RUN pip install -r requirements.txt -i https://pypi.doubanio.com/simple
CMD ["python","manage.py","runserver","0.0.0.0:8080"]