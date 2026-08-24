from setuptools import setup, find_packages

setup(
    name="AutoPLC-Studio",
    version="1.0.0",
    description="Multi-Agent System for Industrial PLC Structured Text Code Generation, Formal Verification, and RAG Reasoning",
    author="Nachiket Gadilohar",
    author_email="nachiketlohar0306@gmail.com",
    url="https://github.com/nachiket0987/AutoPLC-Studio",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Interface Engine/Interface Device",
        "Topic :: Software Development :: Code Generators",
    ],
    python_requires=">=3.8",
)
