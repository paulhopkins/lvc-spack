from spack import *


class IgtfPolicyInstallationBundle(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "http://dist.eugridpma.info/distribution/igtf/current/igtf-policy-installation-bundle-1.76.tar.gz"

    version('1.76', '8b799a3a15bb84c5a1d1cd62509c646f')

    def install(self, spec, prefix):
        configure('--with-profile=classic',
            '--prefix={0}'.format(prefix))
        make()
        make('install')
