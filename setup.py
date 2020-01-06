from setuptools import find_packages, setup

setup(
    name="tempus-cli",
    version="0.2.0",
    description="A small time tracker for the terminal",
    author="Buddhima Aushan",
    license="MIT",
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.7",
    entry_points={"console_scripts": ["tempus=tempus.cli:main"]},
)
