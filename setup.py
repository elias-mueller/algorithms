from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='algorithms',
    version='0.1.0',
    long_description=readme,
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
