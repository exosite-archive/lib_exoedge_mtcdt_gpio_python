"""  """
# pylint: disable=I0011,W0312,C0410
import os
from setuptools import setup, find_packages

REQUIREMENTS = ['exoedge', 'six']

def read(fname):
    """ Primarily used to open README file. """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

try:
    README = read('README.rst')
except:
    README = 'README Not Found'

setup(
    name="exoedge_mtcdt_gpio",
    version="18.08.10",
    author="Exosite LLC",
    author_email="support@exosite.com",
    description="An ExoEdge source for interfacing with GPIO on the Multitech Conduit device.",
    license="Apache 2.0",
    keywords="murano exosite iot iiot client gateway mtcdt multitech conduit gpio",
    url="https://github.com/exosite/lib_exoedge_mtcdt_gpio_python",
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    long_description=README,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Operating System :: POSIX :: Linux",
        "Topic :: System :: Operating System Kernels :: Linux",
        "Topic :: Software Development :: Embedded Systems",
        "License :: OSI Approved :: Apache Software License",
    ],
)
