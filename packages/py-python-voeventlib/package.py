from spack import *


class PyPythonVoeventlib(Package):
    """Reference implementation and parser for VOEvent2.
    The reference implementation, and parser, for the VOEvent2 XML
    specification [International Virtual Observatory Alliance
    (IVOA)], which is a standardized language used to report
    observations of astronomical events."""

    homepage = "http://lib.skyalert.org/VOEventLib/"
    url      = "http://software.ligo.org/lscsoft/source/python-voeventlib-0.3.tar.gz"

    version('0.3', '1100432a093d4c4c79ba3939517a7130')

    extends('python')
    depends_on('py-lxml')
    
    def install(self, spec, prefix):
        python('setup.py', 'install', '--prefix={0}'.format(prefix))
