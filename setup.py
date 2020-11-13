import pathlib
from setuptools import setup,find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="TOPSIS-Anubhav-101803051",
    version="1.0.0",
    description="Compute Topsis Scores/Ranks of a given csv file",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/sharma-anubhav/Topsis",
    author="Anubhav Sharma",
    author_email="anubhav0399@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["topsis"],
    include_package_data=True,
    install_requires=find_packages(),
    entry_points={
        "console_scripts": [
            "topsis=topsis.__main__:topsis",
        ]
    },
)