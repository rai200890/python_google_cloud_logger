from setuptools import setup, find_packages

with open("README.md", "r") as output:
    long_description = output.read()


__VERSION__ = "0.1.1"

setup(
    name="google_cloud_logger",
    version=__VERSION__,
    description="Google Cloud Logger Formatter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/rai200890/python_google_cloud_logger",
    author="Raissa Ferreira",
    author_email="rai200890@gmail.com",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.4.*",
    install_requires=[
        "python-json-logger>=0.1.10",
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: System :: Logging"
    ],
    zip_safe=False)
