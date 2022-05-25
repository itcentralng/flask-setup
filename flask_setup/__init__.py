#!/usr/bin/env python
import os

from flask_setup.config import args

from flask_setup.methods import initialize_setup, install, uninstall, helper, get_project_name, destroy_project

from flask_setup.app_builder import build_app

from flask_setup.generators import generate_blueprint, generate_marshmallow, generate_model, destroy_blueprint, destroy_marshmallow, destroy_model

def do_work():

    #Run if VENV is activated
    if os.environ.get('VIRTUAL_ENV'):

        if args.init:
            #Create .fs file with project name inside
            return initialize_setup(args.init)
        
        elif args.build:
            return build_app(args.build)
        
        #Check for generate request first
        elif args.generate:
    
            if args.generate == 'blueprint' or args.generate == 'b':
                return generate_blueprint()
            
            elif args.generate == 'marshmallow' or args.generate == 'm':
                return generate_marshmallow()

            elif args.generate == 'model':
                return generate_model()
        
        #Check for destroy request next
        elif args.destroy:
        
            if args.destroy == 'blueprint' or args.generate == 'b':
                return destroy_blueprint()
            
            elif args.destroy == 'marshmallow' or args.generate == 'm':
                return destroy_marshmallow()
            
            elif args.destroy == 'model':
                return destroy_model()
            
            elif args.destroy == get_project_name():
                return destroy_project()
        
        elif args.add:
            return install([args.add])
        
        elif args.remove:
            return uninstall([args.remove])
        
        return helper()
    print('Please make sure you have virtual environment installed and activated')
    return False