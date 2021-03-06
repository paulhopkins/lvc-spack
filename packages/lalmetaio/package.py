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

class Lalmetaio(Package):
    """LSC Algorithm Library - MetaIO
    LIGO Scientific Collaboration Algorithm Library - MetaIO containing
    routines for reading/writing LIGO_LW XML files.
    """

    homepage = "https://www.lsc-group.phys.uwm.edu/daswg/projects/lalsuite.html"
    url      = "http://software.ligo.org/lscsoft/source/lalsuite/lalmetaio-1.2.7.tar.xz"

    version('1.3.1', '5222898eebfc05dbddeba2d63c64d336')
    version('1.3.0', '5b8074b34fa084a23db37f1575aafdf5')
    version('1.2.8', '90f65f3ddfdbf08525ff6ab400588226')
    version('1.2.7', '8d13f353cc131bad73d5d5c28a01d38e')

    variant('swig_python', True, 'Generate SWIG bindings for Python')
    variant('octave', False, 'Generate SWIG bindings for Octave')

    extends("python")
    depends_on("metaio")
    depends_on('lal')
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

        configure(*config_args)

        make()
        make("install")

    def setup_environment(self, spack_env, run_env):
        run_env.set('LALMETAIO_PREFIX', self.spec.prefix)
        run_env.set("LALMETAIO_DATADIR",
                    join_path(self.prefix.share, 'lalmetaio'))

        ## Use normal user-env script if it exists.
        #source_file = join_path(self.prefix.etc, 'lalmetaio-user-env.sh')
        #if can_access(source_file):
        #    source_file_env = EnvironmentModifications.from_sourcing_files(source_file)
        #    run_env.extend(source_file_env)
