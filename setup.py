from setuptools import setup, find_packages

setup(
    name="WhatsSched",
    version="1.0.0",
    author="Ishant Yadav",
    author_email="yadav.ishantsbi0985@gmail.com",
    description="A simple Python module to schedule and send WhatsApp messages at a specific time of your choice.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/YadavIshant0808/WhatsSched",
    packages=find_packages(),
    install_requires=[
        "pywhatkit"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    license="MIT",  # Change to your chosen license

)
