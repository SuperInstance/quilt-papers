from setuptools import setup, find_packages
setup(
    name="quilt-papers",
    version="0.1.0",
    description="Convert canon lore to academic paper format",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Casey / SuperInstance",
    packages=find_packages(),
    python_requires=">=3.8",
)
