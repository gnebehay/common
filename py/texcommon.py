import os

from parse import *

def getLatexMain(directory):

    files = os.listdir('.')

    for f in files:
        if f.endswith('.latexmain'):
            result = parse('{}.{}.latexmain', f)
            main_file = result[0]
            return main_file

    return None
