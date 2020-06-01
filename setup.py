from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Replace LuckJMG",
    version="1.0.1",
    author="Lucas Mosquera",
    author_email="lucas.mosquera13@gmail.com",
    description="Add replace method improvements",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LuckJMG/Replace",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
