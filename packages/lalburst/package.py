from spack import *
from spack.environment import *

class Lalburst(Package):
    """LSC Algorithm Library - Burst
    LIGO Scientific Collaboration Algorithm Library - Burst, containing
    routines for burst gravitational wave data analysis.
    """

    homepage = "https://www.lsc-group.phys.uwm.edu/daswg/projects/lalsuite.html"
    url      = "http://software.ligo.org/lscsoft/source/lalsuite/lalburst-1.4.1.tar.xz"

    version('1.4.3', '2d2d97115a3be8b27d7d1ff9119b4dc5')
    version('1.4.2', '6fac2dfc6c9d1d301cf58c8a47763a71')
    version('1.4.1', '2b0f81cce1aea92883f8b8337d330d48')

    variant('swig_python', True, 'Generate SWIG bindings for Python')
    variant('octave', False, 'Generate SWIG bindings for Octave')
    variant('fastgsl', False, 'Enable fast/inline GSL code')

    extends("python")

    depends_on("gsl")
    depends_on("metaio")

    depends_on('swig', when='+swig_python')
    depends_on('swig', when='+octave')
    depends_on('py-numpy', when='+swig_python')
    depends_on('octave+fftw', when='+octave')

    depends_on('lalmetaio')
    depends_on('lal')
    depends_on('lalsimulation')
    
    def install(self, spec, prefix):
        config_args = ['--prefix=%s' % prefix]

        if '+swig_python' in spec:
            config_args.append('--enable-swig-python')
        else:
            config_args.append('--disable-swig-python')

        if '+octave' in spec:
            config_args.append('--enable-swig-octave')
        else:
            config_args.append('--disable-swig-octave')

        if '+fastgsl' in spec:
            config_args.append('--enable-fast-gsl')
        else:
            config_args.append('--disable-fast-gsl')

        configure(*config_args)

        make()
        make("install")

    def setup_environment(self, spack_env, run_env):
        run_env.set('LALBURST_PREFIX', self.spec.prefix)
        run_env.set("LALBURST_DATADIR",
                    join_path(self.prefix.share, 'lalburst'))
#        # Use normal user-env script if it exists.
#        source_file = join_path(self.prefix.etc, 'lalburst-user-env.sh')
#        if can_access(source_file):
#            source_file_env = EnvironmentModifications.from_sourcing_files(source_file)
#            run_env.extend(source_file_env)
