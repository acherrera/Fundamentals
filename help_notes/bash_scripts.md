# Bash scripting notes

## 'Here' commands
Used to feel lots of lines to single command. Use *<<-* to ignore indents for
better readability

    cat<<- _EOF_
        This is where all your text can go
        Like this command too.

    _EOF_

*cat* can be any command and *_EOF_* can be any identifier. This is just
fairly common convention


