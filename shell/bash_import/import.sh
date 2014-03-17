function exists() {
    echo $*

    parrents=$(pwd|sed '/\// /g')
    for i in $parrents;
    do
        if [ $i == ]
    done
    return 0
}
function import() {
    filenames="$*"
    filenames=$(echo $filenames|sed 's/,/ /g')
    for fn in $filenames;
    do
        fn=$(echo ${fn}|sed 's/\./\//g')
        echo $fn

        if [ -e $filename ];then
            source $fn
        else
            if exists fn;then
                echo "exits"
            else
                echo "Error import: $fn do not exist!!!"
            fi
        fi
    done
}
