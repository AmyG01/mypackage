from setuptools import setup, find_packages
setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['test*']),
    license='MIT',
    description=open('README.md').read(), 
    install_requires=['numpy'],
    url='https://github.com/<username>/<package-name>',
    author='<Gugu Mtonjeni>',
    author_email='<gammtonjeni@gmail.com>'
)