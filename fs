#!/usr/bin/env python

# Build
# python setup.py bdist_wheel
# Test Install
# python -m pip install dist/project-version-py3-none-any.whl
# Upload
# python -m twine upload dist/project-version-py3-none-any.whl

from flask_setup import run

if __name__ == "__main__":
    run()