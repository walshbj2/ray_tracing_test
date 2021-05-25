from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="ray_tracing_test",
    version="0.0.0",
    author="walshbj2",
    description="A simple ray tracer.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/walshbj2/ray_tracing_test",
    package_dir={"": "src"},
    packages=find_packages(),
    install_requires=requirements,
)
