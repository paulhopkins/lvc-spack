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

class Lalsimulation(Package):
    """LSC Algorithm Library - Simulation
    LIGO Scientific Collaboration Algorithm Library - Simulation containing
    routines for simulation gravitational-wave waveforms and noise sources.
    """
    homepage = "https://wiki.ligo.org/DASWG/LALSuite"
    url      = "http://software.ligo.org/lscsoft/source/lalsuite/lalsimulation-1.5.0.tar.xz"

    version('1.7.2', '34c9066e763751aa61e4ff13dfd401d4')
    version('1.7.1', 'f2afbe88ba68ad3d0bebe4df90ef03ea')
    version('1.7.0', '2adaa6dd93baea8d6207c1125f5b1b12')
    version('1.6.1', 'a6f19a9912bf08ea76004bcea1fd2712')
    version('1.6.0', '6a853a7db72c4327df49a24a4cc0fca3')
    version('1.5.0', '13c05ae1c07512f598f815c75a2279e7')

    variant('swig_python', True, 'Generate SWIG bindings for Python')
    variant('octave', False, 'Generate SWIG bindings for Octave')
    variant('openmp', True, 'Enable OpenMP')
    variant('fastgsl', False, 'Enable fast/inline GSL code')

    extends('python')

    depends_on("gsl")
    depends_on("lal")
    depends_on('swig', when='+swig_python')
    depends_on('swig', when='+octave')
    depends_on("octave", when="+octave")

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

        if '+openmp' in spec:
            config_args.append('--enable-openmp')
        else:
            config_args.append('--disable-openmp')

        if '+fastgsl' in spec:
            config_args.append('--enable-fast-gsl')
        else:
            config_args.append('--disable-fast-gsl')

        configure(*config_args)

        make()
        make("install")

    def setup_environment(self, spack_env, run_env):
        run_env.set('LALSIMULATION_PREFIX', self.spec.prefix)
        run_env.set("LALSIMULATION_DATADIR",
                    join_path(self.prefix.share, 'lalsimulation'))
        #source_file = join_path(self.prefix.etc, 'lalsimulation-user-env.sh')
        #if can_access(source_file):
        #    source_file_env = EnvironmentModifications.from_sourcing_files(source_file)
        #    run_env.extend(source_file_env)
