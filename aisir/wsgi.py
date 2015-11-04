
import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.abspath(os.path.join(root_path, 'aisir')))
sys.path.insert(0, root_path)
sys.path.insert(0, '/home/aisir/.local/lib/python3.4/site-packages')
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aisir.settings")
application = get_wsgi_application()
