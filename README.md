## Create virtual environment

python3 -m venv .venv

## Activate venv

source .venv/bin/activate

## add requirement file

pip install -r requirements.txt

## requirements

requests
seaborn
tqdm.auto
matplotlib.pyplot

plotly
plotly.offline
plotly.graph_objs
plotly.express

## 1. Setup Django

- create a new Django project using dnago-admin startproject

```plain
pip install django

django-admin startproject projectname

cd projectname

python manage.py startapp appname

django-admin startproject motor_vehicle_collisions_crashes

cd motor_vehicle_collisions_crashes
```

run the development server

```
python manage.py runserver
```

## 2. configure setting

- Createa PostgreSQL database in PgAdmin4
- Install psycopg2 Package:<br>
  psycopg2 is the PostgreSQL adapter for Python. You need to install it in your Django project's virtual environment:

```
pip install psycopg2-binary
```

- configure Django Setting.py

```python
# update database setting to use PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',  # Or the hostname where your PostgreSQL server is running
        'PORT': '5432',  # Default PostgreSQL port
    }
}

#run migration
python manage.py migrate

# (optional)create a super user
python manage.py createsuperuser
```

## 1. Setup Django Project:

Create a new Django project using django-admin startproject.
Configure project settings, including database settings, static files, and templates.
Optionally, create a virtual environment for the project to manage dependencies.

## Create Django App:

Create a new Django app within the project using python manage.py startapp.
Define models to represent the data you'll be storing in the PostgreSQL database.
Define views to handle HTTP requests and serve responses.
Create templates to render HTML pages and display data to users.

2. Retrieve and Process Data from NYC OpenData API:

Write Python scripts or Django management commands to retrieve data from the NYC OpenData API using the requests library.
Process the JSON data as needed, including cleaning, filtering, and transforming it into a suitable format.
Optionally, perform data analysis and visualization using libraries like Pandas and Matplotlib.

3. Setup PostgreSQL Database:

Install and configure PostgreSQL on your local machine or a remote server.
Create a new database for your Django project using the PostgreSQL command line or a GUI tool like pgAdmin.
Configure Django settings to connect to the PostgreSQL database.

4. Define Django Models:

Define Django models to represent the data retrieved from the NYC OpenData API.
Define fields and relationships in the models to match the structure of the data.
Use Django's ORM to define database tables and manage interactions with the database.

5. Load Data into PostgreSQL Database:

Write Python scripts or Django management commands to load the processed data into the PostgreSQL database.
Use Django's ORM to save instances of your models to the database.

6. Data Processing and Visualization (Optional):

Implement data processing and analysis features within Django views or Python scripts.
Integrate data visualization libraries like Matplotlib or Plotly for generating charts and graphs.
Render visualizations in HTML templates for user interaction.

7. Testing and Deployment:

Test the application locally to ensure all features work as expected.
Deploy the application to a production server using platforms like Heroku, AWS, or DigitalOcean.
Monitor the application's performance and troubleshoot any issues.

```

```

```

```

```

```
