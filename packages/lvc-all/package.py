from spack import *
from os.path import dirname

class LvcAll(Package):
    """Description"""

    homepage = "http://www.example.com"
    # Empty archive shared between meta-packages
    url="file://" + join_path(dirname(dirname(dirname(__file__))),
                              'archives', 'empty.tar.gz')
    version("0.1", "fbfe7b4acab1f9c5642388313270a616")

    variant("version", "spack", "Version of packages to use")

    depends_on('lscsoft-all')
    depends_on('lscsoft-all version=sl7', when="version=sl7")

    depends_on('ldg-client')

    # Do not install anything and do not check if anything was installed
    def install(self, spec, prefix):
        pass
    def sanity_check_prefix(self):
        pass
