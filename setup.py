import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="grasslands-demo",
    version="0.1",
    author="Sam Bennetts",
    author_email="sam.bennetts@regen.network",
    license="GPLv3",
    description="demo of grasslands workflow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/regen-network/grasslands-demo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering",
    ],
    python_requires=">=3.7",
    install_requires=[
        "shapely",
        "rasterio",
        "rasterstats",
        "fiona",
        "geopandas",
        "pandas",
        "numpy", 
        "confuse",
    ],
)
