#!/usr/bin/env python

# PyPI upload:
#
#     $ python -m pip install --upgrade twine wheel
#     $ python setup.py sdist bdist_wheel --universal
#     $ twine upload dist/*
#
# Install in development:
#
#     $ python3 -m pip install -e .

from setuptools import setup

VERSION = "0.2.7"
INSTALL_REQUIRES = ["requests<3.0.0"]
TESTS_REQUIRE = ["pytest"]

if __name__ == "__main__":
    setup(
        name="newsapi-python",
        version=VERSION,
        author="Matt Lisivick",
        author_email="lisivickmatt@gmail.com",
        license="MIT",
        url="https://github.com/mattlisiv/newsapi-python",
        packages=["newsapi"],
        install_requires=INSTALL_REQUIRES,
        tests_require=TESTS_REQUIRE,
        description="An unofficial Python client for the News API",
        download_url="https://github.com/mattlisiv/newsapi-python/archive/master.zip",
        keywords=["newsapi", "news"],
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "Intended Audience :: Financial and Insurance Industry",
            "Intended Audience :: Information Technology",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
        ],
    )
