from spack import *
from itertools import product

class LscsoftLalsuite(Package):
    """LSC Algorithm Library Applications.
    LALApps is a set of codes for gravitational wave data analysis,
    against the LSC Algorithm Library.
    """

    homepage = "https://wiki.ligo.org/DASWG/LALSuite"
    url      = "1"

    version("1")

    variant('swig_python', True, 'Generate SWIG bindings for Python')
    variant('octave', False, 'Generate SWIG bindings for Octave')
    variant('openmp', True, 'Enable OpenMP')
    variant('fastgsl', False, 'Enable fast/inline GSL code')
    variant('mpi', False, 'Enable MPI')
    variant('extra', True, 'Include lalsuite-extra')

    extends("python")

    depends_on("fftw+float+long_double")
    depends_on("gsl")
    depends_on("py-healpy")

    depends_on("libframe")
    depends_on("metaio")

    depends_on('lalsuite-extra', when='+extra')

    depends_on("mpi", when="+mpi")

    def all_combinations(*names):
        combs = []
        for name in names:
            combs.extend(['+' + name, '~' + name])
        return [('', None)] + zip(combs, combs)

    for c,d in all_combinations('swig_python', 'octave'):
        depends_on('lalstochastic' + c, when=d)
        depends_on('lalframe' + c, when=d)
        depends_on('lalmetaio' + c, when=d)
   
    for c,d in all_combinations('swig_python', 'octave', 'fastgsl'):
        depends_on('lal' + c, when=d)
        depends_on('lalinspiral' + c, when=d)
        depends_on('laldetchar' + c, when=d)
        depends_on('lalburst' + c, when=d)
        depends_on('lalxml' + c, when=d)
        
    for c,d in all_combinations('swig_python', 'octave', 'fastgsl', 'openmp'):
        depends_on('lalsimulation' + c, when=d)
        depends_on('lalpulsar' + c, when=d)
        depends_on('lalinference' + c, when=d)

    for c,d in all_combinations('fastgsl', 'openmp', 'mpi'):
        depends_on('lalapps' + c, when=d)

    def install(self, spec, prefix):
        pass
    def do_fetch(self):
        pass
    def do_stage(self):
        pass
