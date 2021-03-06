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
#     spack install py-virtualenvwrapper
#
# You can edit this file again by typing:
#
#     spack edit py-virtualenvwrapper
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class PyVirtualenvwrapper(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://pypi.python.org/packages/2f/76/6d39003e32429604bf1df9128652d90bec6015c62f66358df1f2e73e7fb3/virtualenvwrapper-4.7.1.tar.gz#md5=3789e0998818d9a8a4ec01cfe2a339b2"

    version('4.7.1', '3789e0998818d9a8a4ec01cfe2a339b2')

    extends('python')

    # FIXME: Add additional dependencies if required.
    depends_on('py-setuptools', type='build')
    depends_on('py-stevedore')

    def install(self, spec, prefix):
        # FIXME: Add logic to build and install here.
        setup_py('install', '--prefix={0}'.format(prefix))
