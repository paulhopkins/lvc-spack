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

class Libframe(Package):
    """LIGO/VIRGO Frame Library
    A Common Data Frame Format for Interferometric Gravitational
    Wave Detector has been developed by VIRGO and LIGO. The Frame
    Library is a software dedicated to the frame manipulation
    including file input/output.
    """

    homepage = "http://lappweb.in2p3.fr/virgo/FrameL/"
    url      = "http://lappweb.in2p3.fr/virgo/FrameL/libframe-8.30.tar.gz"

    version('8.30', 'efd7959d70e488b95395fbcde9bcd057')
    version('8.21', '74e2d944f4ed7f50e4e7ce30ae6bb08f')
    version('8.20', '4e95fe3af932b68b4ab1bcd892656dfc')

    #variant('python', default=False)
    #variant('octave', False, 'Generate SWIG bindings for Octave')
    #variant('root', default=False)
    variant('matlab', default=False)

    depends_on('matlab', when='+matlab')

    def install(self, spec, prefix):
        configure('--prefix=%s' % prefix)

        make()
        make("install")

        if '+matlab' in spec:
            with working_dir('matlab'):
                mex = which('mex', required = True)

                for lib in ['frextract.c',
                            'frgetvect.c',
                            'frgetvectN.c',
                            'mkframe.c']:
                    mex(lib,
                        '../src/.libs/libFrame.a',
                        '-I../src',
                        '-outdir', join_path(prefix, 'matlab'))

                    make("install")
