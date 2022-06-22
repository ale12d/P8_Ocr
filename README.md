# P8_Ocr

## Table of contents
* [General info](#general-info)
* [Packages](#packages)
* [Setup Linux](#setup-linux)
* [Setup Windows](#setup-windows)
 
## General info
This project is a web application allowing a community of users to consult or request book reviews on demand.

## Packages
Project is created with:
* asgiref: 3.5.1
* Django: 4.0.4
* Pillow: 9.1.1
* sqlparse: 0.4.2
* tzdata: 2022.1

## Setup Linux
To run this project, install python3 : ```sudo apt install python3.8```

Go in the project folder : ```cd /.../P8_Ocr-main```

Create a virtual environment : ```python3 -m venv env```

Activate the virtual environment : ```source env/bin/activate```

To install directly all packages you need : ```python -m pip install -r requirements.txt```

Create your database: ```python LitReview\manage.py makemigrations```
                        +
                      ```python LitReview\manage.py migrate```

Run the django server : ```python LitReview\manage.py runserver```

To go on your local website:
* http://127.0.0.1:8000/

## Setup Windows
To run this project, write ```python3``` in the cmd to install python3 in microsoft store

Go in the project folder : ```cd \...\P8_Ocr-main```

Create a virtual environment : ```python3 -m venv env```

Activate the virtual environment : ```\Users\...\P8_Ocr-main\env\Scripts\activate.bat```

To install directly all package you need : ```python -m pip install -r requirements.txt```

Create your database: ```python LitReview\manage.py makemigrations```
                        +
                      ```python LitReview\manage.py migrate```
                      
Run the django server : ```python LitReview\manage.py runserver```

To go on your local website:
* http://127.0.0.1:8000/
