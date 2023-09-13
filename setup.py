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
    packages=find_packages(),
    include_package_data=True,
     package_data={
        '': ['static/*', 'templates/*'],
    },
    zip_safe=False,
    platforms='any',
    extras_require=extras_require,
    install_requires=install_requires,
    tests_require=[
        'pytest',
        'pillow>=3.3.2',
        'mongoengine',
        'pymongo',
        'wtf-peewee',
        'sqlalchemy',
        'flask-mongoengine<=0.21.0',
        'flask-sqlalchemy',
        'flask-babelex',
        'shapely',
        'geoalchemy2',
        'psycopg2',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    test_suite='flask_admin.tests'
)
