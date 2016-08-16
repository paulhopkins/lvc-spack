from spack import *

class LigoProxyUtils(Package):
    """Utilities for obtaining short-lived proxy certificates for LIGO"""

    homepage = "https://wiki.ligo.org/AuthProject"
    url      = "http://software.ligo.org/lscsoft/source/ligo-proxy-utils-1.3.0.tar.gz"

    version('1.3.0', 'b20c2e59ea9b05ce7b1c8d65e3453cdc')
    version('1.2.5', '401a7829b52499dfb2d07a8f1813f6a0')

    variant('bash', False, "Explicitly depend on BASH package")
    variant('krb5', False, "Explicitly depend on krb5 package")
    variant('globus', False, "Explicitly depend on globus-toolkit")
    variant('certs', False, "Explicitly depend on IGTF certs")

    depends_on('bash', when="+bash", type='run')
    depends_on('krb5', when="+krb5", type='run')
    depends_on('globus-toolkit', when="+globus", type='run')
    depends_on('igtf-certs', when="+certs", type="run")

    depends_on('curl', type="run")
    depends_on('libxslt', type="run")
    depends_on('openssl', type="run")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install('ligo-proxy-init', prefix.bin)
