from spack import *
from itertools import product

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

    # ----
    depends_on('lal')
    depends_on('lalsimulation')
    depends_on('lalinspiral')
    depends_on('lalburst')
    depends_on('lalxml')
    
    depends_on('lalsimulation')
    depends_on('lalpulsar')
    depends_on('lalinference')

#    def all_combinations(*names):
#        return [''.join(p) for p in product(*[('+'+v, '~'+v) for v in names])]
#    
#    for c in all_combinations('fastgsl'):
#        depends_on('lal' + c, when=c)
#        depends_on('lalsimulation' + c, when=c)
#        depends_on('lalinspiral' + c, when=c)
#        depends_on('lalburst' + c, when=c)
#        depends_on('lalxml' + c, when=c)
#
#    for c in all_combinations('fastgsl', 'openmp'):
#        depends_on('lalsimulation' + c, when=c)
#        depends_on('lalpulsar' + c, when=c)
#        depends_on('lalinference' + c, when=c)

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
        run_env.set("LALAPPS_DATADIR", join_path(self.prefix.share, 'lalapps'))
