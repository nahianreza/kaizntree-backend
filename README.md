# Kaizntree API 

## Introduction
The Kaizntree API is a versatile backend application designed to manage an inventory of items, including their categories and tags. This document provides a guide to setting up the project, running the application and consuming the API endpoints.

## Setup Intructions
### Prequisites
* Python 3.8 or higher
* pip and virtual environment
* Git

### Installation
1. #### Cloning the repository

2. #### Creating and activating a virtual environment

    For Windows:

    python -m venv venv
    .\venv\Scripts\activate

    For macOS and Linux:

    python3 -m venv venv
    source venv/bin/activate

3. #### Installing Dependencies

    pip install -r requirements.txt

4. #### Applying migrations

    python manage.py makemigrations
    python manage.py migrate

5. #### Running the server

    python manage.py runserver

    The appplication now can be accessible at `http://127.0.0.1:8000/`.
    The browsable API for the endpoints can be accessed at `http://127.0.0.1:8000/api/`

## API documentation


