# Django WebShop

This is webstore example built with Django. I used Visual Studio Code as an IDE.

Last changes 21.03.2021.

The features what the webshop should have are following:
1. Product search
a. Search with product name and product code
b. Sorting of the search results by product name and price
2. Product information
a. Feature displaying detailed product information
3. Shopping chart
a. Adding products to shopping chart without refreshing the page eg. With Ajax technology or other modern UI technology
4. Product addition
a. Features to add products to the store

## Running this project

To get this project up and running you should start by having Python installed on your computer.
This application uses MySql database, so it's good to have MySQL WorkBench installed on your machine.

The database settings are in the file ..\Webshop\productlist\settings.py. If you want to use another database, change the settings according your needs.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'webshopdb',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

You can create database in MySQL workbench using commands like these:

show databses;
create database webshopdb;
use webshopdb;

It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with (mac/linux)

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project (for example c:\Users\Timo\Webshop)

```
virtualenv env
```

That will create a new folder `env` in your project directory. Next activate it with this command on mac/linux:

```
source env/bin/activate
```

In windows the commands are:

```
cd env/Scripts
activate
```

Then install the project dependencies with

```
pip install -r requirements.txt   The requirements.txt file is in Webshop directory.
```

Run command 
```
python manage.py makemigrations
```

and 

```
python manage.py migrate
```
to create tables in the database.

You can create admin user, if you want by this command 
```
python manage.py createsuperuser
```

Now you can run the project with this command

```
python manage.py runserver
```

There is no need to login to this application.

You can add products to this application. Select Home or click logo to see the product list. 
You can search by entering a part of product name or product code. Press add to cart in order to shop something. Press cart icon to see the contents of your shopping cart.

Missing features: Checkout is not implemented yet.
