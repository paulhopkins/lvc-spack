from spack import *

class PyPyxmpp(Package):
    """FIXME: put a proper description of your package here."""
    # FIXME: add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://pypi.python.org/packages/source/p/pyxmpp/pyxmpp-1.1.2.tar.gz"

    version('1.1.2', 'a38abf032aca0408b6055cd94296eb75')
    # FIXME: Add dependencies if this package requires them.

    extends("python")
    depends_on("libxml2+python")
    depends_on("py-dnspython")

    def install(self, spec, prefix):
        # FIXME: Modify the configure line to suit your build system here.
        python('setup.py', 'install', '--prefix=%s' % prefix)
