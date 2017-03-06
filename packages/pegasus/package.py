from spack import *
from distutils.dir_util import copy_tree

class Pegasus(Package):
    """Description"""

    homepage = "http://www.example.com"
    url      = "http://download.pegasus.isi.edu/pegasus/4.7.2/pegasus-binary-4.7.2-x86_64_rhel_6.tar.gz"

    version('4.7.4', '4cd87387591136000f5082a066ae04cf',
            url="https://download.pegasus.isi.edu/pegasus/4.7.4/pegasus-binary-4.7.4-x86_64_rhel_6.tar.gz")
    version('4.7.3', '3fd9a53877f4eaf1b0215c2e9c592847',
            url="http://download.pegasus.isi.edu/pegasus/4.7.3/pegasus-binary-4.7.3-x86_64_rhel_6.tar.gz")
    version('4.7.2', '16975804429d3cab23b05287acaeadb4',
            url="http://download.pegasus.isi.edu/pegasus/4.7.2/pegasus-binary-4.7.2-x86_64_rhel_6.tar.gz")

    def install(self, spec, prefix):
        copy_tree('.', prefix)
