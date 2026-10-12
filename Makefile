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
	mypy inversion test

.PHONY: doctest
doctest:
	sphinx-build -b doctest doc $(BUILDDIR)/doctest

.PHONY: static-check
static-check: lint typecheck

.PHONY: doc-html
doc-html:
	sphinx-build -b html doc $(BUILDDIR)/html

.PHONY: doc-deploy
doc-deploy: doc-html
	ghp-import --no-jekyll $(BUILDDIR)/html

.PHONY: clean
clean:
	-rm -rf $(BUILDDIR)/*
