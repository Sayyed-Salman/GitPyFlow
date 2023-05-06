# Automating Your Python Application's Workflow: Creating a CI/CD Pipeline with GitHub Actions

## Introduction

Deploying and testing a Python application can be a tedious task. In this article, we will see how to deploy a Python application on GitHub using GitHub Actions.
We will create a simple Python application and then deploy it on GitHub using GitHub Actions. We will also see how to test the application using GitHub Actions.

### What is GitHub Actions?

[GitHub Actions](https://github.com/features/actions) is a platform that allows developers to automate workflows in their repositories. It provides a way to create custom workflows that can be triggered by events, such as code pushes, pull requests, or releases. With GitHub Actions, developers can automate tasks such as building and testing code, deploying applications, and sending notifications.

### What is CI/CD?

Continuous Integration and Continuous Deployment (CI/CD) is a software engineering practice where developers frequently merge their code changes into a central repository, which is then automatically built, tested, and deployed. This ensures that the code changes are always tested and verified, and that the deployed application is always up-to-date.

## Prerequisites

- Basic knowledge of Python
- Basic knowledge of Git
- GitHub account
- [render](https://render.com/) account

## Setting up a workflow for a python application

#### 1) Create a flask application

Create a new directory and create a file named `__init__.py` in it.

Directory structure:

![](/images/filestructure.png)

Add the following code to the file:

1. `app\__init__.py`

```python
from flask import Flask


def create_app(config=None):
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello World'

    @app.route('/add/<int:num1>/<int:num2>')
    def add(num1, num2):
        return f"{num1} + {num2} = {num1 + num2}"

    return app
```

2. `wsgi.py`

```python
from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()
```

Now run the application using the following command:

```bash
python wsgi.py
```

Create a `tests` directory and create a file named `__init__.py` and `test_app.py` in it.
We need to create some test cases for our application, These test cases will be executed in the GitHub Actions workflow.

Add the following code to the file:

```python
import unittest
from app import create_app


app = create_app()


class TestAddFunction(unittest.TestCase):

    def test_addition(self):
        with app.test_client() as client:
            response = client.get('/add/4/5')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data.decode(), '4 + 5 = 9')

    def test_missing_variable(self):
        with app.test_client() as client:
            response = client.get('/add/4/')
            self.assertEqual(response.status_code, 404)

    def test_invalid_variable(self):
        with app.test_client() as client:
            response = client.get('/add/4/foo')
            self.assertEqual(response.status_code, 404)

```

Now run the test cases using the following command:

```bash
python -m unittest discover -s tests
```

All of these test cases should pass.
Finally, we need to create a `requirements.txt` file to install the dependencies.
The only library we need is `flask`. so add the following line to the file:

```txt
flask
```

You can also add other dependencies if you want. For example, if you want to use `pytest` instead of `unittest`, you can add `pytest` to the `requirements.txt` file.
You can also automatically generate this file using the following command

```bash
pip freeze > requirements.txt
```

All the code for this application can be found [here](https://github.com/Sayyed-Salman/GitPyFlow).

#### 2) Create a GitHub repository

1. Create a new repository on GitHub.
2. Push the code to the repository.

Finally, we have a simple Python application that we want to deploy on GitHub.
Not only do we want to deploy the application, but we also want to test it.

#### 3) Create a workflow file

#### 4) Test it
