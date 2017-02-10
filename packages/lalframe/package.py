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

class Lalframe(Package):
    """LSC Algorithm Library - Frame
    LIGO Scientific Collaboration Algorithm Library - Frame, containing \
    routines for reading and writing frame files.
    """

    homepage = "https://www.lsc-group.phys.uwm.edu/daswg/projects/lalsuite.html"
    url      = "http://software.ligo.org/lscsoft/source/lalsuite/lalframe-1.4.0.tar.xz"

    version('1.4.3', 'f7e471322ac062c0bc9ffd3179b770fb')
    version('1.4.2', '91494d8783ee6b4b5725d0a8e866856a')
    version('1.4.1', 'e11a791b728176eb0f677419a004fe46')
    version('1.4.0', '087163c020b4da459fa7c5e1dca1aac8')

    variant('swig_python', True, 'Generate SWIG bindings for Python')
    variant('octave', False, 'Generate SWIG bindings for Octave')

    extends('python')

    depends_on("lal")
    #depends_on("ldas-tools")
    depends_on("libframe")

    depends_on('swig', when='+swig_python')
    depends_on('swig', when='+octave')
    depends_on('py-numpy', when='+swig_python')
    depends_on('octave+fftw', when='+octave')

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


        configure(*config_args)

        make()
        make("install")

    def setup_environment(self, spack_env, run_env):
        run_env.set('LALFRAME_PREFIX', self.spec.prefix)
        run_env.set("LALFRAME_DATADIR",
                    join_path(self.prefix.share, 'lalframe'))
        ## Use normal user-env script if it exists.
        #source_file = join_path(self.prefix.etc, 'lalframe-user-env.sh')
        #if can_access(source_file):
        #    source_file_env = EnvironmentModifications.from_sourcing_files(source_file)
        #    run_env.extend(source_file_env)
