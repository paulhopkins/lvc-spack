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

class LdasTools(Package):
    """Suite of LDAS tools"""

    homepage = "http://www.ldas-sw.ligo.caltech.edu"
    url      = "http://software.ligo.org/lscsoft/source/ldas-tools-2.4.2.tar.gz"

    version('2.4.2', '946374e36ce98021dd37a7471facf54e')
    version('2.4.1', '81da5227f4d49358dc5d60af4b842d55')
    version('2.4.0', '831d8cba6ece3b9b5456971426e2c02c')
    version('2.3.3', '5cac6f9b5d68048afc0b4cc3798feb45')
    version('2.3.2', '91df75718ba359dbe564efbf5d33ff78')

    variant('python', default=True)
    variant('matlab', default=False)

    depends_on("zlib")
    depends_on("flex")
    depends_on("bzip2")

    depends_on('python',   when='+python')
    depends_on('py-numpy', when='+python')
    depends_on('swig',     when='+python')

    patch('patch-disable-Werror.patch', level=0)

    def install(self, spec, prefix):
        config_args = ['--disable-silent-rules',
                       '--with-optimization=high',
                       '--disable-tcl',
                       '--without-doxygen',
                       '--without-dot',
                       '--disable-latex',
                       '--prefix=%s' % prefix]
        
        if '+python' in spec:
            config_arg.append('--enable-python')
        else:
            config_arg.append('--disable-python')

        configure(*config_args)

        make()
        make("install", parallel = False)
