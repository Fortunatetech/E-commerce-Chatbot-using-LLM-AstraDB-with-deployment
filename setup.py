from setuptools import find_packages, setup

setup(
    name="Ecommerc-chatbot",
    version="0.0.1",
    author="Ayodele Ayodeji",
    author_email="ayodeleayodeji250@gmail.com",
    packages=find_packages(),
    install_requires=['langchain-astradb','langchain ','langchain-openai','datasets','pypdf','python-dotenv','flask']
)