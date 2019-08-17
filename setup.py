import sys
from setuptools import setup, setuptools
# from hdface import __version__

__author__ = "hanson"


def readme():
    with open("README.md",'r') as f:
        return f.read()


if sys.version_info < (3, 4, 1):
    sys.exit("python < 3.4.1 is not supported yet!")

setup(
    name='hdface',
    version="0.1.3",
    description='heils face detector',
    long_description=readme(),
    long_description_content_type="text/markdown",
    url = 'https://github.com/hanson-young/hdface',
    packages=['hdface','hdface.data'],
    package_data = {'': ["*net.data"]},
    author='hanson',
    author_email='hanson.young@foxmail.com',
    license="MIT",
    install_requires=[
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',

        # 'Programming Language :: Python :: 3.6',

    ],
    include_package_data=True,
    keywords="heils face detection pytorch pip package",
    )