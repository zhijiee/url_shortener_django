FROM python:3.9


RUN mkdir /code
WORKDIR /code
RUN pip install --upgrade pip
COPY requirements.txt /code/

RUN pip install -r requirements.txt
COPY . /code/

RUN apt update
RUN apt install python3-psycopg2 npm -y

# Setup for Django Models
RUN ./manage.py makemigrations 
RUN ./manage.py migrate

# Setup for react frontend
RUN cd frontend
RUN npm install
RUN npm run dev
RUN cd ..

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
