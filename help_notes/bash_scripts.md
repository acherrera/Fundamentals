# What is this
Notes on how to use bash scripts

## Beginner Notes
In order to run the scripts that are created, will need to set permissions in
order to execute the script

    chmod 755 myscript.sh

Use *echo* to print to the screen

    echo 'Hello, world!'

Finding if a file exists:

    if [[ -e readme.txt ]] ; then
        echo 'The file "readme.txt" exists.'
    else
        echo 'The file "readme.txt" does not exist.'
    fi

The above commands run entirely in bash. But a large part of bash's usefulness
is running outside commands


### Running outside commands

This command will check the difference between two files if they both exist and
write that difference to its own file. If the file does not exist, it will
copty the original.

    if [[ -e config.txt ]] ; then
        echo 'The file "config.txt" already exists. Comparing with default . . .'
        diff -u config-default.txt config.txt > config-diff.txt
        echo 'A diff has been written to "config-diff.txt".'
    else
        echo 'The file "config.txt" does not exist. Copying default . . .'
        cp config-default.txt config.txt
        echo '. . . done.'
    fi



            
