from setuptools import find_packages, setup

setup(
    name="spv",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "jinja2",
        "pdfkit",
        "boto3",
        "python-barcode"
    ]
)
