# Shop Management

This is a part of the assignment given. It is an API-based project with the following links

1. signup - provide the username, password, email, first_name and last_name as form-data and pass it for registering a user
2. login - provide the username and passwrd and get an auth token which is valid for 24 hours. All APIs require except login and signup this token in the authorisation header
3. logout - Used to delete auth token if user manually signs out
4. items - Allows GET to view all items available, along with their quantity
5. buy - Allows GET to view items bought by user, and allows POST to let user add items to list by providing item id and quantity required.
6. family - Allows GET to view members part of family, allows POST to let head of family add members to family by their username and password
7. family/buy - Allows GET toview items bought by family, allows POST let any family member add items to family list

# Tech

Shopmanage uses the following:

* Django - as the backend for the services
* DRF- provides the APIs
* mysql - Using AWS RDS for the online mysql DB


# Installation
Shopmanage requires django 3.1 to run.

For linux users
```sh
$ git clone https://github.com/TanmayAmbadkar/shopmanage.git
$ cd gccc-dashboard
$ sudo pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

For windows users with conda
```sh
$ git clone https://github.com/TanmayAmbadkar/shopmanage.git
$ cd gccc-dashboard
$ conda create -n myenv python=3.8
$ conda activate myenv
$ pip install -r requirements.txt
```

To test the app

```sh
$ python manage.py makemigrations && python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```
Open a browser tab and write http://localhost:8000/ to see the website.

You can find the deployed link here. There is no visible homepage yet so you might get an error [link](https://shopmanage.tk/)
