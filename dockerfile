FROM python:3.8
WORKDIR /user
COPY . /user
RUN pip install -r requirements.txt