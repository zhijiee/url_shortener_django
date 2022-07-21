# URL Shortener 

This is a short project created to understand how to use Django and React. It uses Django RESTFRAMEWORK as backend and React as frontend. 

- Django Backend 
- React Frontend 


## Setup

### Running the application on the system directly
```
# Clone the project
git clone git@github.com:zhijiee/url_shortener_django.git git clone 
cd url_shortener_django

# Create a virtual environemnt python
python3 -m venv venv 
source venv/bin/activate

# Install the required depenencies 
pip install -r requirements.txt


# Django models and databases
./manage.py makemigrations
./manage.py migrate

# React install
cd frontend
npm install
npm run dev
cd ../

# Running the server
./manage.py runserver 8000
```

### Running it via Docker
```
docker compose up --build
```