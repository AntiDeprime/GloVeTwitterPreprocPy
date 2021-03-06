with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GloVeTwitterPreprocPy", # Replace with your own username
    version="0.1.0",
    author="Aleksei Shchetinin",
    author_email="to@alxy.sh",
    description="Python script for preprocessing Twitter data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AntiDeprime/GloVeTwitterPreprocPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License ::  MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)