from setuptools import setup

setup(
    name="solscan-python",
    version="2.1.0",
    description="A minimal, yet complete, python API for solscan.io.",
    url="https://github.com/MrsNFTy/solscan-python",
    author="Panagiotis-Christos Kotsias",
    author_email="kotsias.pan@gmail.com",
    license="MIT",
    packages=[
        "solscan",
        "solscan.configs",
        "solscan.enums",
        "solscan.modules",
        "solscan.utils",
    ],
    install_requires=["requests"],
    include_package_data=True,
    zip_safe=False,
)
