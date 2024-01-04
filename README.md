
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="stylesheet" href="style.css" />

</head>

<body>
  <h1>
    Welcome To My Flask App!
  </h1>
  <h2>About Flask</h2>
  <p>
    Flask is a lightweight and versatile web application framework for Python. It provides tools, libraries, and technologies for building web applications quickly and efficiently. Flask is known for its simplicity and flexibility, making it a great choice for both beginners and experienced developers
  </p>
  
  <h2>Feautures</h2>
  <p><b>Minimalistic:</b> Flask keeps its core simple while allowing for easy customization.<br><br>
<b>Extensible:</b> It's designed to be easily extensible with various libraries and extensions.<br><br>
<b>Jinja Templating:</b> Utilizes Jinja2 templating engine for flexible and powerful HTML rendering.<br><br>
<b>Built-in Development Server:</b> Comes with a built-in development server for testing and debugging.<br><br>
<b>RESTful Request Handling:</b> Supports RESTful request dispatching.</p>  

  <h2>Resources:</h2>
    <a href="https://flask.palletsprojects.com/en/3.0.x/">Flask Documentation</a><br>
    <a href="https://realpython.com/flask-project/">Build from scratch</a><br>
    <a href="https://jinja.palletsprojects.com/en/3.1.x/">Jinja Templating</a>
    
</body>

</html>

 # Esoteric: A Simple Flask App with SQLAlchemy

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

4. Create a MySQL database named `esoteric`.
5. Create a table named `connect` in the `esoteric` database with the following columns:

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


