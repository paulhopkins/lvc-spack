from spack import *
from spack.environment import *
from itertools import product

class Laldetchar(Package):
    """LSC Algorithm Library - DetChar
    LIGO Scientific Collaboration Algorithm Library - DetChar, containing \
    routines for detectory characterisation.
    """

    homepage = "https://www.lsc-group.phys.uwm.edu/daswg/projects/lalsuite.html"
    url      = "http://software.ligo.org/lscsoft/source/lalsuite/laldetchar-0.3.2.tar.xz"

    version('0.3.2', '0c52036d4bf65830e8006e85b12305a2')
    version('0.3.3', '8c213d90d44b709a23faa0af94acc6b9')

    variant('swig_python', True, 'Generate SWIG bindings for Python')
    variant('octave', False, 'Generate SWIG bindings for Octave')
    variant('fastgsl', False, 'Enable fast/inline GSL code')

    extends("python")

    depends_on("gsl")
    depends_on("metaio")
    depends_on("libframe")

    depends_on('swig', when='+swig_python')
    depends_on('swig', when='+octave')
    depends_on('py-numpy', when='+swig_python')
    depends_on('octave+fftw', when='+octave')

    depends_on('lalmetaio')
    depends_on('lal')
    depends_on('lalsimulation')
    depends_on('lalburst')

    
#    for c in all_combinations('swig_python', 'octave'):
#        depends_on('lalmetaio' + c, when=c)
#
#    for c in all_combinations('swig_python', 'octave', 'fastgsl'):
#        depends_on('lal' + c, when=c)
#        depends_on('lalsimulation' + c, when=c)
#        depends_on('lalburst' + c, when=c)

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
        run_env.set('LALDETCHAR_PREFIX', self.spec.prefix)
        run_env.set("LALDETCHAR_DATADIR",
                    join_path(self.prefix.share, 'laldetchar'))

        # This step is required to overcome a restriction in 
        # "EnvironmentModifications.from_sourcing_files" that does not properly
        # handle paths which have no initial value.
        if '+octave' in self.spec:
            source_file_env = EnvironmentModifications.from_sourcing_files(
                join_path(self.prefix.etc,'laldetchar-user-env.sh'))
            modifications = source_file_env.group_by_name()
            octave_path = modifications['OCTAVE_PATH'][0].value.split(':',1)[0]
            run_env.append_path("OCTAVE_PATH", octave_path)
                           
