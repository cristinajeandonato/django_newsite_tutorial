from setuptools import setup, find_packages

setup(
    name = "steelrumors",
    version = "1.0",
    description = "news about man of steel",
    author = 'Cristina Donato',
    author_email='cristinajeandonato@gmail.com',
    packages = ['steelrumors'],
    package_dir = {'': 'src/steelrumors'},
    install_requires = ['setuptools'],
)
