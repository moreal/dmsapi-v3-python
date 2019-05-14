import setuptools
from setuptools import setup

setup(
    url='https://github.com/dmsapi/python',
    name='dmsapi',
    version='0.1.0',
    long_description='DMS API :)',
    description='Simple DSM-DMS API',
    author='moreal',
    author_email='dev.moreal@gmail.com',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities'
    ]
)