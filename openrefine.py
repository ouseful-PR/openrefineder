import os

def setup_openrefine():
  path = os.path.join(os.environ['HOME'], 'openrefine')
  return {
    'command': ['/home/jovyan/openrefine-2.8/refine', '-p', '{port}','-d',path],
    'port': 3333,
    #The following needs a the labextension installing.
    #eg in postBuild: jupyter labextension install jupyterlab-server-proxy
    'launcher_entry': {
        'enabled': True,
        'icon_path': '/home/jovyan/.jupyter/open-refine-logo.svg',
        'title': 'OpenRefine',
    },
  }
