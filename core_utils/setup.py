from setuptools import find_packages, setup


setup(
    name="shop-core-utils",
    version="0.0.1",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        'kombu'
    ]
)
