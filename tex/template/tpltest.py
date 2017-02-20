from jinja2 import Environment, FileSystemLoader

template_folder = 'templates'
env = Environment(loader=FileSystemLoader(template_folder))

import ipdb; ipdb.set_trace()
mytemplate = env.get_template('mytemplate.tex')
