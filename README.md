# IP Helper

## Goal
A tool to take the ip and submask as the input and return all IP addressing details

## Installation
Make sure you have poetry installed, then run the following cmds
```
poetry install
poetry run ip-helper 1.1.1.1/24
```

## Test
To run test case on ip_helper
```
# Pytest
poetry run pytest test/test_ip_helper_pytest.py
# Unittest
poetry run python -m unittest test/test_ip_helper.py
```