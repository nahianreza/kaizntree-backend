# Kaizntree API 

## Introduction
The Kaizntree API is a versatile backend application designed to manage an inventory of items, including their categories and tags. This document provides a guide to setting up the project, running the application and consuming the API endpoints.

## Setup Intructions
### Prequisites
* Heroku installed
* Heroku CLI Installed
* Git

#### Cloning the repository

    git clone https://github.com/nahianreza/kaizntree-backend.git
    cd kaizntree-backend

### Installation

1. #### Creating a heroku superuser

    To create a superuser for the admin interface, use the Heroku CLI with the following command:

    heroku run python manage.py createsuperuser --app kaizntree-deploy

    Please follow the instruction to setup an account for the interface


2. #### Accessing the admin interface

    https://kaizntree-deploy-435cd2062fb6.herokuapp.com/admin/login/?next=/admin/

    Please use the username and password created in step 2 for successful login

3. #### Browsing the API

    Once logged into the admin interface, you can navigate to the browsable API:

    https://kaizntree-deploy-435cd2062fb6.herokuapp.com/api/

    The interface allows you to interact with the API endpoints directly. You can perform all CRUD operations and also apply filters to the queries


## API documentation
## Swagger UI

    A detailed API documentation is provided here via Swagger UI. This contains details on all endpoints, query parameters, request formats and response structures:

    https://kaizntree-deploy-435cd2062fb6.herokuapp.com/swagger/

## Consuming the endpoints
   
   To consume the endpoints, you must obtain an authentication token. Send a post request to the following endpoint with your registered superuser credentials:
   https://kaizntree-deploy-435cd2062fb6.herokuapp.com/api/api-token-auth/

   include the payment in the content and replace accordingly:

   ```json
{
  "username": "yourSuperUsername",
  "password": "yourSuperPassword"
}

   Upon successsful authentication, you will receive a token which you can include in the Authorization header of your subsequent API requests:
   Authorization: Token yourReceivedTokenHere
```

Here is an example of how to consume some of the main endpoints

### Create a New Item
* Endpoint: `POST /api/items/`
* Headers:
    * `Authorization: Token <yourToken>`
    * `Content-Type: application/json`
* Body:
```json
{
  "sku": "ITEM-SKU",
  "name": "Random Item Name",
  "category": <new_category_id>,
  "tags": [<new_tag_id>],
  "in_stock": false,
  "available_stock": 50
}
```

## Using cURL

cURL can also be used to consume the API from the command line. 

```sh
# Obtain Token
curl -X POST -d "username=yourSuperUsername&password=yourSuperPassword" https://kaizntree-deploy-435cd2062fb6.herokuapp.com/api/api-token-auth/

# Get List of Items
curl -H "Authorization: Token <yourToken>" https://kaizntree-deploy-435cd2062fb6.herokuapp.com/api/items/
```

## Local Development

To run the API locally, follow these steps:

#### 1. Install Dependencies:

pip install -r requirements.txt

#### 2. Run Migrations to create the schema:

python manage.py migrate

#### 3. Create superuser:

python manage.py createsuperuser

#### 4. Start the development server:

python manage.py runserver

#### 5. Navigate the server:

The appplication now can be accessible at http://127.0.0.1:8000/.

The admin page can be accessible at http://127.0.0.1:8000/admin/

The browsable API for the endpoints can be accessed at http://127.0.0.1:8000/api/






