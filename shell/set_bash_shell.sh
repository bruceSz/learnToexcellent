#!/bin/bash
setBashShell(){
    if which bash;then
        echo "has bash"
    else
        echo "no bash exist,exit..."
        exit 1
    fi
}
setBashShell
