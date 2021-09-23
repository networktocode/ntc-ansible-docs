from setuptools import find_packages, setup

setup(name='module_formatter',
      version='0.0.1',
      packages=['module_formatter'],
      package_data={'module_formatter': ['templates/*.j2']},
      install_requires=['ansible==4.2.0',
                        'jinja2',
                       ]
      )