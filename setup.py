"""
Flask-JSONlocale
-------------

This is the description for that library
"""
from setuptools import setup


setup(
    name='Flask-JSONLocale',
    version='1.0',
    url='http://example.com/flask-jsonlocale/',
    license='GNU',
    author='Martin Urbanec',
    author_email='martin@urbanec.cz',
    description='Very short description',
    long_description=__doc__,
    py_modules=['flask_jsonlocale', 'simplejson'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)