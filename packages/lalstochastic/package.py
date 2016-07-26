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
#     spack install lalstochastic
#
# You can edit this file again by typing:
#
#     spack edit lalstochastic
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *
from spack.environment import *

class Lalstochastic(Package):
    """LSC Algorithm Library - Stochastic
    LIGO Scientific Collaboration Algorithm Library  - Stochastic,
    containing routines for stochastic gravitational wave background
    data analysis.
    """

    homepage = "https://www.lsc-group.phys.uwm.edu/daswg/projects/lalsuite.html"
    url      = "http://software.ligo.org/lscsoft/source/lalsuite/lalstochastic-1.1.17.tar.xz"

    version('1.1.17', '77d28029df0c9183ddc08b1d6cb2be7c')
    version('1.1.18', '862a1c7f76e20b899fd610d0e0ee0643')

    variant('swig_python', True, 'Generate SWIG bindings for Python')
    variant('octave', False, 'Generate SWIG bindings for Octave')

    extends("python")
    depends_on("metaio")

    depends_on('swig', when='+swig_python')
    depends_on('swig', when='+octave')
    depends_on('py-numpy', when='+swig_python')
    depends_on('octave+fftw', when='+octave')

    depends_on('lalmetaio')
    depends_on('lal')

    
    #for p in ['+swig_python', '~swig_python']:
    #    for o in ['+octave', '~octave']:
    #        depends_on('lalmetaio' + p + o, when=p + o)
    #        depends_on('lal' + p + o, when=p + o)

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

        configure(*config_args)

        make()
        make("install")
                           
    def setup_environment(self, spack_env, run_env):
        run_env.set('LALSTOCHASTIC_PREFIX', self.spec.prefix)
        run_env.set("LALSTOCHASTIC_DATADIR",
                    join_path(self.prefix.share, 'lalstochastic'))

        # This step is required to overcome a restriction in 
        # "EnvironmentModifications.from_sourcing_files" that does not properly
        # handle paths which have no initial value.
        if '+octave' in self.spec:
            source_file_env = EnvironmentModifications.from_sourcing_files(
                join_path(self.prefix.etc,'lalstochastic-user-env.sh'))
            modifications = source_file_env.group_by_name()
            octave_path = modifications['OCTAVE_PATH'][0].value.split(':',1)[0]
            run_env.append_path("OCTAVE_PATH", octave_path)
