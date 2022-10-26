# Getting Started

This project was created with [FLASK-SETUP](https://github.com/mrteey/flask-setup).

## Initial Setup
Please follow the following steps to get started with this project.
1. Create a .env file
2. Create a virtual environment
3. Activate the virtual environment
4. Install the requirements
5. Run migration upgrade
6. Run the application

## Content of your .env file:
```DATABASE_URI=your-database-uri```

## Create a virtual environment
```python3 -m venv venv```

## Activate the virtual environment
```source venv/bin/activate```

## Install the requirements
```pip install -r requirements.txt```

## Run migration upgrade
```flask db upgrade```

## Run the application
```./run```

Some commands you can run with flask-setup:
<br />
```fs add blueprint_name```
<br />
```fs remove blueprint_name```
<br />
```fs copy blueprint_name_to_copy blueprint_name_to_paste```
<br />
```fs install library-name```
<br />
```fs uninstall library-name```
<br />
