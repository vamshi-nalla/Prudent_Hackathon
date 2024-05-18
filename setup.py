from setuptools import find_packages, setup

setup(
    name="Text Generation",
    version="0.0.1",
    author="vamshi nalla",
    author_email="nvkrishna9396@gmail.com",
    packages=find_packages(),
    install_requires=["pipwin","google-generativeai","python-dotenv","streamlit"]
)
