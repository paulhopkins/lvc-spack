from spack import *

class PyDns(Package):
    """Description"""

    homepage = "http://www.example.com"
    url      = "https://pypi.python.org/packages/e1/ab/36f4e337d6cf6590f9cf46349f519b682542d211c604755ab8409f67f26b/dnspython-1.14.0.zip"

    version('1.14.0', '577f6b60b185d1ac90d76e9364a543d4')

    extends("python")
    depends_on("py-setuptools")

    def install(self, spec, prefix):
        python('setup.py', 'install', '--prefix=' + prefix)
