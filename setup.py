from setuptools import setup, find_packages
import sys, os

version = "0.1"

setup(name='RescueDelicious',
      version=version,
      description="Convert bookmarks in delicious firefox extension to importable file",
      long_description="",
      classifiers=[], # Get strings from http://bit.ly/tYt3j
      keywords='',
      author="Qiangning Hong",
      author_email="hognqn@gmail.com",
      url="",
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples*', 'tests*']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'pydelicious',
      ],
      entry_points="""
      [console_scripts]
      rescue-delicious = rescuedel.rescue:main
      """,
      tests_require=['nose'],
      test_suite='nose.collector',
)
