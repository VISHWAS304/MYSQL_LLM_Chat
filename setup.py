from setuptools import setup, find_packages

setup(
    name="MYSQL_LLM_Chat",  # Name of your package
    version="0.1",  # Version of your package
    author="VISHWAS BHUSHAN BASURU",  # Your name or organization
    author_email="vishwasbhushanb@gmail.com",  # Your email
    description="A package for managing obesity prediction data and configurations in database with LLM and Agentic AI",  # Short description
    long_description=open("README.md").read(),  # Long description from README.md
    long_description_content_type="text/markdown",  # Type of long description
    url="https://github.com/VISHWAS304/MYSQL_LLM_Chat",  # URL to your project repository
    packages=find_packages(),  # Automatically find all packages (including `src`)
    install_requires=[  # List of dependencies
        "pymysql",
        "pyyaml",
        "pandas",
        "numpy",
    ],
    classifiers=[  # Metadata about your package
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",  # Minimum Python version required
)