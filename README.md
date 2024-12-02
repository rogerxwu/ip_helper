# IP Helper
![PyTest Check](https://github.com/rogerxwu/ip_helper/actions/workflows/ci.yml/badge.svg)
![Publish](https://github.com/rogerxwu/ip_helper/actions/workflows/cd.yml/badge.svg)
![Format Check](https://github.com/rogerxwu/ip_helper/actions/workflows/format-check.yml/badge.svg)
![Lint Check](https://github.com/rogerxwu/ip_helper/actions/workflows/lint-check.yml/badge.svg)
![Python3.11](https://img.shields.io/badge/language-Python3.11-blue)

A tool to take the ip and submask as the input and return all IP addressing details, released at https://pypi.org/project/ip-helper/

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
A tool to take the ip and submask as the input and return all IP addressing details

## Installation
Install from pip
```
pip install ip-helper
```
Install from source code
```
git clone https://github.com/rogerxwu/ip_helper.git
cd ip_helper
poetry install
poetry run ip-helper -h
```

## Usage
To check the ip details for 10.1.0.0/20
```
ip-helper 10.1.0.0/20
```
To debug
```
ip-helper [subnet] -v #debug
```

## Contributing
Run the following test and check before commit your change
Run pylint
```
poetry run pylint .
```
Run pytest
```
poetry run pytest tests/test_main.py
```
Run black
```
poetry run black --check .    # Check format
poetry run black .    # Fix format
```


## To do
Add -v, -vv, -vvv debug mode
