# flask-setup #
Flask Setup Tool

# INSTALLATION #
`$ pip install flask-setup`

# USAGE #

1. create a virtual environment and activate it, the run an fs command:
   `$ fs command argument`

# COMMANDS #

1. build: Builds the project.
    `$ fs build [project name]`

2. add: Takes blueprint name e.g.
    `$ fs add api` this will add a blueprint with the name 'api'

3. remove: Takes blueprint name e.g.
    `$ fs remove api` this will remove the blueprint with the name 'api'

4.  install: pass this alongside a module e.g.:
    `$ fs install flask` this will install flask and freeze to requirements file

5.  uninstall: pass this alongside a module e.g.:
    `$ fs uninstall flask` this will uninstall flask and freeze to requirements file

6.  destroy: This will destroy the current project e.g.:
    `$ fs destroy`

7.  init: Initializes fs on an existing project with similar setup e.g.:
    `$ fs init`
