from spack import *
from os.path import dirname

class LscsoftExternalCbc(Package):
    """Description"""

    homepage = "https://wiki.ligo.org/DASWG"
    # Empty archive shared between meta-packages
    url="file://" + join_path(dirname(dirname(dirname(__file__))),
                              'archives', 'empty.tar.gz')
    version("0.1", "fbfe7b4acab1f9c5642388313270a616")

    depends_on("cfitsio")
    depends_on("chealpix")
    depends_on("fftw")
    depends_on("gsl")
    depends_on("healpix_cxx")
    depends_on("healpy")
    depends_on("numpy")
    depends_on("pegasus")
    depends_on("py-decorator")
    depends_on("py-decoratortools")
    depends_on("py-matplotlib")
    depends_on("py-sqlobject")
    depends_on("py-virtualenv")
    depends_on("scipy")
    depends_on("spr")

    # Do not install anything and do not check if anything was installed
    def install(self, spec, prefix):
        pass
    def sanity_check_prefix(self):
        pass
