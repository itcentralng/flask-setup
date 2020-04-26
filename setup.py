import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='flask_setup',  
     version='0.1',
     scripts=['flask_setup'] ,
     author="Nasir Mustapha",
     author_email="nasir@mrteey.com",
     description="A simple flask project starter",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/mrteey/flask-starter",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )