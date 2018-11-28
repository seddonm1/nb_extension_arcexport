from setuptools import setup, find_packages

setup(name='ArcExporter',
      version='0.0.1',
      description='Export Jupyter notebook as Arc .json file',
      author='Mike Seddon',
      author_email='',
      license='MIT',
      packages=find_packages(),
      package_data={'templates': ['*']},
      entry_points={
          'nbconvert.exporters': [
              'arcexport = arcexport:ArcExporter'
          ],
      })
