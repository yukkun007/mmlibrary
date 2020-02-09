import os
from setuptools import setup

PACKAGE_NAME = "mmlibrary"

with open("README.md") as f:
    readme = f.read()

with open(os.path.join(PACKAGE_NAME, "VERSION")) as f:
    version = f.read()

setup(
    # matadata
    name=PACKAGE_NAME,
    version=version,
    description="my book library service library",
    long_description=readme,
    author="Yutaka Kato",
    author_email="kato.yutaka@gmail.com",
    url="https://github.com/yukkun007/mmlibrary",
    # liscence=
    # platform=
    # options
    packages=[PACKAGE_NAME],
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.6",
    install_requires=[
        "python-dotenv",
        "python-dateutil",
        "selenium",
        "beautifulsoup4",
        "jinja2"
    ],
    entry_points="""
        [console_scripts]
        {app} = {app}.cli:main
    """.format(
        app=PACKAGE_NAME
    ),
)
