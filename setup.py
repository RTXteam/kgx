from setuptools import setup, find_packages

requires = [
    "prefixcommons>=0.1.4"
    "pip>=9.0.1"
    "networkx>=2.2"
    "SPARQLWrapper>=1.8.2"
    "pandas>=0.24.2"
    "pytest>=0.0"
    "mypy>=0.0"
    "pystache>=0.0"
    "rdflib>=0.0"
    "Click>=7.0"
    "neo4j>=1.7.4"
    "neo4jrestclient>=0.0"
    "pyyaml>=0.0"
    "BiolinkMG>=0.0"
    "biolinkml>=0.0"
    "bmt>=0.1.0"
    "prologterms==0.0.5"
    "shexjsg>=0.6.5"
    "terminaltables>=3.1.0"
    "stringcase>=1.2.0"
    "validators>=0.13.0"
]

setup(
    name='Knowledge Graph Exchange',
    version='0.0.1',
    packages=find_packages(),
    install_requires=requires,
    scripts=['bin/translator_kgx.py'],
    entry_points="""
        [console_scripts]
        kgx=translator_kgx:cli
    """
)
