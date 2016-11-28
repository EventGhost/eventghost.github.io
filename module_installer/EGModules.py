import os
import pip
from setuptools.command import easy_install

modulepath = os.path.dirname(os.path.realpath(__file__))


pipupgrades = (['install', '--upgrade', 'pip'], ['install', '--upgrade', 'setuptools'])
pipinstalls = pipupgrades + tuple(['install', modulepath + '\\' + f] for f in os.listdir(modulepath) if f.endswith('.whl'))

easyinstalls = tuple([modulepath + '\\' + f] for f in os.listdir(modulepath) if f.endswith('.zip'))

for module in pipinstalls:
    print(module)
    pip.main(module)

for module in easyinstalls:
    print(module)
    easy_install.main(module)
