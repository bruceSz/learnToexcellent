
function part() {

    TARGET_DEV=$1
    PART_TYPE=$2
    PART_NUMBER=$3
    START=$4
    END=$5
    expect <<-END
    spawn fdisk $TARGET_DEV
    expect "(m for help):"
    send "n\n"
    expect "(1-4)\n"
    send "$PART_TYPE\n"
    expect "(1-4):"
    send "$PART_NUMBER\n"
    expect "):"
    send "$START\n"
    expect "):"
    send "$END\n"
    expect "(m for help):"
    send "w\n"
    expect eof
    exit 
    END
}

function unpart() {

    TARGET_DEV=$1
    PART_NUMBER=$2
    expect <<-END
    spawn fdisk $TARGET_DEV
    expect "(m for help):"
    send "d $PART_NUMBER\n"
    expect "(m for help):"
    send "w\n"
    expect eof
    exit 
    END
}
