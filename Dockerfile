FROM python:3.9


RUN mkdir /code
WORKDIR /code
RUN pip install --upgrade pip
COPY requirements.txt /code/

RUN pip install -r requirements.txt
COPY . /code/

RUN apt update
RUN apt install npm -y

# Setup for react frontend
WORKDIR /code/frontend
RUN npm install
RUN npm run build

EXPOSE 8000
WORKDIR /code/
