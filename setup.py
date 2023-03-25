from setuptools import setup, find_packages

setup(
    name='census-income',
    version='0.0.1',
    long_description='Demo Machine Learning Project with complete pipelime',
    author='Saurabh Gupta',
    author_email='saurabhg2083@gmail.com'
    packages=find_packages(),
    install_requirements=['pandas','numpy','flask','matplotlib']


)