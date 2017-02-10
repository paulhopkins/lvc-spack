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


class LalsuiteExtra(Package):
    """LSC Algorithm Library Extra Data
    Extra data files needed to run certain applications that use the
    LALSimulation Library.
    """

    homepage = "https://www.lsc-group.phys.uwm.edu/daswg/projects/lalsuite.html"
    url      = "http://software.ligo.org/lscsoft/source/lalsuite-extra-1.1.0.tar.gz"

    version('develop', svn='https://svn.ligo.caltech.edu/svn/lalsuite-extra/')

    version('1.3.0', '9fa7a8251f81d04b040af98ecaab376c')
    version('1.2.0', '383a73eea86a845dc12dfc0dd8a7651b')
    version('1.1.0', '325ead3b51d62a1bff48053d20ccbf1c')
    version('1.0.0', '2c8f66b90e68e200fdb62913c6fd3f9c')

    def install(self, spec, prefix):
        configure('--prefix={0}'.format(prefix))

        make()
        make('install')

#    @when("@develop")
#    def install(self, spec, prefix):
#        with working_dir("lalsuite-extra"):
#            self.install(spec, prefix)
        
    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('LAL_DATA_PATH',
                             join_path(self.prefix.share, 'lalsimulation'))
