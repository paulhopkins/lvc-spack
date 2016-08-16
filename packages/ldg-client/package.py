from spack import *
from os.path import dirname

class LdgClient(Package):
    """This meta-package will pull in all necessary packages to provide the
    user with a client configuration to access remote (LDG) clusters as well
    as apply for, retrieve, and renew their DoE certificates."""

    homepage = "https://wiki.ligo.org/AuthProject"
    url="file://" + join_path(dirname(dirname(dirname(__file__))),
                              'archives', 'empty.tar.gz')
    version("0.1", "fbfe7b4acab1f9c5642388313270a616")

    depends_on('ligo-proxy-utils')
    depends_on('ecp-cookie-init')

    # Do not install anything and do not check if anything was installed
    def install(self, spec, prefix):
        pass
    def sanity_check_prefix(self):
        pass
