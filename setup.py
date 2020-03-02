import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name="tavalidate",
        version="0.0.5",
        author="Douglas Liu",
        author_email="douglas@sohoffice.com",
        description="Utilities to help you validate and save Tavern response.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/sohoffice/tavalidate",
        packages=setuptools.find_packages(),
        install_requires=[
        ],
        classifiers=(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent"
        ),
)
