import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-comments-spamfighter',
    version='0.1',
    description="A Django app that contributes Akismet and Keyword blocking to your django comments.",
    long_description=read('README'),
    author='Martin Mahner',
    author_email='martin@mahner.org',
    license='BSD',
    url='http://bitbucket.org/barttc/django-comments-spamfighter/',
    download_url='http://bitbucket.org/barttc/django-comments-spamfighter/downloads/',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    package_data = {},
    zip_safe=False,
)
