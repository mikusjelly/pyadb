import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8').read()


setup(
    name="pyadb3",
    version="1.0.1",
    author="mikusjelly",
    author_email="mikusjelly@gmail.com",
    description=(
        "Simple python module to interact with Android Debug Bridge tool"),
    license="BSD",
    keywords="python android adb",
    url="https://github.com/mikusjelly/pyadb3",
    packages=['pyadb3'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: BSD License",
    ],
)
