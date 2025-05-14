@echo off
set PYTHONPATH=.
pytest tests --cov=src --cov-report=term-missing
pause