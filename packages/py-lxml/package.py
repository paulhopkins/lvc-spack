from spack import *


class PyLxml(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "http://pypi.python.org/packages/source/l/lxml/lxml-3.2.1.tar.gz"

    version('3.2.1', 'd183ccd6bbd5ca139e9db9e9a675787e')

    extends('python')

    def install(self, spec, prefix):
        python('setup.py', 'install', '--prefix={0}'.format(prefix))
