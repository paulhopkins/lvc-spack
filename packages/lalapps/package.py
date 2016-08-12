from spack import *
from spack.environment import *

class Lalapps(Package):
    """LSC Algorithm Library Applications
    LALApps is a set of codes for gravitational wave data analysis,
    against the LSC Algorithm Library.
    """

    homepage = "https://wiki.ligo.org/DASWG/LALSuite"
    url      = "http://software.ligo.org/lscsoft/source/lalsuite/lalapps-6.18.0.tar.xz"

    version('6.18.0', 'bfdbc69904da33a969870555b9e5e05e')
    version('6.19.0', '3be60a5f199b48264bf5ea1e35ec7cfb')

    variant('openmp', True, 'Enable OpenMP')
    variant('fastgsl', False, 'Enable fast/inline GSL code')
    variant('mpi', False, 'Enable MPI')

    extends("python")

    depends_on("fftw+float+long_double")
    depends_on("gsl")
    depends_on("py-healpy")

    depends_on("libframe")
    depends_on("metaio")

    depends_on("mpi", when="+mpi")
    
    depends_on("lalstochastic")
    depends_on('lalframe')
    depends_on('lalmetaio')

    depends_on('lal')
    depends_on('lalsimulation')
    depends_on('lalinspiral')
    depends_on('lalburst')
    depends_on('lalxml')
    
    depends_on('lalsimulation')
    depends_on('lalpulsar')
    depends_on('lalinference')

    def install(self, spec, prefix):
        config_args = ['--prefix=%s' % prefix]

        if '+fastgsl' in spec:
            config_args.append('--enable-fast-gsl')
        else:
            config_args.append('--disable-fast-gsl')

        if '+openmp' in spec:
            config_args.append('--enable-openmp')
        else:
            config_args.append('--disable-openmp')

        if '+mpi' in spec:
            config_args.append('--enable-mpi')
        else:
            config_args.append('--disable-mpi')

        configure(*config_args)

        make()
        make("install")

    def setup_environment(self, spack_env, run_env):
        run_env.set('LALAPPS_PREFIX', self.spec.prefix)
        run_env.set("LALAPPS_DATADIR",
                    join_path(self.prefix.share, 'lalapps'))
#        # Use normal user-env script if it exists.
#        source_file = join_path(self.prefix.etc, 'lalapps-user-env.sh')
#        if can_access(source_file):
#            source_file_env = EnvironmentModifications.from_sourcing_files(source_file)
#            run_env.extend(source_file_env)
