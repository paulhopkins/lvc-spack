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
from spack.environment import *

class Lalxml(Package):
    """LSC Algorithm Library - XML
    LIGO Scientific Collaboration Algorithm Library - XML containing
    routines for accessing XML files using libxml2.
    """

    homepage = "https://www.lsc-group.phys.uwm.edu/daswg/projects/lalsuite.html"
    url      = "http://software.ligo.org/lscsoft/source/lalsuite/lalxml-1.2.1.tar.xz"

    version('1.2.1', '0c157b20cbcb6397240cc81f95b8dbe3')
    version('1.2.2', '7de3ee80512d0d5352184064560de9b5')

    variant('swig_python', True, 'Generate SWIG bindings for Python')
    variant('octave', False, 'Generate SWIG bindings for Octave')
    variant('fastgsl', False, 'Enable fast/inline GSL code')

    depends_on("gsl")
    depends_on("libxml2")
    extends('python')

    depends_on('swig', when='+swig_python')
    depends_on('swig', when='+octave')
    depends_on('py-numpy', when='+swig_python')
    depends_on('octave+fftw', when='+octave')

    for p in ['+swig_python', '~swig_python']:
        for o in ['+octave', '~octave']:
            for f in ['+fastgsl', '~fastgsl']:
                depends_on('lal' + p + o + f, when=p + o + f)


    def install(self, spec, prefix):
        config_args = ['--prefix=%s' % prefix]

        if '+swig_python' in spec:
            config_args.append('--enable-swig-python')
        else:
            config_args.append('--disable-swig-python')

        if '+octave' in spec:
            config_args.append('--enable-swig-octave')
        else:
            config_args.append('--disable-swig-octave')

        if '+openmp' in spec:
            config_args.append('--enable-openmp')
        else:
            config_args.append('--disable-openmp')

        if '+fastgsl' in spec:
            config_args.append('--enable-fast-gsl')
        else:
            config_args.append('--disable-fast-gsl')

        configure(*config_args)

        make()
        make("install")

    def setup_environment(self, spack_env, run_env):
        run_env.set('LALXML_PREFIX', self.spec.prefix)
        run_env.set("LALXML_DATADIR",
                    join_path(self.prefix.share, 'lalxml'))

        # This step is required to overcome a restriction in 
        # "EnvironmentModifications.from_sourcing_files" that does not properly
        # handle paths which have no initial value.
        if '+octave' in self.spec:
            source_file_env = EnvironmentModifications.from_sourcing_files(
                join_path(self.prefix.etc,'lalxml-user-env.sh'))
            modifications = source_file_env.group_by_name()
            octave_path = modifications['OCTAVE_PATH'][0].value.split(':',1)[0]
            run_env.append_path("OCTAVE_PATH", octave_path)
