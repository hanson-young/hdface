import sys
from setuptools import setup, setuptools
from src import  __version__

__author__ = "hanson"


def readme():
    with open("README.md",encoding="UTF-8") as f:
        return f.read()


# if sys.version_info < (3, 4, 1):
#     sys.exit("python < 3.4.1 is not supported yet!")

setup(
    name='hdface',
    version=__version__,
    description='heils face detector',
    long_description=readme(),
    url = '',
    author='hanson',
    author_email='yj@heils.cn',
    license="MIT",
    packages = setuptools.find_packages(exclude=["tests.*", "tests"]),
    install_requires=[
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',

        # 'Programming Language :: Python :: 3.6',

    ],
    test_suite='nose.collector',
    tests_require=['numpy','torchvision','pytorch'],
    include_package_data=True,
    keywords="mtcnn face detection tensorflow pip package",
    zip_safe=False)