from spack import *
from os.path import dirname

class LscsoftInternal(Package):
    """Description"""

    homepage = "https://wiki.ligo.org/DASWG"
    # Empty archive shared between meta-packages
    url="file://" + join_path(dirname(dirname(dirname(__file__))),
                              'archives', 'empty.tar.gz')
    version("0.1", "fbfe7b4acab1f9c5642388313270a616")

    depends_on("py-dqsegdb", type="run")
    depends_on("py-ligo-lvalert", type="run")
    depends_on("libframe+matlab", type="run")
    depends_on("py-glue", type="run")
    depends_on("lscsoft-lalsuite+swig_python+octave", type="run")
    depends_on("ldas-tools+matlab", type="run")
    depends_on("ligotools", type="run")
    depends_on("metaio", type="run")
    depends_on("py-pylal", type="run")
    depends_on("py-pyrxp", type="run")
    depends_on("py-python-voeventlib", type="run")
    depends_on("py-ligo-gracedb", type="run")
    depends_on("nds2-client+octave+python", type="run")
    depends_on("ligo-lars", type="run")
    depends_on("gds+core+crtools+monitors+pygds+services", type="run")

    # Do not install anything and do not check if anything was installed
    def install(self, spec, prefix):
        pass
    def sanity_check_prefix(self):
        pass
