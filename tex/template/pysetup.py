\begin{pycode}
import os.path
from jinja2 import Environment, FileSystemLoader

template_folder = 'templates'
env = Environment(loader=FileSystemLoader(template_folder))

def tpl(template, **kwargs):
    template_file = os.path.join(template_folder, template)
    mytemplate = env.get_template(template)
    pytex.add_dependencies(template_file)
    print('\\addFileDependency{' + template_file + '}')
    return mytemplate.render(**kwargs)

\end{pycode}
