from setuptools import setup
import sys, os

if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist bdist_wheel upload; git push")
    sys.exit()

setup(name="pycwl",
        version='0.1.0',
        description='',
        author='Kenzo-Hugo Hillion and Hervé Ménager',
        author_email='kehillio@pasteur.fr and hmenager@pasteur.fr',
        keywords = ['cwl'],
        install_requires=['pyaml'],
        packages=["pycwl"],
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Topic :: Scientific/Engineering :: Bio-Informatics',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'Environment :: Console',
            ],
        )