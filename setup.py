from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='kafkaComms',
    version='0.1.7',
    description='Communication director for Kafka cluster',
    long_description=readme,
    author='Noah Jennings',
    author_email='njenn001@odu.edu',
    url='https://github.com/njenn001/kafkaComms',
    license=license,
    packages=['app',]
)