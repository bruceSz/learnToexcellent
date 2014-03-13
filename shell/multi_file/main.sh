echo this is the main script
parse_para()  {
    if [ -z "${1}" ];then
        echo "should not happend!!!"
    fi

    while [ -n "${1}" ]
    do
        case ${1} in 
            -s| --schema)
                if [  a$debug != a ];then
                    echo "you provided -s option"
                fi
                shift
                SCHEMA=${1}
                ;;
            *)
                echo "unknow option"
                exit 1
                ;;
        esac
        shift
    done
}
source sub.sh 
