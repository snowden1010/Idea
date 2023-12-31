[![Run on Repl.it](https://replit.com/badge/github/snowden1010/Shop-WApp)](https://replit.com/new/github/snowden1010/Shop-WApp)

# My E-Commerce Project

This Django project implements a simple e-commerce website using the MVT (Model-View-Template) architecture.

## Project Structure

```plaintext
myecommerceproject/
|-- manage.py
|-- myecommerceproject/
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   |-- asgi.py
|   |-- wsgi.py
|-- myapp/
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- migrations/
|   |   |-- __init__.py
|   |-- models.py
|   |-- tests.py
|   |-- views.py
|   |-- templates/
|   |   |-- base.html
|   |   |-- home.html
|   |   |-- shop/
|   |       |-- product_list.html
|   |       |-- product_detail.html
|   |-- static/
|       |-- css/
|       |-- js/
|       |-- images/
|-- templates/
|   |-- registration/
|       |-- login.html
|       |-- register.html
|-- static/
    |-- css/
    |-- js/
    |-- images/
