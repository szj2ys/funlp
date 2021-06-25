#/bin/bash


# root project dir name
PROJECT_DIR=`pwd`
ENVNAME=$(basename $PROJECT_DIR)
echo "Virtual environment name is $ENVNAME"

# create virtual environment
pipenv --python 3.7

PIPENV=`pipenv --venv`
PREFIX="${PIPENV}/bin/"
PIP="${PIPENV}/bin/pip"


${PIP} install -r requirements-dev.txt
#${PIP} install -r requirements-dev.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

#pipenv run python -m ipykernel install --user --name=${ENVNAME}
# 将环境配置到jupyter notebook中

${PREFIX}jupyter kernelspec list  # look over existing kernels
# ${PREFIX}jupyter kernelspec remove ${ENVNAME} 删除指定kernel

