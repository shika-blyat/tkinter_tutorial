import setuptools

with open("README.md", "r") as fd:
    long_description = fd.read()

with open("VERSION", "r") as fd:
    version = fd.read().strip()

setuptools.setup(
    name="tkinter turorial",
    version=version,
    author="Shika-blyat",
    description="Tkinter simple MVC tutorial",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shika-blyat/tkinter_tutorial",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: X11 Applications",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
    ],
)
