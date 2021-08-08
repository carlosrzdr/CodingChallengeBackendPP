FROM python:3.6.1-alpine
WORKDIR /web
ADD . /web
RUN pip install -r requirements.txt
CMD ["python","app.py"]