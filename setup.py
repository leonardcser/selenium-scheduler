from setuptools import find_packages, setup


def readme():
    with open("README.md") as f:
        return f.read()


def requirements():
    with open("requirements/requirements.txt") as f:
        return list(f.readlines())


setup(
    name="selenium_scheduler",
    version="0.0.1",
    description="Selenium webscraper conjobs",
    long_description=readme(),
    long_description_content_type="text/markdown",
    install_requires=requirements(),
    url="https://github.com/leonardcser/selenium-scheduler",
    author="Leonard C.",
    packages=[find_packages("selenium_scheduler")],
    classifiers=[],
)
