from spack import *

class LscsoftInternal(Package):
    """Description"""

    homepage = "https://wiki.ligo.org/DASWG/LALSuite"
    url      = "1"

    version("1")

    depends_on("py-dqsegdb")
    depends_on("py-ligo-lvalert")
    depends_on("libframe+matlab")
    depends_on("py-glue")
    depends_on("lscsoft-lalsuite+swig_python+octave")
    depends_on("ldas-tools+matlab")
    depends_on("ligotools")
    depends_on("metaio")
    depends_on("py-pylal")
    depends_on("py-pyrxp")
    depends_on("py-python-voeventlib")
    depends_on("py-ligo-gracedb")
    #depends_on("nds2-client+doc+octave+python")
    #depends_on("ligo-lars")
    #depends_on("gds+core+crtools+monitors+pygds+services")
    
    def install(self, spec, prefix):
        pass
    def do_fetch(self):
        pass
    def do_stage(self):
        pass
