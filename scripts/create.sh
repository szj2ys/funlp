#/bin/bash

SOURCE=$1
# root project dir name
PROJECT_DIR=`pwd`
ENVNAME=$(basename $PROJECT_DIR)
echo "Virtual environment name is $ENVNAME"

# create virtual environment
pipenv --python 3.7

PIPENV=`pipenv --venv`
PREFIX="${PIPENV}/bin/"
PIP="${PIPENV}/bin/pip"



echo "installing python package ..."
${PIP} install --upgrade pip
while read PKG
do
  if [ "${SOURCE}" = "pypi" ]; then
    ${PIP} install ${PKG} -i https://pypi.org/simple
  elif [ "${SOURCE}" = "aliyun" ]; then
    ${PIP} install ${PKG} -i https://mirrors.aliyun.com/pypi/simple
  else
    ${PIP} install ${PKG} -i https://pypi.org/simple
  fi
done  < ${PROJECT_DIR}/requirements-dev.txt

#pipenv run python -m ipykernel install --user --name=${ENVNAME}
# 将环境配置到jupyter notebook中

#${PREFIX}jupyter kernelspec list  # look over existing kernels
# ${PREFIX}jupyter kernelspec remove ${ENVNAME} 删除指定kernel

