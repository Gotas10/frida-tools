# -*- coding: utf-8 -*-

import glob
import os

from setuptools import setup

pkg_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "frida_tools"))

agents = glob.glob(os.path.join(pkg_dir, "*_agent.*"))
assert len(agents) > 0, "Agents not compiled; run “npm install && npm run build” in agents/*/"
os.system("python ./build_aux/build_treesitter.py")
package_data = agents + ["treesitter.so"]

setup(
    name="frida-tools",
    version="12.0.1",
    description="Frida CLI tools",
    long_description="CLI tools for [Frida](https://frida.re).",
    long_description_content_type="text/markdown",
    author="Frida Developers",
    author_email="oleavr@frida.re",
    url="https://frida.re",
    install_requires=[
        "colorama >= 0.2.7, < 1.0.0",
        "frida >= 16.0.0, < 17.0.0",
        "prompt-toolkit >= 2.0.0, < 4.0.0",
        "pygments >= 2.0.2, < 3.0.0",
        "tree_sitter==0.20.1",
    ],
    license="wxWindows Library Licence, Version 3.1",
    zip_safe=True,
    keywords="frida debugger dynamic instrumentation inject javascript windows macos linux ios iphone ipad android qnx",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: JavaScript",
        "Topic :: Software Development :: Debuggers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=["frida_tools"],
    package_data={
        "frida_tools": package_data,
    },
    entry_points={
        "console_scripts": [
            "frida = frida_tools.repl:main",
            "frida-ls-devices = frida_tools.lsd:main",
            "frida-ps = frida_tools.ps:main",
            "frida-kill = frida_tools.kill:main",
            "frida-ls = frida_tools.ls:main",
            "frida-rm = frida_tools.rm:main",
            "frida-pull = frida_tools.pull:main",
            "frida-push = frida_tools.push:main",
            "frida-discover = frida_tools.discoverer:main",
            "frida-trace = frida_tools.tracer:main",
            "frida-join = frida_tools.join:main",
            "frida-create = frida_tools.creator:main",
            "frida-compile = frida_tools.compiler:main",
            "frida-apk = frida_tools.apk:main",
        ]
    },
)
