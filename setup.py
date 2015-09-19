# -*- coding: utf-8 *-
# setup.py
# modeled after recommended example on packaging.python.org
# https://github.com/pypa/sampleproject/blob/master/setup.py

from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

_classifiers = ["Development Status :: 3 - Alpha",
                "Operating System :: POSIX :: Linux",
                "Programming Language :: Python :: 3",
                "Programming Language :: Python :: 3.4",
                "Programming Language :: Python :: 3.5"]

setup(name="lwapythoncrashcourse",
      version="0.0.1",
      description="lern2python",
      long_description="Maybe you're curious, or maybe you're a grown-up and typing `Button button = new Button(); // makes a new button` feels condescending. Learn to use a sane language",
      author="Nathan Shurte",
      author_email="nshurte@royall.com",
      license="©2015 Animal Control Labs a/k/a org.animalcontrol. All rights reserved.",
      classifiers=_classifiers,
      keywords="pedantic learning lern larning language",
      install_requires=[ ],
      packages=find_packages(exclude=("dnsreconciler.tests",
                                      "iython_cluetrail",
                                      "test",
                                      "tests")),
      entry_points={ "console_scripts" : ["lwanoob=noob:main",
                                          "lwalessnoob=lessnoob:main"] })
