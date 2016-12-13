from spack import *
from os.path import dirname

class LscsoftExternalPython(Package):
    """Description"""

    homepage = "https://wiki.ligo.org/DASWG"
    # Empty archive shared between meta-packages
    url="file://" + join_path(dirname(dirname(dirname(__file__))),
                              'archives', 'empty.tar.gz')
    version("0.1", "fbfe7b4acab1f9c5642388313270a616")

#    depends_on("GitPython")
    depends_on("py-h5py", type='run')
    depends_on("py-virtualenv", type='run')
    depends_on("py-virtualenvwrapper", type='run')
    depends_on("py-setuptools", type='run')
    depends_on("py-basemap", type='run')
#    depends_on("py-basemap-data-hires")
#    depends_on("py-basemap-examples")
    depends_on("py-numpy", type='run')
    depends_on("py-matplotlib", type='run')
    depends_on("py-scipy", type='run')
    depends_on("py-setuptools", type='run')
    depends_on("py-ipython", type='run')
    depends_on("py-shapely", type='run')
#    depends_on("py-pip")
#    depends_on("py-sqlobject")
#    depends_on("py34")
#    depends_on("py34-crypto")
#    depends_on("py34-devel")
#    depends_on("py34-libs")
#    depends_on("py34-nose")
#    depends_on("py34-numpy")
#    depends_on("py34-numpy-f2py")
#    depends_on("py34-setuptools")
#    depends_on("py34-setuptools_scm")


    # Do not install anything and do not check if anything was installed
    def install(self, spec, prefix):
        with open(join_path(spec.prefix, 'dummy.txt'), 'w') as out:
            out.write('This is a bundle\n')
