from spack import *

class LscsoftDeps(Package):
    """Description"""

    homepage = "http://www.example.com"
    url      = 'NA'

    version('20151009', '0123456789abcdef0123456789abcdef', url='NA', expand=False)

    variant('glue', default=True, description="GLUE")
    variant('lalsuite', default=True, description="LALSuite")
    variant('pylal', default=True, description="PyLAL")
    variant('gstlal', default=True, description="GSTLAL")

    depends_on('python', when='+glue')
    depends_on('py-numpy', when='+glue')
    depends_on('py-pyrxp', when='+glue')
    depends_on('py-m2crypto', when='+glue')
    depends_on('py-cjson', when='+glue')
    depends_on('py-pyxmpp', when='+glue')
    depends_on('libxml2+python', when='+glue')
    depends_on('py-m2crypto', when='+glue')
    depends_on('py-dns', when='+glue')

    depends_on('swig', when='+lalsuite')
    depends_on('py-healpy', when='+lalsuite')
    depends_on('gsl', when='+lalsuite')
    depends_on('fftw', when='+lalsuite')
    depends_on('libframe', when='+lalsuite')
    #depends_on('ldas-tools', when='+lalsuite')
    depends_on('metaio', when='+lalsuite')
    depends_on('libxml2', when='+lalsuite')
    depends_on('chealpix', when='+lalsuite')
    depends_on('hdf5', when='+lalsuite')

    depends_on('py-scipy', when='+pylal')
    depends_on('py-matplotlib', when='+pylal')
    depends_on('py-basemap', when='+pylal')
#68    }
#69    
#70    variant gstlal requires glue lalsuite pylal description {Include dependencies for gstlal development} {
#71      depends_run-append port:orc \
#72                         port:gstreamer010 \
#73                         port:gstreamer010-gst-plugins-base \
#74                         port:gstreamer010-gst-plugins-good \
#75                         port:py27-gobject \
#76                         port:py27-gst-python
#77    }

    def install(self, spec, prefix):
        pass
