from setuptools import setup, find_packages

setup(
    name="Funny Gates",
    version="0.5.0",
    install_requires=[
        'pandas'  
    ],
    author="Daniel Papp",
    author_email="ds.papp02@gmail.com",
    description="A practice package to get accustomed to Git; Simple Boolean Gates",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0",
        "Operating System :: OS Independent",
    ],
)