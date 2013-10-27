function test
{

    message=`cat test| sed -n '/Help_Msg_Begin/,/Help_Msg_End/p' | awk '$0!~/Help_Msg_/'`
    echo $message
}
test
