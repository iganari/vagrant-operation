#!/usr/bin/env bash

export echo_e='echo -e'

### 第1引数が数字かどうか確認
### 数字であれば、パス出来る
### e.g. chk_cum 1
chk_num()
{
  expr ${1} + 1 > /dev/null 2>&1
  result=${?}
  ### 数値1 -lt 数値2 ==> 数値1が数値2より小さい場合に真
  if [ ${result} -lt 2 ]; then
    ${echo_e} '' > /dev/null
  else
    ${echo_e} "${1} is no number" "\n"'see you again !!'
    exit
  fi
}

### vmの名前が渡された時にそのvagrantfileのPATHを検索する
### search_vgfile hogehoge_web
search_vgfile()
{
  for i in `find ~/ -name 'Vagrantfile' | grep -v VirtualBox`
    do
      grep -r "${1}" ${i}
      # echo $?
      if [ $? = "0" ];then
        echo "path =>" $i
      fi
    done
}

### check vm
VBoxManage list vms | cut -f 1 -d " " | sed -e "s/\"//g" | grep -v "default"        > /tmp/vmlist_all
VBoxManage list runningvms | cut -f 1 -d " " | sed -e "s/\"//g" | grep -v "default" > /tmp/vmlist_running


### VM operation
${echo_e} '## Virtual Box List ## ' "\n" 
${echo_e} "-------------------------------------------------------" "\n"
${echo_e} " <--- [   ALL VM   ]      |    [   Running VM   ] ---> " "\n"
${echo_e} "-------------------------------------------------------" "\n"

diff -y /tmp/vmlist_all /tmp/vmlist_running

${echo_e} "\n"'###################### ' "\n" 
${echo_e} "\n" '## choose VM operation' "\n" '1 : start' "\n" '2 : stop' "\n" '3 : search' "\n" '9 : exit'
read ans_1


### ans_1が数字であることの確認
chk_num ${ans_1}

if [ ${ans_1} = 1 ] ; then
    ${echo_e} "\n"'Which start ?'"\n"
        diff /tmp/vmlist_all /tmp/vmlist_running | grep \< | cut -d\  -f2              > /tmp/vmlist_diff
        cat -b /tmp/vmlist_diff
        read ans_2        
        ### ans_2が数字であることの確認
        ${echo_e} ${ans_2}
        chk_num ${ans_2}

        num_line=`cat /tmp/vmlist_diff | wc -l`

        ### 数値の大きさにて処理判定
        ### 数値1 -le 数値2 ==> 数値1が数値2より小さいか等しい場合に真
        if [ "${ans_2}" -le "0" ]; then
          ${echo_e} "pls 1 ~ ${num_line}"
        ### 数値1 -gt 数値2 ==> 数値1が数値2より大きい場合に真
        elif [ "${ans_2}" -gt "${num_line}" ]; then
          ${echo_e} "pls 1 ~ ${num_line}"
        else
          ans_2_list=`sed -n ${ans_2}p /tmp/vmlist_diff` 
          ${echo_e} "start ${ans_2_list}"
          VBoxManage startvm "${ans_2_list}" -type vrdp
        fi
elif [ ${ans_1} = 2 ] ; then
    ${echo_e} "\n"'which end ?'"\n"
        cat -b /tmp/vmlist_running
        read ans_2
        ### ans_2が数字であることの確認
        ${echo_e} ${ans_2}
        chk_num ${ans_2}

        num_line=`cat /tmp/vmlist_running | wc -l`

        ### 数値の大きさにて処理判定
        ### 数値1 -le 数値2 ==> 数値1が数値2より小さいか等しい場合に真
        if [ "${ans_2}" -le "0" ]; then
          ${echo_e} "pls 1 ~ ${num_line}"
        ### 数値1 -gt 数値2 ==> 数値1が数値2より大きい場合に真
        elif [ "${ans_2}" -gt "${num_line}" ]; then
          ${echo_e} "pls 1 ~ ${num_line}"
        else
          ans_2_list=`sed -n ${ans_2}p /tmp/vmlist_running` 
          ${echo_e} "stop ${ans_2_list}"
          VBoxManage controlvm "${ans_2_list}" poweroff
        fi
elif [ ${ans_1} = 3 ] ; then
    ${echo_e} "\n"'which search ?'"\n"
        cat -b /tmp/vmlist_all
        read ans_2
        ### ans_2が数字であることの確認
        ${echo_e} ${ans_2}
        chk_num ${ans_2}

        num_line=`cat /tmp/vmlist_all | wc -l`

        ### 数値の大きさにて処理判定
        ### 数値1 -le 数値2 ==> 数値1が数値2より小さいか等しい場合に真
        if [ "${ans_2}" -le "0" ]; then
          ${echo_e} "pls 1 ~ ${num_line}"
        ### 数値1 -gt 数値2 ==> 数値1が数値2より大きい場合に真
        elif [ "${ans_2}" -gt "${num_line}" ]; then
          ${echo_e} "pls 1 ~ ${num_line}"
        else
          ans_2_list=`sed -n ${ans_2}p /tmp/vmlist_all` 
          ${echo_e} "search ${ans_2_list} ..."
          search_vgfile ${ans_2_list}
        fi
elif [ ${ans_1} = 9 ] ; then
    ${echo_e} 'See you !!'
else
    ${echo_e} 'See you !!'    
fi

### 片付け作業
rm -rf /tmp/vmlist_*
exit
