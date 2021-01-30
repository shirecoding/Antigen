from distutils.core import setup

from setuptools import find_packages

from antigen import __version__

setup(
    name="antigen",
    version=__version__,
    author="shirecoding",
    author_email="shirecoding@gmail.com",
    scripts=["bin/antigen"],
    install_requires=[
        "Jinja2",
        "pytest",
        "pytest-html",
        "pytest-cov",
    ],
    url="https://github.com/shirecoding/Antigen",
    download_url=f"https://github.com/shirecoding/Antigen/archive/{__version__}.tar.gz",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
    packages=find_packages() + ["antigen.resources"],
    package_data={
        "antigen.resources": [
            "*",
            "**/*",
            "**/**/*",
            "**/**/**/*",
            "**/**/**/**/*",
        ]
    },
)
