from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='gnews',
    version='0.0.4',
    author="Muhammad Abdullah",
    author_email="ranahaani@gmail.com",
    description='Search Google News RSS Feed and returns a usable JSON response',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    project_urls={
        'Documentation': 'https://github.com/ranahaani/GNews/blob/master/README.md',
        'Source': 'https://github.com/ranahaani/GNews/',
        'Tracker': 'https://github.com/ranahaani/GNews/issues',
    },
)