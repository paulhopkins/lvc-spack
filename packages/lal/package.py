from spack import *
from spack.environment import *

class Lal(Package):
    """LSC Algorithm Library.
    LIGO Scientific Collaboration Algorithm Library containing core
    routines for gravitational wave data analysis.
    """

    homepage = "https://wiki.ligo.org/DASWG/LALSuite"
    url      = "http://software.ligo.org/lscsoft/source/lalsuite/lal-6.16.0.tar.xz"

    version('6.18.0', 'a278f190758c4902055a57efa6d406d4')
    version('6.17.0', '6a3e0f261a1e9a24f115537e9b1090b6')
    version('6.16.0', '4d5b2b79f1d7b720e32a7d4672ead0a1')
    version('6.16.1', 'ba9d91ce403f1d12e128ca579a2eb9a5')

    variant('swig_python', True, 'Generate SWIG bindings for Python')
    variant('octave', False, 'Generate SWIG bindings for Octave')
    variant('hdf5', True, 'Include HDF5 support')
    variant('fastgsl', False, 'Enable fast/inline GSL code')
    variant('cuda', False, 'Include CUDA support')

    # Required dependencies
    extends('python')
    depends_on('gsl')
    depends_on('fftw+float+long_double')

    # Optional dependencies
    depends_on('swig', when='+swig_python', type='build')
    depends_on('py-numpy', when='+swig_python', type=('build', 'run'))
    depends_on('swig', when='+octave', type='build')
    depends_on('octave+fftw', when='+octave')
    depends_on('hdf5~mpi', when='+hdf5')
    depends_on('cuda', when='+cuda')

    def install(self, spec, prefix):
        config_args = ['--prefix=%s' % prefix]

        config_args.append('--enable-swig-python' if '+swig_python' else
        					  '--disable-swig-python')

        config_args.append('--enable-swig-octave' if '+octave' in spec else
        					  '--disable-swig-octave')

        config_args.append('--with-hdf5=yes' if '+hdf5' in spec else
        				     '--with-hdf5=no')

        config_args.append('--enable-fast-gsl' if '+fastgsl' in spec else
        				       '--disable-fast-gsl')

        config_args.append('--with-cuda=yes' if '+cuda' in spec else
        				     '--with-cuda=no')

        configure(*config_args)

        make()
        make("install")

    def setup_environment(self, spack_env, run_env):
        run_env.set('LAL_PREFIX', self.spec.prefix)
        run_env.set("LAL_DATADIR",
                    join_path(self.prefix.share, 'lal'))

        #source_file = join_path(self.prefix.etc, 'lal-user-env.sh')
        #if can_access(source_file):
        #    source_file_env = EnvironmentModifications.from_sourcing_files(source_file)
        #    modifications = source_file_env.group_by_name()
        #    if 'OCTAVE_PATH' in modifications:
        #        octave_path = modifications['OCTAVE_PATH'][0].value.split(':',1)[0]
        #        run_env.append_path("OCTAVE_PATH", octave_path)

