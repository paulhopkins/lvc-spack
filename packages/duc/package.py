from spack import *


class Duc(Package):
    """Duc is a collection of tools for inspecting and visualizing disk usage.
       Duc scales quite well, it has been tested on systems with more than 500
       million files and several petabytes of storage."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://duc.zevv.nl/"
    url      = "https://github.com/zevv/duc/releases/download/1.4.1/duc-1.4.1.tar.gz"

    version('1.4.1', 'c2108ef00f20784a9401ae95550adf2e')

    depends_on('sqlite')

    def install(self, spec, prefix):
        config_args = ['--disable-ui', '--disable-x11', '--with-db-backend=sqlite3', '--disable-cairo']
        configure('--prefix={0}'.format(prefix), *config_args)

        make()
        make('install')
