##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################

#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install lalinference
#
# You can edit this file again by typing:
#
#     spack edit lalinference
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *
from spack.environment import *

class Lalinference(Package):
    """LSC Algorithm Library - Inference
    LIGO Scientific Collaboration Algorithm Library - Inference containing \
    routines for Bayesian inference data analysis.
    """

    homepage = "https://www.lsc-group.phys.uwm.edu/daswg/projects/lalsuite.html"
    url      = "http://software.ligo.org/lscsoft/source/lalsuite/lalinference-1.6.0.tar.xz"

    version('1.6.0', 'e4f68dc673dd9a24730e2e8473c363b3')
    version('1.7.0', '29ebf36a1e989f6a6e2ad2b12050244c')

    variant('swig_python', True, 'Generate SWIG bindings for Python')
    variant('octave', False, 'Generate SWIG bindings for Octave')
    variant('fastgsl', False, 'Enable fast/inline GSL code')
    variant('hdf5', default=True)
    variant('openmp', True, 'Enable OpenMP')

    extends("python")

    depends_on("chealpix")
    depends_on("gsl")
    depends_on("metaio")
    depends_on("libxml2")
    depends_on("py-healpy")

    depends_on('swig', when='+swig_python')
    depends_on('swig', when='+octave')
    depends_on('py-numpy', when='+swig_python')
    depends_on('octave+fftw', when='+octave')

    depends_on('lalframe')
    depends_on('lalmetaio')
    depends_on('lal')
    depends_on('lalinspiral')
    depends_on('lalburst')
    depends_on('lalxml')
    depends_on('lalpulsar')
    depends_on('lalsimulation')

    
#    for p in ['+swig_python', '~swig_python']:
#        for o in ['+octave', '~octave']:
#            depends_on('lalframe' + p + o, when=p + o)
#            depends_on('lalmetaio' + p + o, when=p + o)
#            for f in ['+fastgsl', '~fastgsl']:
#                depends_on('lal' + p + o + f, when=p + o + f)
#                depends_on('lalinspiral' + p + o + f, when=p + o + f)
#                depends_on('lalburst' + p + o + f, when=p + o + f)
#                depends_on('lalxml' + p + o + f, when=p + o + f)
#
#                for m in ['+openmp', '~openmp']:
#                    depends_on('lalpulsar' + p + o + f + m, when=p + o + f + m)
#                    depends_on('lalsimulation' + p + o + f + m, when=p + o + f + m)

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

        if '+hdf5' in spec:
            config_args.append('--with-hdf5=yes')
        else:
            config_args.append('--with-hdf5=no')

        if '+openmp' in spec:
            config_args.append('--enable-openmp')
        else:
            config_args.append('--disable-openmp')

        configure(*config_args)

        make()
        make("install")

    def setup_environment(self, spack_env, run_env):
        run_env.set('LALINFERENCE_PREFIX', self.spec.prefix)
        run_env.set("LALINFERENCE_DATADIR",
                    join_path(self.prefix.share, 'lalinference'))
#        source_file = join_path(self.prefix.etc,'lalinference-user-env.sh')
#        if can_access(source_file):
#            source_file_env = EnvironmentModifications.from_sourcing_files(source_file)
#            run_env.extend(source_file_env)
#
#        run_env.set('LALINFERENCE_PREFIX', self.spec.prefix)
#        run_env.set("LALINFERENCE_DATADIR",
#                    join_path(self.prefix.share, 'lalinference'))
#
#        # This step is required to overcome a restriction in 
#        # "EnvironmentModifications.from_sourcing_files" that does not properly
#        # handle paths which have no initial value.
#        if '+octave' in self.spec:
#            source_file_env = EnvironmentModifications.from_sourcing_files(
#                join_path(self.prefix.etc,'lalinference-user-env.sh'))
#            modifications = source_file_env.group_by_name()
#            octave_path = modifications['OCTAVE_PATH'][0].value.split(':',1)[0]
#            run_env.append_path("OCTAVE_PATH", octave_path)
                           
