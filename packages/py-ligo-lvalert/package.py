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


class PyLigoLvalert(Package):
    """The LIGO-Virgo Alert System
    A prototype notification service built on the xmpp (jabber) protocol
    and the pubsub extension. It provides a basic notification tool
    which allows multiple producers and consumers of notifications.
    """

    homepage = "https://www.lsc-group.phys.uwm.edu/daswg/projects/lvalert.html"
    url      = "http://software.ligo.org/lscsoft/source/ligo-lvalert-1.3.tar.gz"

    version('1.4.1', '9141a410f6323df4fd8ed9d13d19910c')
    version('1.4'  , '91a3fc81f1a55605d5ace16bb282d018')
    version('1.3.1', '21ef876c11c9be06e3b6b0e8258a4d5a')
    version('1.3'  , '284ede73e728fe626b922ab1094802f9')
    version('1.2'  , '2a4fe591fa1f0a357fb7ee80f2e682b9')
    version('1.1'  , '89e043c2ed7b23cf96231e96ba104996')
    version('1.0'  , '179776a3576efa70e339a71da107252a')

    extends('python')
    depends_on('py-pyxmpp')
    #depends_on('py-libxml2')
    #depends_on('py-m2crypto')
    #depends_on('py-dnspython')

    def install(self, spec, prefix):
        python('setup.py', 'install', '--prefix={0}'.format(prefix))
