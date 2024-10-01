 # Eso: A Simple Flask App with SQLAlchemy

This repository contains the code for a simple Flask application that uses SQLAlchemy to connect to a MySQL database and perform basic CRUD operations. The application allows users to enter their email addresses, which are then stored in the database. Users can also view all the email addresses that have been entered.

## Prerequisites

To run this application, you will need the following:

* Python 3.6 or later
* Flask
* SQLAlchemy
* MySQL Connector/Python

## Installation

1. Clone this repository to your local machine.
2. Create a virtual environment and activate it.
3. Install the required Python packages:

```
pip install -r requirements.txt
```

4. Create a MySQL database named `eso`.
5. Create a table named `connect` in the `eso` database with the following columns:

```
id INT NOT NULL AUTO_INCREMENT,
email VARCHAR(50) NOT NULL,
PRIMARY KEY (id)
```

## Usage

To run the application, simply run the following command:

```
python app.py
```

The application will be available at `http://localhost:5000`.

## Features

The application has the following features:

* Users can enter their email addresses, which are then stored in the database.
* Users can view all the email addresses that have been entered.

## Code Overview

The application is structured as follows:

* `app.py`: The main Flask application file.
* `templates`: The Jinja2 templates.

### `app.py`

The `app.py` file is the main Flask application file. It creates the Flask application, configures the SQLAlchemy database connection, and defines the routes.

```python
from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'YOUR_MySQL_URI'


db = SQLAlchemy(app)
```


