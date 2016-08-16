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
#     spack install gsi-openssh
#
# You can edit this file again by typing:
#
#     spack edit gsi-openssh
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class GsiOpenssh(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/globus/gsi-openssh/archive/V_6_4_P1.tar.gz"

    version('6.4p1', '3fcdc219e8134f7ba0d866f2575a36e0')

    # FIXME: Add dependencies if required.
    depends_on('zlib')
    depends_on('openssl')

    def install(self, spec, prefix):
        aclocal = which('aclocal')
        aclocal()
        autoconf = which('autoconf')
        autoconf()
        autoheader = which('autoheader')
        autoheader()

        configure('--prefix=%s' % prefix)
        make()
        make('install')

    def url_for_version(self, version):
        return "https://github.com/globus/gsi-openssh/archive/V_6_4_P1.tar.gz"
