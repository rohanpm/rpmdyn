import os

from setuptools import setup, find_packages

# from setuptools.command.develop import develop
# from setuptools.command.easy_install import easy_install
from setuptools.command.install_lib import install_lib
from setuptools.command.build_py import build_py
from setuptools.command.develop import develop


# Below classes have been borrowed from pytest-cov.


PTH_PATH = os.path.join(os.path.dirname(__file__), 'src', 'rpmdyn', 'rpmdyn.pth')

class BuildWithPTH(build_py):
    def run(self, *args, **kwargs):
        build_py.run(self, *args, **kwargs)
        dest = os.path.join(self.build_lib, os.path.basename(PTH_PATH))
        self.copy_file(PTH_PATH, dest)


class InstallLibWithPTH(install_lib):
    def run(self, *args, **kwargs):
        install_lib.run(self, *args, **kwargs)
        dest = os.path.join(self.install_dir, os.path.basename(PTH_PATH))
        self.copy_file(PTH_PATH, dest)
        self.outputs = [dest]

    def get_outputs(self):
        return list(install_lib.get_outputs(self)) + self.outputs


class DevelopWithPTH(develop):
    # FIXME: when package is installed in editable mode, figure out how to
    # make 'pip uninstall' delete the .pth.
    def run(self, *args, **kwargs):
        develop.run(self, *args, **kwargs)
        dest = os.path.join(self.install_dir, os.path.basename(PTH_PATH))
        self.copy_file(PTH_PATH, dest)


def get_description():
    return "Alternative Python bindings to RPM library"


def get_long_description():
    with open("README.md") as f:
        text = f.read()

    # Long description is everything after README's initial heading
    idx = text.find("\n\n")
    return text[idx:]


def get_requirements():
    with open("requirements.in") as f:
        return f.read().splitlines()


setup(
    name="rpmdyn",
    version="0.1.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    url="https://github.com/rohanpm/rpmdyn",
    license="GNU General Public License",
    description=get_description(),
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    install_requires=get_requirements(),
    python_requires=">=2.6",
    cmdclass={
        'install_lib': InstallLibWithPTH,
        'build_py': BuildWithPTH,
        'develop': DevelopWithPTH,
    },
)
