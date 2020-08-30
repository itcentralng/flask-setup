import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='flask_setup',  
     version='0.2.1',
     scripts=['flask_setup'] ,
     author="Nasir Mustapha",
     author_email="nasir@mrteey.com",
     description="A simple tool to help you setup a flask project for web development, API development and just any basic app",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/mrteey/flask-setup",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )