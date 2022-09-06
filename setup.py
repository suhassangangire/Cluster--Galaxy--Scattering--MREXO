from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()



setup(name='mrexo',
      version='0.2',
      description='Nonparametric mass radius relationship for exoplanets',
      long_description=readme(),
      long_description_content_type="text/markdown",
      url='https://github.com/suhassangangire/Cluster--Galaxy--Scattering--MREXO.git',
      author='Suhas Sangangire',
      author_email='suhassangangire2601@gmail.com',
      install_requires=['astropy>2','matplotlib','numpy','scipy'],
      packages=['mrexo'],
      include_package_data = True,
      license='GPLv3',
      classifiers=['Topic :: Scientific/Engineering :: Astronomy & Astrophysics'],
      keywords='Mass-Radius relationship Non parametric Exoplanets' )
