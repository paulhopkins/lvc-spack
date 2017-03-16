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

class PyPycbc(PythonPackage):
    """A Python toolkit for analysis of data from gravitational-wave laser
    interferometer detectors with the goal of detecting and studying signals
    from compact binary coalescences (CBCs)."""

    homepage = "https://github.com/ligo-cbc/pycbc"
    url      = "https://github.com/ligo-cbc/pycbc/archive/v1.5.5.tar.gz"

    version('1.6.8', 'ffb1286c62912608a40633edffa79bde')
    version('1.5.5', '58f045c556c87dbe61f47e51aa082a69')
    version('1.5.4', 'fb32cb06069c5e952a5cbc4be4edb63b')
    version('1.5.3', '343ab2bbdc2243d168daec605275afde')

    variant('lalapps', False, 'Add static LALApps binaries')

    depends_on('py-setuptools', type='build')

    depends_on('py-mako@1.0.1:', type=('build', 'run'))
    depends_on('py-decorator@3.4.2:', type=('build', 'run'))
    depends_on('py-scipy@0.13.0:', type=('build', 'run'))
    depends_on('py-unittest2', type=('build', 'run'))
    depends_on('py-matplotlib@1.3.1:', type=('build', 'run'))
    depends_on('py-numpy@1.6.4:', type=('build', 'run'))
    depends_on('py-pillow', type=('build', 'run'))
    depends_on('py-h5py@2.5:', type=('build', 'run'))
    depends_on('py-jinja2', type=('build', 'run'))
    depends_on('py-mpld3@0.3:', type=('build', 'run'))
    depends_on("py-pyrxp@2.1.0:", type=('build', 'run'))
    depends_on('py-pycbc-glue@1.0.1:', type=('build', 'run'))
    depends_on('py-kombine', type=('build', 'run'))
    depends_on('py-emcee@2.2.0:', type=('build', 'run'))
    depends_on('py-corner@2.0.0:', type=('build', 'run'))
    depends_on("py-cjson", type=('build', 'run'))
    depends_on("py-cython", type=('build', 'run'))
    depends_on("py-m2crypto", type=('build', 'run'))

    depends_on('fftw+float+long_double', type=('build', 'run'))
    depends_on('gsl', type=('build', 'run'))
    depends_on('libframe', type=('build', 'run'))
    depends_on('metaio', type=('build', 'run'))

    # LALSuite, --enable-swig-python,  --disable-lalstochastic, --disable-lalxml, --disable-lalinfere, --disable-laldetchar, --disable-lalappso
    depends_on("lalframe+swig_python", type=('build', 'run'))
    depends_on("lalmetaio+swig_python", type=('build', 'run'))
    depends_on("lal+swig_python", type=('build', 'run'))
    depends_on("lalinspiral+swig_python", type=('build', 'run'))
    depends_on("lalburst+swig_python", type=('build', 'run'))
    depends_on("lalsimulation+swig_python", type=('build', 'run'))
    depends_on("lalpulsar+swig_python", type=('build', 'run'))
    depends_on("lalapps+swig_python+static", when='+lalapps', type=('build', 'run'))

    depends_on("py-pylal", type=('build', 'run'))
    depends_on('py-pycbc-dqsegdb', type=('build', 'run'))
    depends_on("py-ligo-gracedb", type=('build', 'run'))

    depends_on("pegasus", type=('build', 'run'))

    def install_args(self, spec, prefix):
        args = super(PyPycbc, self).install_args(spec, prefix)
        return args + ['--record=INSTALLED_FILES',
                       '--single-version-externally-managed']
