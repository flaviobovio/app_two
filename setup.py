#setup.py for app_two
from setuptools import setup, find_packages

setup(
    name='app_two',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',  # or your chosen license
)
