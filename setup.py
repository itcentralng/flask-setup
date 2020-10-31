from setuptools import setup, find_packages
with open("README.md", "r") as fh:
    long_description = fh.read()
    setup(
     name='flask_setup',  
     version='0.2.4',
     scripts=['fs'] ,
     author="Nasir Mustapha",
     author_email="nasir@mrteey.com",
     description="A simple tool to help you setup a flask project for web development, API development and just any basic app",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/mrteey/flask-setup",
     packages=find_packages(),
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