from spack import *
from itertools import product
from os.path import dirname

class LscsoftLalsuite(Package):
    """LSC Algorithm Library Applications.
    LALApps is a set of codes for gravitational wave data analysis,
    against the LSC Algorithm Library.
    """

    homepage = "https://wiki.ligo.org/DASWG/LALSuite"
    # Empty archive shared between meta-packages
    url="file://" + join_path(dirname(dirname(dirname(__file__))),
                              'archives', 'empty.tar.gz')
    version("0.1", "fbfe7b4acab1f9c5642388313270a616")

    variant('swig_python', True, 'Generate SWIG bindings for Python')
    variant('octave', False, 'Generate SWIG bindings for Octave')
    variant('openmp', True, 'Enable OpenMP')
    variant('fastgsl', False, 'Enable fast/inline GSL code')
    variant('mpi', False, 'Enable MPI')
    variant('extra', True, 'Include lalsuite-extra')

    depends_on('lalsuite-extra', when='+extra', type="run")

    def all_combinations(*names):
        combs = []
        for name in names:
            combs.extend(['+' + name, '~' + name])
        return [('', None)] + zip(combs, combs)

    for c,d in all_combinations('swig_python', 'octave'):
        depends_on('lalstochastic' + c, when=d, type="run")
        depends_on('lalframe' + c, when=d, type="run")
        depends_on('lalmetaio' + c, when=d, type="run")

    for c,d in all_combinations('swig_python', 'octave', 'fastgsl'):
        depends_on('lal' + c, when=d, type="run")
        depends_on('lalinspiral' + c, when=d, type="run")
        depends_on('laldetchar' + c, when=d, type="run")
        depends_on('lalburst' + c, when=d, type="run")
        depends_on('lalxml' + c, when=d, type="run")

    for c,d in all_combinations('swig_python', 'octave', 'fastgsl', 'openmp'):
        depends_on('lalsimulation' + c, when=d, type="run")
        depends_on('lalpulsar' + c, when=d, type="run")
        depends_on('lalinference' + c, when=d, type="run")

    for c,d in all_combinations('fastgsl', 'openmp', 'mpi'):
        depends_on('lalapps' + c, when=d, type="run")

    # Do not install anything and do not check if anything was installed
    def install(self, spec, prefix):
        with open(join_path(spec.prefix, 'dummy.txt'), 'w') as out:
            out.write('This is a bundle\n') 
