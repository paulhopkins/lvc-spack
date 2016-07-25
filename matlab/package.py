from spack import *

class Matlab(Package):
    """Description"""

    homepage = "http://www.example.com"
    url      = "http://www.example.com/matlab-1.0.tar.gz"

    version('R2015b')#, '0123456789abcdef0123456789abcdef')

    def install(self, spec, prefix):
        configure("--prefix=%s" % prefix)
        make()
        make("install")
