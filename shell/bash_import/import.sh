@absolute
function exists() {
    #echo $*

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
    args="$@"
    dirs=""

    for arg in $args;do
        
    done
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

function from()
