# pylint: disable=W0622
"""cubicweb-tuto application packaging information"""


modname = "cubicweb_tuto"
distname = "cubicweb-tuto"

numversion = (0, 1, 0)
version = ".".join(str(num) for num in numversion)

license = "LGPL"
author = "LOGILAB S.A. (Paris, FRANCE)"
author_email = "contact@logilab.fr"
description = "beginer level cube"
web = "https://forge.extranet.logilab.fr/cubicweb/cubes/tuto"

__depends__ = {"cubicweb": ">= 4.1.0"}
__recommends__ = {}

classifiers = [
    "Environment :: Web Environment",
    "Framework :: CubicWeb",
    "Programming Language :: Python :: 3",
    "Programming Language :: JavaScript",
]
