import setuptools
from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(
    url='https://github.com/dmsapi/python',
    name='dmsapi',
    version='0.1.2',
    long_description=readme,
    long_description_content_type='text/markdown',
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