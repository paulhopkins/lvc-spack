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

class PyPycbcDqsegdb(Package):
    """Client library for DQSegDB
    This provices the client tools needed to connect to LIGO/Virgo
    DQSEGDB instances.
    """

    homepage = "https://www.lsc-group.phys.uwm.edu/daswg/projects/dqsegdb.html"
    url      = "https://github.com/ligo-cbc/dqsegdb/archive/dqsegdb-release-1-2-2.tar.gz"

    version("develop", git="https://github.com/duncan-brown/dqsegdb.git",
            branch="pypi_release")

    extends('python')
    depends_on('py-setuptools')
    depends_on('py-pycbc-glue')
    depends_on("py-pyrxp@2.1.0:")

    def install(self, spec, prefix):
        python('setup.py', 'install', '--prefix={0}'.format(prefix))
