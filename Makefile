.PHONY: all virtualenv install-poetry install-dev clean dist-clean

SRC_DIR=public_transport_routing
TEST_DIR=tests

PYTHON_VERSION=python3.8
VIRTUALENV_DIR=${PWD}/env
PIP=${VIRTUALENV_DIR}/bin/pip
PIP_INSTALL=${VIRTUALENV_DIR}/bin/pip install
POETRY=${VIRTUALENV_DIR}/bin/poetry

# the `all` target will install everything necessary
all: install-dev

virtualenv:
	if [ ! -e ${PIP} ]; then ${PYTHON_VERSION} -m venv ${VIRTUALENV_DIR}; fi
	${PIP_INSTALL} --upgrade pip==21.1.2

install-poetry: virtualenv
	${PIP_INSTALL} poetry==1.1.6
	${POETRY} config virtualenvs.create false
	${POETRY} config virtualenvs.in-project true

install-dev: install-poetry
	${POETRY} install -vvv

test:
	${VIRTUALENV_DIR}/bin/pytest ${TEST_DIR} --cov ${SRC_DIR} --cov-report=xml\:coverage.xml

clean:
	rm -f .coverage coverage.xml
	rm -rf .idea
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;
	find . -depth -name '__pycache__' -exec rm -rf {} \;

dist-clean: clean
	rm -rf ${VIRTUALENV_DIR}
	find . -depth -name '*.egg-info' -exec rm -rf {} \;
	find . -depth -name '*.pytest*' -exec rm -rf {} \;
