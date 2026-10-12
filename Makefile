BUILDDIR = build
TESTSUITES =

.PHONY: coverage
coverage:
	coverage run -m pytest $(TESTSUITES)

.PHONY: test
test:
	pytest $(TESTSUITES)

.PHONY: lint
lint:
	flake8 .

.PHONY: typecheck
typecheck:
	mypy verspec test

.PHONY: static-check
static-check: lint typecheck

.PHONY: clean
clean:
	-rm -rf $(BUILDDIR)/*
