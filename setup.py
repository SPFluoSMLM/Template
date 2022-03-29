import pathlib
import re
import setuptools


_here = pathlib.Path(__file__).resolve().parent

name = ""
alias = ""
description = ""

# for simplicity we actually store the version in the __version__ attribute in the source
with open(_here / name / "__init__.py") as f:
    meta_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", f.read(), re.M)
    if meta_match:
        version = meta_match.group(1)
    else:
        raise RuntimeError("Unable to find __version__ string.")

author = "Luc Vedrenne"

author_email = "vedrenneluc@gmail.com"


with open(_here / "README.md", "r") as f:
    readme = f.read()

url = "https://github.com/SPFluoSMLM/" + name

license = "Apache-2.0"

classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Programming Language :: Python :: 3",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
    "Topic :: Scientific/Engineering :: Information Analysis",
    "Topic :: Scientific/Engineering :: Mathematics",
]

python_requires = "~=3.8"

install_requires = [
    "torch>=1.5.0",
    "matplotlib>=3.4.0",
    "open3d>=0.10.0",
    "numpy>=1.19.0",
]

setuptools.setup(
    name=alias,
    version=version,
    author=author,
    author_email=author_email,
    maintainer=author,
    maintainer_email=author_email,
    description=description,
    long_description=readme,
    long_description_content_type="text/markdown",
    url=url,
    license=license,
    classifiers=classifiers,
    zip_safe=False,
    python_requires=python_requires,
    install_requires=install_requires,
    packages=setuptools.find_packages(exclude=["examples", "data"]),
)

# _______________________________________________________________________________________________ #
# Using this script:
# >>> python setup.py sdist bdist_wheel

# Resulting package should be inspected, checked, and tested with:
# > tar tzf realpython-reader-1.0.0.tar.gz
# > twine check dist/*
# > twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# Then finally if everything is ok:
# twine upload dist/*
# _______________________________________________________________________________________________ #
