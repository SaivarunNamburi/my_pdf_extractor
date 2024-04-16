from setuptools import setup, find_packages

setup(
    name='my_pdf_extractor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'PyMuPDF'
    ],
    entry_points={
        'console_scripts': [
            'extract-pdf-info = my_pdf_extractor.extractor:main'
        ]
    }
)
