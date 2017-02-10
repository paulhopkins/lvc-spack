from spack import *
from distutils.dir_util import copy_tree

class Pegasus(Package):
    """Description"""

    homepage = "http://www.example.com"
    url      = "http://download.pegasus.isi.edu/pegasus/4.7.2/pegasus-binary-4.7.2-x86_64_rhel_6.tar.gz"

    version('4.7.2', '16975804429d3cab23b05287acaeadb4',
            url="http://download.pegasus.isi.edu/pegasus/4.7.2/pegasus-binary-4.7.2-x86_64_rhel_6.tar.gz")

    def install(self, spec, prefix):
        copy_tree('.', prefix)
