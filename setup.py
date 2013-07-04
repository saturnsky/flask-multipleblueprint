import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='Flask-MultipleBlueprint',
    packages=['flask_multipleblueprint'],
    version=0.1,
    description='Decorate function using multiple blueprints at once.',
    license='MIT License',
    author='Cha, Hojeong',
    author_email='ikadro+flask@gmail.com',
    maintainer='Cha, Hojeong',
    maintainer_email='ikadro+flask@gmail.com',
    flatforms='any',
    install_requires=[
        'Flask>=0.8',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
