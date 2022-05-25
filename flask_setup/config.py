import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--init", help="Pass your project name to -i flag e.g. flask_setup -i project_name")
parser.add_argument("-n", "--name", nargs='?', default="", help="optional name of generator")
parser.add_argument("-b", "--build", help="Pass your project type to -b flag e.g. flask_setup -b api. supported project types include: api, basic, standard")
parser.add_argument("-g", "--generate", help="Pass your a name to -g flag e.g. flask_setup -g blueprint. supported generator types include: blueprint, model, marshmallow")
parser.add_argument("-d", "--destroy", help="Pass your a name to -d flag e.g. flask_setup -d blueprint. supported generator types include: blueprint, model, marshmallow")
parser.add_argument("-a", "--add", help="Pass module name to -a flag e.g. flask_setup add flask-wtf.")
parser.add_argument("-r", "--remove", help="Pass module name to -r flag e.g. flask_setup remove flask-wtf.")

args = parser.parse_args()