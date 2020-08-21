#!/usr/bin/env python
import os

from fs.config import args

from fs.methods import initialize_setup, install, uninstall, helper

from fs.app_builder import build_app

from fs.generators import generate_blueprint, generate_marshmallow, generate_model, destroy_blueprint, destroy_marshmallow, destroy_model

def do_work():

    #Run if VENV is activated
    if os.environ.get('VIRTUAL_ENV'):

        if args.init:
            #Create .flask_setup file with project name inside
            return initialize_setup(args.init)
        
        elif args.build:
            return build_app(args.build)
        
        #Check for generate request first
        elif args.generate:
    
            if args.generate == 'blueprint':
                return generate_blueprint()
            
            elif args.generate == 'marshmallow':
                return generate_marshmallow()

            elif args.generate == 'model':
                return generate_model()
        
        #Check for destroy request next
        elif args.destroy:
        
            if args.destroy == 'blueprint':
                return destroy_blueprint()
            
            elif args.destroy == 'marshmallow':
                return destroy_marshmallow()
            
            elif args.destroy == 'model':
                return destroy_model()
        
        elif args.install:
            return install([args.install])
        
        elif args.uninstall:
            return uninstall([args.uninstall])
        
        return helper()
    print('Please make sure you have virtual environment installed and activated')
    return False