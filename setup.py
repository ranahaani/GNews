from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='gnews',
    version='0.0.2',
    author="Muhammad Abdullah",
    author_email="ranahaani@gmail.com",
    description='Search Google News RSS Feed and returns a usable JSON response',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
)