from setuptools import setup, find_packages
with open("README.md", "r") as fh:
    long_description = fh.read()
    setup(
     name='flask_setup',  
     version='0.5.3',
     scripts=['fs'] ,
     author="Nasir Mustapha",
     author_email="nasir@mrteey.com",
     description="A simple tool to help you setup a flask project quickly",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/mrteey/flask-setup",
     packages=find_packages(),
     install_requires=['typer'],
     data_files=[('starter', [
         
         'flask_setup/starter/app/user/controller.py',
         'flask_setup/starter/app/user/model.py',
         'flask_setup/starter/app/user/schema.py',
         
         'flask_setup/starter/app/celery/__init__.py',
         'flask_setup/starter/app/celery/tasks.py',
         
         'flask_setup/starter/app/__init__.py',
         'flask_setup/starter/app/error_handlers.py',
         'flask_setup/starter/app/route_guard.py',
         
         'flask_setup/starter/config/__init__.py',
         'flask_setup/starter/config/db.py',
         'flask_setup/starter/config/jwt.py',
         'flask_setup/starter/config/mail.py',
         'flask_setup/starter/config/celery.py',
         
         'flask_setup/starter/helpers/__init__.py',
         'flask_setup/starter/helpers/upload_helper.py',
         
         'flask_setup/starter/main.py',
         'flask_setup/starter/manage.py',
         
         'flask_setup/starter/Dockerfile',
         'flask_setup/starter/supervisord.conf',
         'flask_setup/starter/requirements.txt',
         'flask_setup/starter/run',
         'flask_setup/starter/.env',

         ]),
      ('generators', [
          'flask_setup/generators/blueprint/controller.py',
         'flask_setup/generators/blueprint/model.py',
         'flask_setup/generators/blueprint/schema.py',

         'flask_setup/generators/samples/sample.model.py',
         'flask_setup/generators/samples/sample.schema.py',
         'flask_setup/generators/samples/user.model.py',
          ])],
     include_package_data=True,
     entry_points={
        'console_scripts': [
            'fs=flask_setup:run',
        ]
    },
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )