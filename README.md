# IP Helper
![PyTest Check](https://github.com/rogerxwu/ip_helper/actions/workflows/ci.yml/badge.svg)
![Publish](https://github.com/rogerxwu/ip_helper/actions/workflows/cd.yml/badge.svg)
![Format Check](https://github.com/rogerxwu/ip_helper/actions/workflows/format-check.yml/badge.svg)
![Lint Check](https://github.com/rogerxwu/ip_helper/actions/workflows/lint-check.yml/badge.svg)
![Python3.11](https://img.shields.io/badge/language-Python3.11-blue)

## Goal
A tool to take the ip and submask as the input and return all IP addressing details
https://pypi.org/project/ip-helper/

## Install
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
poetry run ip-helper 8.8.8.8/20
ip-helper [subnet] -v #debug
```

## Dev and Contribute
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
1. add pylint for code analysis
2. add black for formatting
