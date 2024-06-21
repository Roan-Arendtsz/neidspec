from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='neidspec',
      version='0.0.1',
      description='Package to work with NEID Spectra',
      long_description=readme(),
      url='https://github.com/TeHanHunter/neidspec',
      author='Te Han, Gudmundur Stefansson (author of HPFSpec)',
      author_email='tehanhunter@gmail.com',
      install_requires=['barycorrpy>=0.3.4','astroquery','crosscorr'],
      # install_requires=['barycorrpy>=0.3.4','astroquery'],#,'crosscorr'],
      packages=find_packages(),
      license='GPLv3',
      classifiers=['Topic :: Scientific/Engineering :: Astronomy'],
      keywords='NEID Spectra Astronomy',
      package_data={'neidspec': ['data/neidmasterfile/*']},
      include_package_data=True
      )
