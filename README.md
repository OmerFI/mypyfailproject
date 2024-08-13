# Mypy 1.11.1 fail POC with Pydantic 1.10.11

1. Install the requirements

```python
❯ pip install -r requirements.txt
```

2. Run the mypy command

```python
❯ mypy .
/home/omerfi/mypyfailproject/.venv/lib/python3.10/site-packages/pydantic/env_settings.py:23: error: INTERNAL ERROR -- Please try using mypy master on GitHub:
https://mypy.readthedocs.io/en/stable/common_issues.html#using-a-development-mypy-build
If this issue continues with mypy master, please report a bug at https://github.com/python/mypy/issues
version: 1.11.1
/home/omerfi/mypyfailproject/.venv/lib/python3.10/site-packages/pydantic/env_settings.py:23: : note: please use --show-traceback to print a traceback when reporting a bug
```
