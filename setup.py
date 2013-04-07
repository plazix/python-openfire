# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from openfire import get_version


setup(
    name='python-openfire',
    version=get_version().replace(' ', '-'),
    description=u'A python client for openfire’s api',
    license="BSD License",
    author='Aleksandr Zorin (plazix)',
    author_email='plazix@gmail.com',
    url='https://github.com/plazix/python-openfire',
    download_url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
