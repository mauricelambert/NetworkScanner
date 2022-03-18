from setuptools import setup

setup(
    name="NetworkScanner",
    version="1.0.0",
    py_modules=["NetworkScanner"],
    install_requires=["PythonToolsKit"],
    author="Maurice Lambert",
    author_email="mauricelambert434@gmail.com",
    maintainer="Maurice Lambert",
    maintainer_email="mauricelambert434@gmail.com",
    description="This module implements a NetworkScanner.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    url="https://github.com/mauricelambert/NetworkScanner",
    project_urls={
        "Documentation": "https://mauricelambert.github.io/info/python/security/NetworkScanner.html",
        "Executable": "https://mauricelambert.github.io/info/python/security/NetworkScanner.pyz",
    },
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Natural Language :: English",
        "Topic :: System :: Networking",
        "Topic :: Security",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.9",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
    ],
    entry_points={
        "console_scripts": ["NetworkScan = NetworkScanner:scanner"],
    },
    python_requires=">=3.6",
    keywords=[
        "Network",
        "Scanner",
        "Discovery",
        "Host",
        "Ping",
        "nmap",
        "Security",
        "Scapy",
        "ARP",
    ],
    platforms=["Windows", "Linux", "MacOS"],
    license="GPL-3.0 License",
)
