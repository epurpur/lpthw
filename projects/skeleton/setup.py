try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Skeleton Test',
    'author': 'Erich Purpur',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'epurpur@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['Name'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
