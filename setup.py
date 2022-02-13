from setuptools import setup, find_packages

setup(
    name='NotebookAPI',
    version='0.1.0',
    packages=find_packages(include=['src', 'src.*']),
    install_requires=[
        "pymongo==3.12",
        "beanie==1.9.1",
        "uvicorn==0.17.4",
        "python-dotenv==0.19.2",
        "fastapi-pagination==0.9.1",
        "pydantic~=1.9.0",
        "pytest==7.0.1",
        "trio==0.19.0"
    ]
)