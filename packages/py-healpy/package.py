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
#     spack install py-healpy
#
# You can edit this file again by typing:
#
#     spack edit py-healpy
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *

class PyHealpy(Package):
    """FIXME: put a proper description of your package here."""
    # FIXME: add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://pypi.python.org/packages/06/94/de69bbb3e2739f3305ad26a7e827d3d896ffda36c7020c26e8bb579fa010/healpy-1.9.1.tar.gz"

    version('1.10.3', '6491777d1bcbd36d356551bf240d3a2f',
            url='https://pypi.python.org/packages/b0/e6/7e5002721095fad75680fe14bc6f8593e8ea853b345dd5dfbb263eb03ed5/healpy-1.10.3.tar.gz')
    version('1.10.1', 'ee8750957a6fdfdafbef54e54788ec9b',
            url='https://pypi.python.org/packages/29/40/ee62140275003699842e859d245655eb32c9f9d3faf1ab5a6dc28c7edbf5/healpy-1.10.1.tar.gz')
    version('1.9.1', '5d1b082dce77e56023329496cecab48d')

    # FIXME: Add dependencies if this package requires them.
    ignore = ["fits2bitmap",  "fitscheck",  "fitsdiff",  "fitsheader",  "fitsinfo",  "samp_hub",  "volint",  "wcslint"]
    extends("python", ignore="|".join("bin/%s$" % s for s in ignore))


    depends_on("chealpix")
    depends_on("cfitsio")

    depends_on("py-setuptools")
    depends_on("py-numpy")
    depends_on("py-astropy")

    def install(self, spec, prefix):
        # FIXME: Modify the configure line to suit your build system here.
        python('setup.py', 'install', '--prefix=%s' % prefix)

