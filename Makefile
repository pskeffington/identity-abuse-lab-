.PHONY: install test lint generate report export all

install:
	python -m pip install -e .[dev]

test:
	pytest

lint:
	ruff check src tests

generate:
	python -m identity_abuse_lab generate

report:
	PYTHONPATH=src python scripts/report_scenarios.py

export:
	PYTHONPATH=src python scripts/export_scored_events.py

all: generate export report test
