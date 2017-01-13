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


class PyLigoGracedb(Package):
    """Gravitational-wave Candidate Event Database
    A prototype system to organize candidate events from
    gravitational-wave searches and to provide an environment to record
    information about follow-ups. This package provides a simple client
    tool to submit candidate events to the database.
    """

    homepage = "https://www.lsc-group.phys.uwm.edu/daswg/projects/gracedb.html"
    url      = "http://software.ligo.org/lscsoft/source/ligo-gracedb-1.20.tar.gz"

    version('1.22', '60c43dfc97a45a61a799303a7edd30b3')
    version('1.21', 'd7ef86d1377290ccddb77b0f5b801a70')
    version('1.20'  , '49081f9251571389998cff70b4fed4cd')
    version('1.19.1', '10dce70ced8cc988104463edead8dca3')
    version('1.19'  , 'f87152c405630af70ee71027cc3e9b1f')
    version('1.18'  , '0cb23f5bc5914a5a7f8c8d5d8ddbfb02')
    version('1.17'  , '65736f22a2f8358ee414630ad8694058')

    extends('python')
    depends_on('py-m2crypto', type=nolink)
    depends_on('py-cjson', type=nolink)
    depends_on('py-setuptools', type='build')
    depends_on('py-ligo-common', type=nolink)

    def install(self, spec, prefix):
        python('setup.py',
               'install',
               '--prefix={0}'.format(prefix),
               '--single-version-externally-managed',
               '--record', 'INSTALLED_FILES')
