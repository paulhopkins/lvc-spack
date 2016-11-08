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
from spack import *
from spack.environment import *

class Lalinspiral(Package):
    """LSC Algorithm Library - Inspiral
    LIGO Scientific Collaboration Algorithm Library - Inspiral, containing
    routines for compact binary gravitational wave data analysis.
    """

    homepage = "https://wiki.ligo.org/DASWG/LALSuite"
    url      = "http://software.ligo.org/lscsoft/source/lalsuite/lalinspiral-1.7.4.tar.xz"

    version('1.7.6', '1df70e801f3f6913df631a144aa7fb84')
    version('1.7.5', '8b511e396038881deeb09880cb51cfab')
    version('1.7.4', '8f5488c5b05347b203e19a5df226cef2')

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


    depends_on('lalframe')
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
        run_env.set('LALINSPIRAL_PREFIX', self.spec.prefix)
        run_env.set("LALINSPIRAL_DATADIR",
                    join_path(self.prefix.share, 'lalinspiral'))
        # Use normal user-env script if it exists.
        #source_file = join_path(self.prefix.etc, 'lalinspiral-user-env.sh')
        #if can_access(source_file):
        #    source_file_env = EnvironmentModifications.from_sourcing_files(source_file)
        #    run_env.extend(source_file_env)
