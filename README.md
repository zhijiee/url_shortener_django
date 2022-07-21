# URL Shortener 

This is a short MVP project created to understand how to use Django REST framework, React and Postgresql. 

- Django Backend 
- React Frontend 
- Postgresql Database

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


## Using the application

Visit http://localhost:8000 for a simple form to generate a shorterened URL. THe URL allow redirect the client to the website originally entered. 

The app also contain a testview. This testview is created using Django generic views to see the database entries stored. 
This can be found in http://localhost:8000/testview