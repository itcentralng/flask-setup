from setuptools import setup, find_packages
with open("README.md", "r") as fh:
    long_description = fh.read()
    setup(
     name='flask_setup',  
     version='0.3.0',
     scripts=['fs'] ,
     author="Nasir Mustapha",
     author_email="nasir@mrteey.com",
     description="A simple tool to help you setup a flask project for web development, API development and just any basic app",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/mrteey/flask-setup",
     packages=find_packages(),
     data_files=[('apps', [
         'flask_setup/apps/api/config/__init__.py',
         'flask_setup/apps/api/projectname/__init__.py',
         'flask_setup/apps/api/.env',
         'flask_setup/apps/api/.gitignore',
         'flask_setup/apps/api/run.py',

         'flask_setup/apps/basic/config/__init__.py',
         'flask_setup/apps/basic/projectname/__init__.py',
         'flask_setup/apps/basic/projectname/static/css/style.css',
         'flask_setup/apps/basic/projectname/static/js/script.js',
         'flask_setup/apps/basic/projectname/templates/index.html',
         'flask_setup/apps/basic/.env',
         'flask_setup/apps/basic/.gitignore',
         'flask_setup/apps/basic/run.py',
         ]),
      ('generators', [
          'flask_setup/generators/blueprint/__init__.py',
          'flask_setup/generators/blueprint/routes.py',
          'flask_setup/generators/blueprint/static/css/style.css',
          'flask_setup/generators/blueprint/static/js/script.js',
          'flask_setup/generators/blueprint/templates/blueprintname/index.html',
          'flask_setup/generators/marshmallow.py',
          'flask_setup/generators/model.py',
          ])],
     include_package_data=True,
     entry_points={
        'console_scripts': [
            'fs=flask_setup:do_work',
        ]
    },
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )