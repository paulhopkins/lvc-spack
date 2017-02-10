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
#     spack install py-seaborn
#
# You can edit this file again by typing:
#
#     spack edit py-seaborn
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class PySeaborn(Package):
    """Seaborn is a Python visualization library based on matplotlib.
    It provides a high-level interface for drawing attractive
    statistical graphics."""

    homepage = "http://seaborn.pydata.org/"
    url      = "https://github.com/mwaskom/seaborn/archive/v0.7.1.tar.gz"

    version('0.7.1', 'f66200e3dbf0ebdd9bbdeba73303c974')
    version('0.7.0', '06aae51a8a51d015bba4bc2620599760')
    version('0.6.0', '6a3fac888983f2825f54ad749ae636fc')
    version('0.5.1', '3c5293b4409310678e175f7ebe3e2906')
    version('0.5.0', '855be4bd22fc622796bd59b488449eb0')
    version('0.4.0', 'f17791e53acf21948fccfa48e3f2cb31')

    extends('python')
    depends_on('py-setuptools',  type='build')
    depends_on('py-numpy',       type=('build', 'run'))
    depends_on('py-scipy',       type=('build', 'run'))
    depends_on('py-matplotlib',  type=('build', 'run'))
    depends_on('py-pandas',      type=('build', 'run'))
    #TODO: Recommended dependency
    #variant("statsmodels", True, "Add dependency on statsmodels")
    #depends_on('py-statsmodels', type=('build', 'run'))

    def install(self, spec, prefix):
        setup_py('install', '--prefix={0}'.format(prefix))
