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
#     spack install py-pycbc
#
# You can edit this file again by typing:
#
#     spack edit py-pycbc
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *

class PyPycbc(Package):
    """A Python toolkit for analysis of data from gravitational-wave laser
    interferometer detectors with the goal of detecting and studying signals
    from compact binary coalescences (CBCs)."""

    homepage = "https://github.com/ligo-cbc/pycbc"
    url      = "https://github.com/ligo-cbc/pycbc/archive/v1.5.5.tar.gz"

    version('1.5.5', '58f045c556c87dbe61f47e51aa082a69')
    version('1.5.4', 'fb32cb06069c5e952a5cbc4be4edb63b')
    version('1.5.3', '343ab2bbdc2243d168daec605275afde')

    extends('python')

    depends_on('py-setuptools', type='build')
    depends_on('py-decorator')
    depends_on('fftw+float+long_double')
    depends_on('gsl')
    depends_on('libframe')
    depends_on('metaio')

    depends_on("py-decorator")
    depends_on("py-numpy")
    depends_on("py-scipy")
    depends_on("py-unittest2")
    depends_on("py-h5py")
    depends_on("py-alabaster")
    depends_on("py-babel")
    #depends_on("boto==2.5.2
    depends_on("py-cython")
    depends_on("py-docutils")
    #depends_on("Flask==0.10
    #depends_on("Flask-Cache==0.13.1
    #depends_on("Flask-SQLAlchemy==0.16
    depends_on("py-funcsigs")
    #depends_on("itsdangerous==0.21
    depends_on("py-jinja2")
    #depends_on("linecache2==1.0.0
    depends_on("py-mako")
    depends_on("py-markupsafe")
    depends_on("py-matplotlib")
    depends_on("py-mock")
    #depends_on("https://github.com/ligo-cbc/mpld3/tarball/master#egg=mpld3-0.3git
    #depends_on("py-mysqldb1")
    depends_on("py-nose")
    #depends_on("pam==0.1.4
    depends_on("py-pbr")
    #depends_on("pegasus-wms==4.6.1
    depends_on("py-pillow")
    #depends_on("pip==7.1.2
    #depends_on("psycopg2==2.6
    depends_on("py-pyrxp@2:")
    #depends_on("py-pycbc-glue")
    #depends_on("py-pycbc-pylal")
    depends_on("py-glue")
    depends_on("py-pylal")

    depends_on("py-pygments")
    #depends_on("pyOpenSSL==0.13
    depends_on("py-pyparsing")
    depends_on("py-cjson")
    depends_on("py-dateutil")
    depends_on("py-pytz")
    #depends_on("requests==1.2.3
    depends_on("py-six")
    depends_on("py-snowballstemmer")
    depends_on("py-sphinx")
    depends_on("py-sphinx-rtd-theme")
    #depends_on("sphinxcontrib-programoutput==0.8
    depends_on("py-SQLAlchemy")
    #depends_on("traceback2==1.4.0
    #depends_on("Werkzeug==0.9.3
    #depends_on("WTForms==1.0.3
    depends_on("py-dqsegdb")
    #https://github.com/duncan-brown/dqsegdb.git@pypi_release#egg=dqsegdb
    depends_on("py-ligo-gracedb")

    depends_on("lalframe+swig_python")
    depends_on("lalmetaio+swig_python")
    depends_on("lal+swig_python")
    depends_on("lalinspiral+swig_python")
    depends_on("lalburst+swig_python")
    depends_on("lalsimulation+swig_python")
    depends_on("lalpulsar+swig_python")

    patch('remove_argparse.patch')
    patch('remove_argparse2.patch')

    def install(self, spec, prefix):
        setup_py('install', '--prefix={0}'.format(prefix))
