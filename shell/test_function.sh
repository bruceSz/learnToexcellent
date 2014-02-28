echo $(uname)
declare num=1000;

uname() {
    echo "test!";
    ((num++))
    return 100;
}

testvar() {
    local num=10;
    ((num++));
    echo $num;
}
echo_para1() {
    echo $0
    if [ $1 ];then
        echo $1
    fi
}
sum() {
    echo $0,$1,$2
    # result can only return 0-255
    return $(($1+$2))
}

foo() {
    local Foo="bar"
}

bar() {
    foo
    echo $Foo
}

test_uname() {
    uname;
    echo $?
    echo $num;
    testvar;
    echo $num;
}

test_sum() {
    total=$(sum 255 1)
    echo result is $?
    echo $total
}
test_bar() {
    bar
}
test_bar

