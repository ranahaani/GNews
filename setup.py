from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='gnews',
    version='0.0.6',
    author="Muhammad Abdullah",
    author_email="ranahaani@gmail.com",
    description='Search Google News RSS Feed and returns a usable JSON response',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    url='https://github.com/ranahaani/GNews/',
    project_urls={
        'Documentation': 'https://github.com/ranahaani/GNews/blob/master/README.md',
        'Source': 'https://github.com/ranahaani/GNews/',
        'Tracker': 'https://github.com/ranahaani/GNews/issues',
    },
    classifiers=[

        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
