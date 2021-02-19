import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup (
    name="dflow",
    version="1.0.0",
    author="HdbSci",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HdbSci/dflow",
    packages=setuptools.find_packages(),
    classifiers= [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Vector :: Matrix :: Array",
    ],
    python_requires='>=3.6',
)