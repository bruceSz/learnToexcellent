

function exists() {
    #echo $*

   return

    #parrents=$(pwd|sed '/\// /g')
    #for i in $parrents;
    #do
    #    echo ''#if [ $i == ]
    #done
    #return 0
}

function get_real_path() {
    args=$*
    args_n=$(echo $args|sed 's/\./\//g')
    #if [ "$args" == "$args_n" ];then
    #    echo $args_n
    #fi
    root_dir=${args_n%%/*}
    cur_path=`pwd`
    dirs=$(echo $cur_path|sed 's/\./ /g')
    for dir in $dirs;
    do
        if [ "$dir" == "${root_dir}" ];
        then
            cur_path=${cur_path%%${dir}*}
            break
        fi
    done
    cur_path=${cur_path%%/}
    echo ${cur_path}/${args_n}


    
}

function from(){
    # The possible usage example is: from xxx.xxx import yy,yy,yy.
    # Here xxx means dir name,while yy means filename. 
    args="$@"
    is_dir=true
    dir=""
    files=""
    

    for arg in $args;do
        if [ "$arg" = "import" ];then
            #echo "meet keyword import:" $arg
            is_dir=false
        else
            if  $is_dir ;then
                # only support one dir,hence the judge is supposed to be entered once. 
                dir=$arg
            else
                # same as above,the branch should be entered only once
                files=$(echo $arg|sed 's/,/ /g')

                #filenames[$i]=$arg
                #i=$((i+1))

            fi
        fi

    done

    #echo $dir
    for file in $files;do
        fullpath=$dir.$file
        import $fullpath
    done

    #for filename in ${filenames[@]};do
    #    echo $filename
    #done
}
function import() {
    filenames="$*"
    filenames=$(echo $filenames|sed 's/,/ /g')
    for fn in $filenames;
    do
        fn=$(get_real_path $fn) 

        if [ -e $fn ];then
            source $fn
            #echo "found :",$fn
        else
            echo "Error import: $fn do not exist!!!"
        fi
    done
}

