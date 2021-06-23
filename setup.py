from pathlib import Path

import pkg_resources
from setuptools import find_packages, setup

###### Readme #################################################################
readme = Path(".", "README.md").absolute()
changelog = Path(".", "CHANGELOG.md").absolute()

with readme.open("r", encoding="utf-8") as file:
    long_description = file.read()

with changelog.open("r", encoding="utf-8") as file:
    long_description += file.read()


def get_current_githash():
    import subprocess
    label = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip();
    label = label.decode('utf-8')
    return label


githash = get_current_githash()
long_description += "\n\n" + githash

############################################################################
req = Path(".", "requirements.txt").absolute()
with req.open() as fp:
    install_requires = [str(r)
                        for r in pkg_resources.parse_requirements(fp)
                        if "#" not in str(r)
                        ]

############################################################################
entry_points = {"console_scripts": [
    "generate=mygen.cli.cli_sequence:run_cli",


], }

############################################################################
setup(
    name="mygenerator",
    packages=find_packages(exclude=("tests", "dev_tools")),
    url="",
    license="MIT License",
    author="",
    install_requires=install_requires,
    author_email="n",
    description="Im",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version='0.0.1',
    entry_points=entry_points,
    python_requires=">=3.6",
    include_package_data=True,
    keywords=[, ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
