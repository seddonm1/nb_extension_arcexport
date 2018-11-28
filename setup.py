from setuptools import setup

setup(name='ArcExporter',
      version='0.0.1',
      description='Export Jupyter notebook as Arc .json file',
      author='Mike Seddon',
      author_email='',
      license='MIT',
      packages=['arcexport'],
      entry_points={
          'nbconvert.exporters': [
              'arcexport = arcexport:ArcExporter'
          ],
      },
      zip_safe=False)
