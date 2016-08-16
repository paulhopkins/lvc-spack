from spack import *
from os.path import dirname

class LscsoftAll(Package):
    """Description"""

    homepage = "https://wiki.ligo.org/DASWG"
    # Empty archive shared between meta-packages
    url="file://" + join_path(dirname(dirname(dirname(__file__))),
                              'archives', 'empty.tar.gz')
    version("0.1", "fbfe7b4acab1f9c5642388313270a616")

    depends_on("lscsoft-internal")
    depends_on("lscsoft-external")

    variant("version", "spack", "Version of packages to use")

    depends_on("ncurses@5.9", when="version=sl7")
    depends_on("openssl@1.0.1t", when="version=sl7")
    depends_on("zlib@1.2.7", when="version=sl7")
    depends_on("fftw@3.3.4", when="version=sl7")
    depends_on("gsl@1.15", when="version=sl7")
    depends_on("lal+hdf5", when="version=sl7")
    depends_on("hdf5@1.8.12", when="version=sl7")
    depends_on("octave@3.8.2", when="version=sl7")
    depends_on("pcre@8.32", when="version=sl7")
    depends_on("pkg-config@0.27.1", when="version=sl7")
    depends_on("readline@6.2", when="version=sl7")
    depends_on("py-numpy@1.7.1", when="version=sl7")
    depends_on("py-nose@1.3.0", when="version=sl7")
    depends_on("py-setuptools@19.2", when="version=sl7")
    depends_on("python@2.7.5+ucs4", when="version=sl7")
    depends_on("bzip2@1.0.6", when="version=sl7")
    depends_on("sqlite@3.7.17", when="version=sl7")
    depends_on("swig@3.0.7", when="version=sl7")
    depends_on("chealpix@3.30.0", when="version=sl7")
    depends_on("cfitsio@3.370", when="version=sl7")
    depends_on("xz@5.2.0", when="version=sl7")
    depends_on("py-healpy@1.9.1", when="version=sl7")
    depends_on("glib@2.42.2", when="version=sl7")
    depends_on("gettext@0.18.2+tar", when="version=sl7")
    depends_on("tar@1.26", when="version=sl7")
    depends_on("libffi@3.0.13", when="version=sl7")
    depends_on("py-m2crypto", when="version=sl7")
    depends_on("py-pyrxp@1.13", when="version=sl7")
    depends_on("py-cjson@1.1.0", when="version=sl7")
    depends_on("libjson-c@0.11", when="version=sl7")
    depends_on("py-h5py@2.3.1", when="version=sl7")
    depends_on("py-astropy@1.1.1", when="version=sl7")

    # Do not install anything and do not check if anything was installed
    def install(self, spec, prefix):
        pass
    def sanity_check_prefix(self):
        pass
