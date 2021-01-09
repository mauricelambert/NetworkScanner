from setuptools import setup, find_packages
import NetworkScanner

setup(
    name = 'NetworkScanner',
 
    version = NetworkScanner.__version__,
    packages = find_packages(),

    author = "Maurice Lambert", 
    author_email = "mauricelambert434@gmail.com",
 
    description = "This package implement a NetworkScanner.",
    long_description = open('README.md').read(),
    long_description_content_type="text/markdown",
 
    include_package_data = True,

    url = 'https://github.com/mauricelambert/NetworkScanner',
 
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8"
    ],
 
    entry_points = {
        'console_scripts': [
            'NetworkScan = NetworkScanner:scanner'
        ],
    },
    python_requires='>=3.6',
)
