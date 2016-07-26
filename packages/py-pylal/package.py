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


class PyPylal(Package):
    """ Python LSC Algorithm Library
    The PyLAL package is best described as the Python LIGO Algorithm
    Library. It was originally a Python wrapping of parts of the LAL
    library, and although it continues to provide that function it has
    acquired a large collection of independent code of its own so that
    it is no longer exclusively a Python interface to LAL. In this
    package you will find convenience code to assist with manipulating
    XML documents using the glue.ligolw I/O library, you will find a
    wrapping to libframe to enable GWF frame-file reading, you will
    find binning and smoothing code, and you will find (partial)
    wrappings of LALs burstsearch, date, inject, tools, and window
    packages. Additionally, you will find most, if not all, of the
    inspiral pipeline's follow-up and summary tools, and several
    burst-related trigger post-production tools.
    """

    homepage = "http://www.example.com"
    url      = "http://software.ligo.org/lscsoft/source/pylal-0.10.0.tar.gz"

    version('0.10.0', '5ea2add74b723db8800f887a06580d50')
    version('0.9.0' , '95ec8621632b1fbd0e713c83f865dda6')
    version('0.8.1' , 'becbed6a5c5efeb8e8ff5404f1d378f8')
    version('0.8.0' , 'e96b8bf6c155a048e142c6bdbd686b69')
    version('0.7.2' , '8f50af69dfab6c03da0d63c8d0857a1d')

    extends('python')
    depends_on('py-numpy')
    depends_on('py-scipy')
    depends_on('py-matplotlib')
    depends_on('py-glue')
    depends_on('lal')
    depends_on('lalframe')
    depends_on('lalmetaio')
    depends_on('lalsimulation')
    depends_on('lalburst')
    depends_on('lalinspiral')

    def install(self, spec, prefix):
        python('setup.py', 'install', '--prefix={0}'.format(prefix))
