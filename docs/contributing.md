# Contributing

Contributions are welcome!

## Setup

```shell
git clone https://github.com/ranahaani/GNews.git
cd GNews
pip install -r requirements.txt
pip install pytest
```

## Running tests

```shell
pytest tests/ -v
```

## Workflow

1. Fork the repo
2. Create a feature branch: `git checkout -b feat/my-feature`
3. Write tests first (TDD)
4. Implement your change
5. Ensure all tests pass: `pytest tests/ -v`
6. Open a Pull Request against `master`

## Code style

- Follow PEP 8
- Add type hints to all public methods
- Keep the package lightweight — avoid adding heavy dependencies to core

## Reporting bugs

Open an issue at [github.com/ranahaani/GNews/issues](https://github.com/ranahaani/GNews/issues).
