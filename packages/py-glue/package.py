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


class PyGlue(Package):
    """Grid LSC User Environment
    Glue is a suite of python modules and programs to allow users to run
    LSC codes on the grid.
    """

    homepage = "https://www.lsc-group.phys.uwm.edu/daswg/projects/glue.html"
    url      = "http://software.ligo.org/lscsoft/source/glue-1.50.0.tar.gz"

    version('1.50.0', 'eb7fe8d752db22522b494c47d5fbfe86')
    version('1.49.1', '616379d11a6de99da5181afee80b29b1')
    version('1.49'  , '245c7d0897cfde9f78b9e431dc888f93')
    version('1.48'  , '4106931086debed39dd617921f2a0c3a')
    version('1.47.1', '7bba9cd4b0ee399f0e771ba4f60be222')

    extends('python')
    depends_on('py-numpy', type=nolink)
    depends_on('py-pyrxp', type=nolink)
    depends_on('py-m2crypto', type=nolink)
    depends_on('py-numpy', type=nolink)

    def install(self, spec, prefix):
        python('setup.py', 'install', '--prefix={0}'.format(prefix))
