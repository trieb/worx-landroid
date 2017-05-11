FROM python:3.5.3
ENV PYTHONUNBUFFERED 1
RUN mkdir /web
WORKDIR /web
ADD requirements.txt /web/
ADD . /web/

# RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 1883 8883

# CMD ["python", "run.py"]
