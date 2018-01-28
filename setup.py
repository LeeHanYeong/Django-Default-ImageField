import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-default-imagefield',
    version='0.4',
    description='Default static path for Django ImageField',
    long_description=README,
    author='Lee HanYeong',
    author_email='dev@azelf.com',
    license='MIT',
    packages=['django_fields'],
    url='https://github.com/LeeHanYeong/Django-Default-ImageField',
    zip_safe=False,
    scripts=['bin/django-fields'],
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
)
