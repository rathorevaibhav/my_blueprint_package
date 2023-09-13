from setuptools import setup, find_packages

setup(
    name='my_blueprint_package',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'my_blueprint': ['static/*', 'templates/*'],
    },
)
