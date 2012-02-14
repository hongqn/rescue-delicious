from setuptools import setup, find_packages
import sys, os

version = "0.1"

setup(name='RescueDelicious',
      version=version,
      description="Convert bookmarks in delicious firefox extension to importable file",
      long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Topic :: Utilities',
      ],
      author="Qiangning Hong",
      author_email="hognqn@gmail.com",
      url="https://github.com/hongqn/rescue-delicious",
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
