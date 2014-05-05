#!/bin/bash
SUDO=sudo

# root ユーザーの場合 sudo コマンドを抜かす
if [ $EUID -eq 0 ]; then
        SUDO=""
fi

# get linux distribution name
read dist_hint < /etc/issue
path=`dirname $0`
dist_name=`echo $dist_hint | awk '{print $1}'`
deploy_script="$path/dist/${dist_name,,}.sh"

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

# 正常に修了した場合自分を消去
trap 'rm $path/install.sh' EXIT

