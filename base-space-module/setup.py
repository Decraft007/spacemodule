from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Um simples pacote que adiciona a função space(int), onde int é um inteiro que vai ser quantos espaços vão ser adicionado'
LONG_DESCRIPTION = "para implementar use assim exemplo: print('esse é um exemplo', space(10), simples), esse é um pacote bem simples e leve"

# Setting up
setup(
        name="space-module", 
        version=VERSION,
        author="Pablo Gomes",
        author_email="<pablo.gs.p2gs@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], 
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3.11.5",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)