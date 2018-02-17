# For setup... I think. Never really flushed this out

try:
    from setuptools import setup
except ImportError:
    from disutils.core import setuptools

config = {
    'description': 'My Project',
    'author' : 'Anthony Herrera',
    'url' : 'URL to get it',
    'download_url' : 'where to download',
    'author_email' : 'My email',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'packages' : ['NAME'],
    'scripts' : [],
    'name' : 'project name'
}
