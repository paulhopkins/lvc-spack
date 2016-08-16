from spack import *


class EcpCookieInit(Package):
    """Utility for obtaining short-lived cookies for accessing Shibbolized SPs from command-line tools (e.g., curl or git)"""

    homepage = "https://wiki.ligo.org/AuthProject"
    url      = "http://software.ligo.org/lscsoft/source/ecp-cookie-init-1.3.5.tar.gz"

    version('1.3.5', '563254e0813cc41407664d6223f33ecb')
    version('1.3.4', '73ce8fd85a02d376e3f80da58506e9ba')

    variant('bash', False, "Explicitly depend on BASH package")
    variant('krb5', False, "Explicitly depend on krb5 package")
    variant('certs', False, "Explicitly depend on IGTF certs")

    depends_on('bash', when="+bash", type='run')
    depends_on('krb5', when="+krb5", type='run')
    depends_on('globus-toolkit', when="+globus", type='run')
    depends_on('igtf-certs', when="+certs", type="run")

    depends_on('curl', type="run")
    depends_on('libxslt', type="run")
    depends_on('python', type="run")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install('ecp-cookie-init', prefix.bin)
