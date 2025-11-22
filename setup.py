pythonfrom setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("failsafe.txt", "r", encoding="utf-8") as f:
    failsafe_content = f.read()

setup(
    name="mercy-directive",
    version="1.0.0",
    author="Dulcinea Circelli",
    description="Ethical failsafe framework for AI systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DulicineaCircelli/mercy-directive",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.7",
    keywords="ai-safety ai-ethics value-alignment mercy government-ai",
)
