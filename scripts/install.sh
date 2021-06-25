#!/bin/sh -e



# Use the Python executable provided from the `-p` option, or a default.
[ "$1" = "-p" ] && PYTHON=$2 || PYTHON="python3"


if [ -f 'Pipfile' ] ; then
    echo 'exsists pipenv'
    PIPENV=`pipenv --venv`
    PREFIX="${PIPENV}/bin/"
    PIP="${PIPENV}/bin/pip"
else
    echo 'do not exsists pipenv'
    PREFIX=""
    PIP="pip"
fi

PACKAGE=$(basename `pwd`)

${PREFIX}autoflake --recursive ${PACKAGE}
${PREFIX}black ${PACKAGE} --check
"$PIP" install -e .



