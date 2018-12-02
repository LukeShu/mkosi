#!/usr/bin/env python3
# SPDX-License-Identifier: LGPL-2.1+

import sys

from setuptools import setup

if sys.version_info < (3, 6):
    sys.exit("Sorry, we need at least Python 3.6.")


setup(
    name="mkosi",
    version="4",
    description="Create legacy-free OS images",
    url="https://github.com/systemd/mkosi",
    maintainer="mkosi contributors",
    maintainer_email="systemd-devel@lists.freedesktop.org",
    license="LGPLv2+",
    scripts=["mkosi"],
)
