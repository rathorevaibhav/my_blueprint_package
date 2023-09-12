from setuptools import setup, find_packages

setup(
    name='my-blueprint-package',
    version='0.1',
    packages=find_packages(),
    package_data={
        'my_blueprint': ['static/*', 'templates/*'],
    },
)
