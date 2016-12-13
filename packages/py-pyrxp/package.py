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
#     spack install py-pyRXP
#
# You can edit this file again by typing:
#
#     spack edit py-pyRXP
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *

class PyPyrxp(Package):
    """FIXME: put a proper description of your package here."""
    # FIXME: add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "http://software.ligo.org/lscsoft/source/pyRXP-1.13.tar.gz"

    version('2.1.0', '945b6586a0bc16e1735bca1244e824c6',
            url='https://pypi.python.org/packages/5b/56/d7d6841b0fc0e4461946a8368d7d5cc4314bae3bed177ca9aadd0538918c/pyRXP-2.1.0.tar.gz#md5=945b6586a0bc16e1735bca1244e824c6')
    version('1.13', '87a1b0bf163ccc7fd1ddbcdb89731c19')

    # FIXME: Add dependencies if this package requires them.
    extends("python")

    def install(self, spec, prefix):
        # FIXME: Modify the configure line to suit your build system here.
        python('setup.py', 'install', '--prefix=%s' % prefix)
