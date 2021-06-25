#!/bin/sh -e


if [ -f 'Pipfile' ] ; then
    PIPENV=`pipenv --venv`
    PREFIX="${PIPENV}/bin/"
    PIP="${PIPENV}/bin/pip"
else
    PREFIX=""
    PIP="pip"
fi

PACKAGE=$(basename `pwd`)

${PREFIX}autoflake --recursive ${PACKAGE}
${PREFIX}black ${PACKAGE} --check
${PREFIX}python setup.py sdist bdist_wheel --universal
${PREFIX}twine upload dist/*
#${PREFIX}mkdocs gh-deploy --force
