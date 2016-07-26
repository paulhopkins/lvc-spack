from spack import *

class Xpipeline(Package):
    """Description"""

    homepage = "http://www.example.com"
    url      = "http://www.example.com/xpipeline-1.0.tar.gz"

    version('svn-head', svn="https://svn.ligo.caltech.edu/svn/xpipeline/branches/light")

    patch('modify_frgetvect_configure_test.diff', level=0)

    depends_on("matlab")
    #depends_on("libframe+matlab")
    depends_on("ligotools+matlab")
    depends_on('fftw+float+long_double')
    depends_on('gsl')
    depends_on('lal')
    depends_on('lalinspiral')
    depends_on('lalsimulation')
    depends_on('py-glue')

    # Not sure if this is causing a problem 
    #parallel = False

    def install(self, spec, prefix):
        pwd = which('pwd')
        pwd()

        _00boot = Executable("./00boot")
        _00boot()

        config_args = ["--with-xtarget=grb",
                       "--with-frgetvectpath=%s" % join_path(spec['ligotools'].prefix.share, 'ligotools', 'matlab'),
                       "--prefix=%s" % prefix]

        configure(*config_args)
        make()
        make("install")
