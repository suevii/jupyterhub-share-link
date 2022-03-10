from traitlets.config import get_config
import sys
from jupyterhub.spawner import SimpleLocalProcessSpawner



c = get_config()

c.JupyterHub.spawner_class = SimpleLocalProcessSpawner

c.ConfigurableHTTPProxy.should_start = False

c.ConfigurableHTTPProxy.auth_token = "6821de66e1de415e9469990b3f2333f2"

c.ConfigurableHTTPProxy.api_url = 'http://localhost:8001'

c.JupyterHub.services = [
    {
        'name': 'share-link',
        'admin': True,
        'url': 'http://127.0.0.1:21211',
        'command': [
            sys.executable, '-m', 'jupyterhub_share_link.run',
            # '--log-file-prefix=/var/log/jupyterhub_share_link.log'
        ],
    }
]
c.JupyterHub.admin_access = True  # Service needs to access user servers.

c.JupyterHub.allow_named_servers = True
# c.Spawner.cmd = ['jupyter-labhub']

c.JupyterHub.authenticator_class = 'jupyterhub.auth.DummyAuthenticator'


c.Spawner.default_url = '/lab'

