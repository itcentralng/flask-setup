# flask-setup #
Flask Setup Tool

# INSTALLATION #
`$ pip install flask-setup`

# USAGE #

1. run an fs command:
   `$ fs command argument`

# COMMANDS #

1. build: Build a project with given name.
    `$ fs build projectname`

2. add: Takes blueprint name e.g.
    `$ fs add api ..fields` this will add a blueprint with the name 'api' and given model fields

3. remove: Takes blueprint name e.g.
    `$ fs remove api` this will remove the blueprint with the name 'api'

4. copy: Takes blueprint name e.g.
    `$ fs copy bp_to_copy bp_to_paste` this will copy the blueprint with the name 'bp_to_copy' to 'bp_to_paste'

5.  install: pass this alongside a module e.g.:
    `$ fs install flask` this will install flask and freeze to requirements file

6.  uninstall: pass this alongside a module e.g.:
    `$ fs uninstall flask` this will uninstall flask and freeze to requirements file

7.  destroy: This will destroy the current project e.g.:
    `$ fs destroy`

8.  init: Initializes fs on an existing project with similar setup e.g.:
    `$ fs init` this will create a .fs file in the root directory of the project

9. start: Starts the server e.g.:
    `$ fs start` this will start the server
