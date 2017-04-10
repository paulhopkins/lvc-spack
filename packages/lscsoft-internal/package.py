from spack import *
from os.path import dirname

class LscsoftInternal(Package):
    """Description"""

    homepage = "https://wiki.ligo.org/DASWG"
    # Empty archive shared between meta-packages
    url="file://" + join_path(dirname(dirname(dirname(__file__))),
                              'archives', 'empty.tar.gz')
    version("0.2", "fbfe7b4acab1f9c5642388313270a616")

    variant('pycbc', False, "Add PyCBC and use PyCBC forks where necessary")

    depends_on("py-ligo-lvalert", type=('build', 'run'))
    depends_on("py-ligo-lvalert-heartbeat", type=('build', 'run'))
    depends_on("libframe")
    depends_on("lscsoft-lalsuite")
    depends_on("py-ligo-common")
    #depends_on("ldas-tools+matlab")
    depends_on("ligotools")
    depends_on("metaio")
    depends_on("py-pylal")
    depends_on("py-pyrxp")
    depends_on("py-python-voeventlib")
    depends_on("py-ligo-gracedb")
    #depends_on("lscsoft-gstlal")
    #depends_on("nds2-client+doc+octave+python")
    #depends_on("ligo-lars")
    #depends_on("gds+core+crtools+monitors+pygds+services")

    depends_on("py-dqsegdb", type=('build', 'run'), when='~pycbc')
    depends_on("py-glue", type=('build', 'run'), when='~pycbc')

    depends_on("py-pycbc-dqsegdb", type=('build', 'run'), when='+pycbc')
    depends_on("py-pycbc-glue", type=('build', 'run'), when='+pycbc')
    depends_on("py-pycbc", type=('build', 'run'), when='+pycbc')

    # Do not install anything and do not check if anything was installed
    def install(self, spec, prefix):
        with open(join_path(spec.prefix, 'dummy.txt'), 'w') as out:
            out.write('This is a bundle\n')
