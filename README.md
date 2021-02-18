# Python Testing with pytest

## What Is pytest?
- Command-line tool that automatically finds tests you've written, run the tests and reports the results.
- Can be used by development teams, QA teams, individuals practicing TDD and open source projects.
- Project all over internet switched from unittest or nose to pytest, including Mozilla and Dropbox.

## Why use pytest?
- Simple tests are simple to write in pytest.
- Complex tests are still simple to write.
- Tests are easy to read.
- Tests are easy to read. (So important it’s listed twice.)
- You can get started in seconds.
- You use assert to fail a test, not things like self.assertEqual() or self.assertLessThan(). Just assert.
- You can use pytest to run tests written for unittest or nose.

## Setup
### Virtualenv
```shell
python -m venv .venv
source .venv/bin/activate
```
### Add main module to Python Path
```shell
 export PYTHONPATH=$PYTHONPATH:$(pwd)/pytest_presentation
```
### Install
```shell
python -m pip install -r requirements.txt
```

## Introduction
```shell
pytest -v tests/test_1_intro.py
```
## Testing module
```shell
pytest -v tests/test_2_add.py
```
## Testing exceptions
```shell
pytest -v tests/test_3_exceptions.py
```
## Parametrize
```shell
pytest -v tests/test_4_parametrize.py
```
## Skip
```shell
pytest -v tests/test_5_skip.py
```
## Subset of Tests
### Single Test File/Module
```shell
pytest -v tests/test_1_intro.py
```
### Single Test Function
```shell
pytest -v tests/test_1_intro.py::test_value_in_list
```
### Single directory
```shell
pytest -v tests/func/
```
### Single Test Class
```shell
pytest -v tests/func/test_6_integration.py::TestIntegration
```
### Single Test Method of a Test Class
```shell
pytest -v tests/func/test_6_integration.py::TestIntegration::test_list_tasks
```

### A set of tests based on Test Name
```shell
pytest -v -k task
```

## Fixtures
```shell
pytest -v tests/test_7_fixtures.py
```

## Plugins

- pytest-cov
- pytest-django
- pytest-mock
- pytest-env
- pytest-freezegun

- pytest-repeat: Run Tests More Than Once
- pytest-xdist: Run Tests in Parallel
- pytest-timeout: Put Time Limits on Your Tests
- pytest-instafail: See Details of Failures and Errors as They Happen
- pytest-sugar: Instafail + Colors + Progress Bar
- pytest-emoji: Add Some Fun to Your Tests
- pytest-html: Generate HTML Reports for Test Sessions
- pytest-pycodestyle, pytest-pep8: Comply with Python’s Style Guide
- pytest-flake8: Check for Style Plus Linting
- pytest-selenium: Test with a Web Browser
- pytest-django: Test Django Applications
- pytest-flask: Test Flask Applications


[Plugins from Docs](https://docs.pytest.org/en/latest/plugins.html)
[Plugins Compatíveis](http://plugincompat.herokuapp.com/)

### pytest-mock
```shell
python -m pip install pytest-mock 
```

```shell
pytest -v tests/test_8_mocker.py
```

[Mock Requests](https://docs.pytest.org/en/stable/monkeypatch.html#global-patch-example-preventing-requests-from-remote-operations)

### pytest-cov
```shell
python -m pip install pytest-cov
```
```shell
pytest -v --cov=pytest_presentation tests/
```
```shell
pytest -v --cov-report html  --cov=pytest_presentation tests/
```
[Debuggers and Pycharm](https://pytest-cov.readthedocs.io/en/latest/debuggers.html)
```shell
pytest --no-cov
```

### Construir seus próprios plugins
[Palestra - Rafael Henrique (PyBR 2019)](https://github.com/pythonbrasil/talks/blob/master/pythonbrasil-2019/talks/construindo-plugins-para-o-pytest/pybr2019-rafael-henrique-da-construindo-plugins-para-o-pytest.pdf)

## Reference
[Book: Python Testing with pytest](https://www.amazon.com/Python-Testing-pytest-Effective-Scalable/dp/1680502409)

## Author
[Patrick Rodrigues](mailto:patrick.pwall@gmail.com)
