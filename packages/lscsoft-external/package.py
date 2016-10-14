from spack import *
from os.path import dirname

class LscsoftExternal(Package):
    """Description"""

    homepage = "https://wiki.ligo.org/DASWG"
    # Empty archive shared between meta-packages
    url="file://" + join_path(dirname(dirname(dirname(__file__))),
                              'archives', 'empty.tar.gz')
    version("0.1", "fbfe7b4acab1f9c5642388313270a616")

    depends_on("lscsoft-external-python")

    # Do not install anything and do not check if anything was installed
    def install(self, spec, prefix):
        pass
    def sanity_check_prefix(self):
        pass