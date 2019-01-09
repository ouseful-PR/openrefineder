import os

def setup_openrefine():
  path = os.path.join(os.environ['HOME'], 'openrefine')
  return {
    'command': ['/home/jovyan/openrefine-2.8/refine', '-p', '{port}','-d',path]
  }
