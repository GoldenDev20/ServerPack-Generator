from setuptools import setup, find_packages

setup(
    name="minecraft-serverpack-generator",
    version="0.1.0",  # Change this version number as needed
    description="A Python-based tool to convert Minecraft modpacks into server-ready packages with Forge.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",  # Update this
    url="https://github.com/yourusername/minecraft-serverpack-generator",  # Update with your repo URL
    packages=find_packages(),  # Automatically find all packages in the project
    install_requires=[
        "pyyaml>=5.4.0",  # Dependency for handling YAML files
        "requests>=2.25.0",  # For downloading files (Forge installer)
        "tqdm>=4.59.0",  # For progress bar in the CLI
    ],
    entry_points={
        'console_scripts': [
            'serverpack-generator=CLI.main:main',  # Define the entry point to run the CLI app
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',  # Minimum Python version
    include_package_data=True,  # Include files from MANIFEST.in
)
