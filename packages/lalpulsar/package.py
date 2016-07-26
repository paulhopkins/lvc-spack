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
#     spack install lalpulsar
#
# You can edit this file again by typing:
#
#     spack edit lalpulsar
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *
from spack.environment import *

class Lalpulsar(Package):
    """LSC Algorithm Library - Pulsar
    LIGO Scientific Collaboration Algorithm Library - Pulsar containing
    routines for continuous gravitatin wave gravitational data analysis.
    """

    homepage = "https://www.lsc-group.phys.uwm.edu/daswg/projects/lalsuite.html"
    url      = "http://software.ligo.org/lscsoft/source/lalsuite/lalpulsar-1.13.0.tar.xz"

    version('1.13.0', '3b6c9116d03f7b6747627e16a790b39e')
    version('1.14.0', '701d536ad947a471d7eb71fa8211598d')

    variant('swig_python', True, 'Generate SWIG bindings for Python')
    variant('octave', False, 'Generate SWIG bindings for Octave')
    variant('openmp', True, 'Enable OpenMP')
    variant('fastgsl', False, 'Enable fast/inline GSL code')

    extends("python")
    depends_on("gsl")
    depends_on("libxml2")
    depends_on("lalxml")

    depends_on('lal')
#    for p in ['+swig_python', '~swig_python']:
#        for o in ['+octave', '~octave']:
#            for f in ['+fastgsl', '~fastgsl']:
#                depends_on('lal' + p + o + f, when=p + o + f)

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
        run_env.set('LALPULSAR_PREFIX', self.spec.prefix)
        run_env.set("LALPULSAR_DATADIR",
                    join_path(self.prefix.share, 'lalpulsar'))

        # This step is required to overcome a restriction in 
        # "EnvironmentModifications.from_sourcing_files" that does not properly
        # handle paths which have no initial value.
        if '+octave' in self.spec:
            source_file_env = EnvironmentModifications.from_sourcing_files(
                join_path(self.prefix.etc,'lalpulsar-user-env.sh'))
            modifications = source_file_env.group_by_name()
            octave_path = modifications['OCTAVE_PATH'][0].value.split(':',1)[0]
            run_env.append_path("OCTAVE_PATH", octave_path)
