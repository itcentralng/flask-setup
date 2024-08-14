# Flask-Setup

Flask-Setup is an open-source and user-friendly tool designed to help you set up a Flask project in under 10 minutes. With a single `fs` command, it takes care of all your CRUD operations (HTTP methods) such as post, get, put, and delete automatically.

Imagine skipping the tedious setup process and diving straight into building your application's features. Flask-Setup does the heavy lifting, so you can focus on what truly matters rather than setting up boilerplate code.

Explore more and see how Flask-Setup can streamline your Flask development at the [Flask-Setup PyPI page](https://pypi.org/project/flask-setup/).

# Getting Started

If you have any questions that are beyond the scope of the documentation, Please feel free to [email us](mailto:nasir@mrteey.com).

## Installation

Make sure [Python](https://www.python.org/downloads/) is installed on your system (Windows, Linux, macOS). Then, run the following command:

```python
pip install flask-setup
```

## Upgrade

To upgrade Flask-Setup to the latest version, run the following command:

```python
 pip install --upgrade flask-setup
```

## Usage

To use Flask-Setup, run the `fs` command followed by the desired argument (`fs command argument`) in the terminal. Here are the available commands:

- build
- init
- add
- remove
- install
- uninstall
- start

The arguments can be a project name, blueprint name, and/or field names with their respective data types.

## Commands

### build

This creates a new project with the specified name.

```python
fs build projectname
```

### init

This initialises a `.fs` file in the root directory of an existing Flask project, enabling seamless use of Flask-Setup `fs` commands.

```python
fs init
```

### migrate

This migrates older version of a flask-setup project (v0.6.1 and below) to the latest version.

```python
fs migrate
```

### add

This command adds a blueprint with the name 'api' and the specified model fields.

```python
fs add api ..fields
```

- Supported field types include `str` (optional), `int`, `float`, `bool`, `date`, `fk`, `rel`.
- Example usage:
  - `fs add category name:str news:rel=news`
  - `fs add news title:str date:date body views:int category_id:fk=category.id`

In the first example, a blueprint named 'category' will be created with the a `str` field 'name' and a relationship with the model 'news'.

In the second example, a blueprint named 'news' will be created with the specified model fields. Note that the `str` field type for `body` is optional and has been omitted.

### remove

This will remove the blueprint named 'api' from the project.

```python
fs remove api
```

### install

This will install the specified module "flask" and freeze it to the requirements file.

```python
fs install flask
```

### uninstall

This will uninstall the specified module "flask" and remove it from the freeze requirements file.

```python
fs uninstall flask
```

### start

This will start the server.

```python
fs start
```

## Model Changes

> [!Note]
> To create database tables or apply model changes, perform the following database migration and upgrade steps:

```python
flask db migrate -m "migration message"
```

```python
flask db upgrade
```
