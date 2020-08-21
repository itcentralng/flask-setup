import argparse, sys

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--init", help="Pass your project name to --init flag e.g. flask_setup --init project_name")
parser.add_argument("-b", "--build", help="Pass your project type to --build flag e.g. flask_setup --build api. supported project types include: api, basic, standard")
parser.add_argument("-bp", "--blueprint", nargs='?', default="api", help="Pass your blueprint name to --blueprint flag e.g. flask_setup --generate blueprint -blueprint api")
parser.add_argument("-g", "--generate", help="Pass your generator name to --generate flag e.g. flask_setup --generate blueprint. supported generator types include: blueprint, model, marshmallow")
parser.add_argument("-d", "--destroy", help="Pass your generator name to --destroy flag e.g. flask_setup --destroy blueprint. supported generator types include: blueprint, model, marshmallow")
parser.add_argument("-install", "--install", help="Pass module name to --install flag e.g. flask_setup --install flask-wtf.")
parser.add_argument("-uninstall", "--uninstall", help="Pass module name to --uninstall flag e.g. flask_setup --uninstall flask-wtf.")

args = parser.parse_args()