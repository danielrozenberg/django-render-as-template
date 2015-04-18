# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-render-as-template',
    version='1.0.0',
    description='A template tag for Django that takes a string and renders as it if it was a template.',
    long_description=long_description,
    url='https://github.com/daniboy/django-render-as-template',
    author='Daniel Rozenberg',
    author_email='me@danielrozenberg.com',
    license='ISC',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='template templates template-engine flatpages',
    packages=['render_as_template', 'render_as_template.templatetags'],
    install_requires=['django'],
)
