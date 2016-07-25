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
#     spack install pegasus-source
#
# You can edit this file again by typing:
#
#     spack edit pegasus-source
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *

class PegasusSource(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "http://download.pegasus.isi.edu/pegasus/4.6.1/pegasus-source-4.6.1.tar.gz"

    version('4.6.1', '78a8e59257925382a461b4f7e03cc05b')

    # FIXME: Add additional dependencies if required.
#    depends_on('* Linux or Mac OS X (not Windows)
#* Ant v1.6 or later
#* Java v1.5 or later
#* Python 2.4 or later (not Python 3 or later)
#* Perl 5 or so
#* A C compiler (gcc or clang)
#* A C++ compiler (gcc or clang)
#* Make
#* Typical UNIX tools such as tar and sed
#
#

    def install(self, spec, prefix):
#        "ant dist"
        make()
        make('install')
