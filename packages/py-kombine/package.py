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


class PyKombine(Package):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://github.com/bfarr/kombine"
    url      = "https://pypi.python.org/packages/73/ee/2b759a011f1da2b5e4e2fe2f7952c830f6bcb3df669d2b9048b166a1c806/kombine-0.8.0.tar.gz#md5=ca14fce10f08c8ab6bac6e541f2889ff"

    version('0.8.0', 'ca14fce10f08c8ab6bac6e541f2889ff')

    depends_on('py-setuptools', type='build')
    depends_on('py-scipy', type=('build', 'run'))
    depends_on('py-numpy', type=('build', 'run'))

    extends('python')
    def install(self, spec, prefix):
        python('setup.py',
               'install',
               '--prefix={0}'.format(prefix),
               '--record=INSTALLED_FILES',
               '--single-version-externally-managed')