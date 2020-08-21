#!/usr/bin/env python

from fs.config import args

from fs.methods import initialize_setup, get_project_name, build_app

from fs.generators import generate_blueprint, generate_marshmallow, generate_model

def do_work():

    #Run if VENV is activated
    if hasattr(sys, 'real_prefix'):
        project = get_project_name()

        if args.init:
            #Create .flask_setup file with project name inside
            return initialize_setup(args.init)
        
        elif args.build:
            return build_app(args.build)
        
        #Check for generate request first
        elif args.generate:
            if args.blueprint:
                return generate_blueprint()
            
            elif args.marshmallow:
                return generate_marshmallow()

            elif args.model:
                return generate_model()
        
        #Check for destroy request next
        elif args.destroy:
            if args.blueprint:
                return destroy_blueprint(args.blueprint)
            
            elif args.marshmallow:
                return destroy_marshmallow(args.marshmallow)
            
            elif args.model:
                return destroy_model(args.model)
    print('Please make sure you have virtual environment installed and activated')
    return False