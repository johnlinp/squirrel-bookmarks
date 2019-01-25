#!/bin/bash

function sq {
    if [ "$#" == "0" ]
    then
        echo 'usage:'
        echo '    sq <branch|bookmark>'
        return
    fi
    local PLACE="$1"
    local JUMP_PATH
    JUMP_PATH=$(squirrel jump "$PLACE")
    if [ "$?" == "0" ]
    then
        echo jump to "$JUMP_PATH"
        cd "$JUMP_PATH"
    fi
}
