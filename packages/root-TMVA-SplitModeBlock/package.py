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
#     spack install root
#
# You can edit this file again by typing:
#
#     spack edit root
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class RootTmvaSplitmodeblock(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://root.cern.ch/download/root_v6.06.04.source.tar.gz"

    version('6.06.04', '55a2f98dd4cea79c9c4e32407c2d6d17')
    version('5.34.32', '292a0b95063053699b3273bd50515b0a')

    # FIXME: Add additional dependencies if required.
    depends_on('cmake')
    depends_on('libxpm')
    depends_on('python@2.7:')

    patch('tmvasplitmodeblock.patch')

    def install(self, spec, prefix):
        with working_dir('spack-build', create=True):
            # FIXME: Modify the cmake line to suit your build system here.
            cmake('..',
                  '-DCMAKE_CXX_COMPILER={0}'.format(which('g++')),
                  '-DCMAKE_C_COMPILER={0}'.format(which('gcc')),
                  '-DCMAKE_Fortran_COMPILER={0}'.format(which('gfortran')),
                  '-Dcxx11=ON',
                  '-DCMAKE_CXX_FLAGS=-D_GLIBCXX_USE_CXX11_ABI=0',
                  '-Wno-dev',
                  *std_cmake_args)

            # FIXME: Add logic to build and install here.
            make()
            make('install')

    def setup_environment(self, spack_env, run_env):
        run_env.set('ROOTSYS', self.spec.prefix)

    def url_for_version(self, version):
        """Handle ROOT's unusual version string."""
        return "https://root.cern.ch/download/root_v%s.source.tar.gz" % version
