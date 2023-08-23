from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in hkm/__init__.py
from hkm import __version__ as version

setup(
	name="hkm",
	version=version,
	description="For Various Departments in HKM",
	author="Narahari Dasa",
	author_email="nrhd@hkm-group.org",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
