from setuptools import setup, find_packages

# setup(
#     name='my_blueprint_package',
#     version='0.1',
#     packages=find_packages(),
#     include_package_data=True,
#     package_data={
#         'my_blueprint': ['static/*.css', 'templates/*.html'],
#     },
# )

extras_require = {
    'aws': ['boto'],
    'azure': ['azure-storage-blob']
}


install_requires = [
    'Flask>=0.7',
    'wtforms'
]

setup(
    name='my_blueprint_package',
    version='0.1',
    url='https://github.com/rathorevaibhav/my_blueprint_package/',
    license='BSD',
    python_requires='>=3.6',
    author='ColoredCow',
    author_email='vaibhav@coloredcow.com',
    description='this is short description',
    long_description='this is long description',
    packages=['my_blueprint'],
    package_data={
        'my_blueprint': ['static/*.css', 'templates/*.html'],
    },
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    extras_require=[],
    install_requires=[],
    tests_require=[],
    classifiers=[]
)
