from setuptools import setup

setup(name='airlog',
      version='1.0.0',
      description='A tool for logging HAM radio contacts ',
      url='https://github.com/Ewpratten/AirLog',
      author='Evan Pratten',
      author_email='ewpratten@gmail.com',
      license='GPLv3',
      packages=['AirLog'],
      zip_safe=False,
      include_package_data=True,
      instapp_requires=[
      ],
      entry_points = {
            'console_scripts': ['airlog=AirLog.__main__:main'],
      }
      )