from setuptools import setup

__VERSION__ = "0.1.0"


setup(
    name="google_cloud_logger",
    version=__VERSION__,
    description="Google Cloud Logger Formatter",
    url="http://github.com/rai200890/python_google_cloud_logger",
    author="Raissa Ferreira",
    author_email="rai200890@gmail.com",
    license="MIT",
    packages=["google_cloud_logger"],
    python_requires=">=3.4.*",
    install_requires=[
        "python-json-logger>=v0.1.5",
    ],
    classifiers=[
        "Environment :: Web Environment", "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English", "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: System :: Logging"
    ],
    zip_safe=False)
