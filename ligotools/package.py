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
#     spack install ligotools
#
# You can edit this file again by typing:
#
#     spack edit ligotools
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Ligotools(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "http://software.ligo.org/lscsoft/source/ligotools-1.1.0.tar.gz"

    version('1.1.0', '57ec7134faf031ce84e409856150c00c')
    version('1.0.4', 'ad147cd4240a280465728883692903a1')
    version('1.0.3', '6f09863c07bfc35eb7288e35865853aa')
    version('1.0.2', 'a5665a267cd10048ea8c15b608b6b072')
    version('1.0.1', 'a7ba3fef58f41f9ad1e0a721a83b7931')

    variant('matlab', default=True)

    # FIXME: Add additional dependencies if required.
    depends_on('cmake')

    def install(self, spec, prefix):
        with working_dir('spack-build', create=True):
            # FIXME: Modify the cmake line to suit your build system here.
            cmake_args = []
            if '+matlab' in spec:
                cmake_args.append('-DENABLE_BINARY_MATLAB=TRUE')

            cmake('..', *cmake_args + std_cmake_args)

            # FIXME: Add logic to build and install here.
            make()
            make('install')
