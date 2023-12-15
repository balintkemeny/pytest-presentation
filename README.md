# Pytest Presentation

## Creating a Virtual Environment and installing Pytest

```sh
python3 -m venv venv
source venv/bin/activate
pip install pytest
```

## Running a subset of tests

```sh
pytest tests/basics/test_ship.py::TestShip::test_equality
```

## Disabling output capture in case of passing tests

```sh
pytest -s
pytest --capture=no
```

## Tracing Fixture execution

```sh
pytest --setup-show
```
