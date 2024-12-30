# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 21:16:42 2024

@author: marca
"""

from setuptools import setup
from setuptools.command.install import install
import subprocess

class CustomInstallCommand(install):
    def run(self):
        # Run the standard install steps
        super().run()
        # Clone submodules recursively
        subprocess.check_call(['git', 'submodule', 'update', '--init', '--recursive'])

setup(
    setup_cfg=True,  # Tells setuptools to use setup.cfg for metadata
    cmdclass={
        'install': CustomInstallCommand,
    },
)