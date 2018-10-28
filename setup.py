from setuptools import setup

setup(
    name="google_cloud_logger",
    version="0.0.1",
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
    zip_safe=False)
