# What is this


## Most helpful notes
Add *export PATH=~/bin:"$PATH"* to the .bashrc file to add a source of
scripts to your bash environment. This allow you to call them without
specifying the location all the time

Will then need to use *. .bashrc* to apply changes for current session.
**NOTE** The usr/bin path is usually already part of the $PATH environment so
shoudldn't need to be sourced



## Where should scripts go

*/usr/local/bin*        - everyone can run
*/usr/local/sbin*       - system administrator scripts
*~/bin*                 - personal scripts

*/bin*                  - Do not put here
*/usr/bin*              - Do not put here either

# Notes from Linux commnad line book 

## Here Documents

Another form of I/O redirection which allows us to embed a body of textn the
script

    command<< token
    TEXT
    token

Here command is the command to run and token is the marker that marks the end
of the text. The first line sets up those two items

Can also use the *<<-* operator to ignore tabs, making the file easier to read

    command <<- token
        Text
        more text
    token

Generally the token is *_EOF_* since you are not likely to use that in whatever
command you are trying to run



# Notes from website
Notes on how to use bash scripts
this is mainly taken from

    https://ryanstutorials.net/bash-scripting-tutorial/bash-variables.php

However my version is shorter and includes some custom notes


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


### Variables

Variables are well.... we know what variables are. To take in variables as
arguement we use $1 for arguement one, $2 for arguement two and so on. For
example, to create an advanced copy script:

    #!/bin/bash
    #simple copy script
    cp $1 $2
    #show data
    echo Detail for $2
    ls -lh $2

Special variable names

    $0          - name of bash script
    $1-$9       - First 9 arguments
    $#          - Number of arguements passed
    $@          - all arguemnts pass
    $?          - exit status of most recent process
    $$          - process ID of current script
    $USER       - Username of user running script
    $HOSTNAME   - Machine hostname
    $SECONDS    - Number of seconds since script started
    $RANDOM     - Returns a random number
    $LINENO     - Returns current linenumber in bash script

#### How to set variables
Note that there are no spaces and to call the variable you have to use the *$*

    variable=value

To call the variable

    $variable

You can also assign a variable more than one word by using quotes. Single
quotes are literal and double will be expanded if passing a variable.

    myvar='Hello World'     - will be interpreted literally. No difference
    newvar="More $myvar"    - will expand the $myvar
    newvar='More $myvar'    - will interpret literally. No expansion

#### Command Substitution
You can call a command as the variable and take the output of the command as
the value. This will assign the count of lines of the ls function to the value
myvar. This allows you to see how many files are in the /etc folder

    myvar=$(ls /etc | wc -l)
    echo $myvar

If the output of the command is more than one line, the newline characters will
be stripped out and only a single line will be interpreted as a variable


Because of the odd way that this can sometimes behave it's a good idea to test
your commands before putthing them in a script. That is, assign the variable
and echo the variable as we did above

#### Exporting Variables

You can export variable by calling new instances of a scipt and passing the
variables to them. 
