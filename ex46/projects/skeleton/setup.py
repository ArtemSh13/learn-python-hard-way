try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My project',
    'author': 'ArtemSh13',
    'url': 'https://www.myproject.com',
    'download_url': 'https://www.myproject.com/download',
    'author_email': 'artemsh13@icloud.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
