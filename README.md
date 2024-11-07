# IP Helper
![Build&Test Workflow](https://github.com/rogerxwu/ip_helper/actions/workflows/ci.yml/badge.svg)
![Build&Test Workflow](https://github.com/rogerxwu/ip_helper/actions/workflows/cd.yml/badge.svg)
![Python3.11](https://img.shields.io/badge/language-Python3.11-blue)

## Goal
A tool to take the ip and submask as the input and return all IP addressing details
https://pypi.org/project/ip-helper/

## Install
pip install ip-helper

## Dev
Make sure you have poetry installed, then run the following cmds
```
poetry install
poetry run ip-helper -h
poetry run ip-helper 8.8.8.8/20
```

## Debug
```
ip-helper [subnet] -v
```

## Test
To run test manually
```
# Pytest
poetry run pytest tests/test_main.py
```
