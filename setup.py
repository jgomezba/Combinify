from setuptools import setup, find_packages

setup(
    name="Combinify",  
    version="0.1.0",   
    description="A combinatory package",  
    author="Your Name",  # Your name
    author_email="gomezbarrosojavier@example.com", 
    url="https://github.com/jgomezba/Combinify",
    packages=find_packages(),
    install_requires=[  "itertools"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
