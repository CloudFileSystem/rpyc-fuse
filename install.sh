#!/bin/bash
SUDO=sudo

# root ユーザーの場合 sudo コマンドを抜かす
if [ $EUID -eq 0 ]; then
        SUDO=""
fi

# get linux distribution name
read dist_hint < /etc/issue
dist_name=`echo $dist_hint | awk '{print $1}'`
deploy_script="./dist/base/${dist_name,,}.sh"
python_deply_script="./dist/pypy/pip.sh"

# ディストリビューションのデプロイスクリプトの存在確認
if [ -f $deploy_script ]
then
	# get source
	source $deploy_script
else
	# error message
	echo "Deploy script($deploy_script) not found!!"
	exit
fi

# ディストリビューションのデプロイスクリプトの存在確認
if [ -f $python_deploy_script ]
then
	# get source
	source $python_deploy_script
else
	# error message
	echo "Deploy script($python_deploy_script) not found!!"
	exit
fi

