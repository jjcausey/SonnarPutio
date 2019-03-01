from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='sonarr_putio',
    version='0.1',
    long_description=open('README.md').read(),
    author='jjcausey',
    url='https://github.com/jjcausey/SonnarPutio',
    packages=find_packages(exclude=('tests',)),
    install_requires=requirements,
    lincense='???',
    entry_points={
        'console_scripts': ['sonarr_putio=sonarr_putio.cli:cli'],
    },
)
