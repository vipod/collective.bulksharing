from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='collective.bulksharing',
      version=version,
      description="This packages allows setting local roles for multiple items inside folder in one run.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Vitaliy Podoba',
      author_email='vitaliypodoba@gmail.com',
      url='https://github.com/vipod/collective.bulksharing',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone

      """,
      )
