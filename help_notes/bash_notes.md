# Linux Command info


NOTE: use the 'man' command to see the manual page for a given command. for
example: 'man ls' will show the manual page for ls

## 3 - MOVING THROUGH DIRECTORIES

cd      Change the current directory

        ..  Go up one directory
        ~   Return to home directory  
        -   (Minus Sign) go to last directory. 

ls      list contents of given direcotry.

        -l  Long format of file for extra details
        -a  Shows all, inlcuding hidden files

less    shows the contents of a file

        Note: use in piplines to keep output from filling up screen. 
        Example: printenv | less
        This will 'open' new screen to view output

vim     editor for files
        Spend years learning this stupid thing

## 4 - MOVING AND EDITING - work with files

cp      copy files and directories

        -a      archive mode: copy along with attributes
        -i      interactive: prompt for overwrite permission 
        -r      recursive: copy backwards - required for directories
        -u      update: only copy new/newer files
        -v      verbose: display information as it's copied

mv      Move/rename files and directories

mkdir   Create directories

rm      Remove files and directories by defailt no warning

        -i      interactive: prompt for comfirmation
        -r      recursive:  delete backwards - for directories
        -f      force: ignores files that don't exist
        -v      verbose: shows output messages

Wildcards   Allows better matching of characters.

            *   Match any characters
            ?   Match any single character
            [characters]    Match character in []
            [!characters]   Match character not in []
           [[:class:]]     Match character in class
                [:alnum:]   Any alphanumeric character
                [:alpha:]   Any alphabet character
                [:digit:]   Any digit
                [:lower:]   Any lowercase letter
                [:upper:]   Any uppercase letter 
            Examples:
            g*              anything beginning with g
            b*.txt          anything beginning with b ending in ".txt"
            Data???         "Data" followed by three characters
            [abc]*          begins with "a,b, or c"
            [![:digit:]]*   not beginning with a digit
            [0-9]           will match any number 0-9
            [0-9][0-9]      matches exactly two numberals
            *[[:lower:]123] ends in lowercase letter OR numbers 1,2,3 
 

ln      Create hard and symbolic links must specific the locations for the link
to point to. Example: ln -s /home/Documents/file.txt

        -s      symbolic: creates a soft link (good)


## 5 - COMMAND OPTIONS - MORE WITH COMMANDS

type    How a command is interpreted

which   Which program will be executed

help    Help for shell builtins

apropos List of appropriate commands

man     Command's manual page

info    Command's info page

whatis  Display a brief description of command

alias   Create an alias for a command: USEFUL
        alias runit='ls -la'    Use 'type runit' to make sure the wods is not
        in use currently. 

unalias Used to remove a previously created alias



## 6 - I/O REDIRECTION

cat     Concatenate files

sort    Sort lines of text

uniq    report/remove repeated lines
        -d      will show duplicates rather than remove them

grep    print matching lines

wc      wordcount: print newline, word and byte count for file
        -l      will only count lines

head    show first part of file
        -n      number of lines to display
        show first 5 lines of file - same for tails
        head -n 5 ls-output.txt

tail    show last part of file
        -n      number of lines to display
        -f      shows files in real time - USEFUL FOR LOG

tee     read standard input and write to standard output and files
        Can take data out at a certain poit, and allow the process to continue. 
        Example: 
        ls /usr/bin | tee ls.txt | grep zip
        This will output the 'ls' command before using grep on it
        
>       Redirection operatore. Will send the output of the command to the
specified file: but will overwrite
        > output.txt        Will create file
        ls -l > /usr/bin    Will send output to file 

>>      Appended redirection. Adds output to end of file
        Can also redirect error output, but whatever. 

|       Pipeline: Send output of one command to the next command
        ls -l /usr/bin | less

        These can be made to create filters by combining commands
        Show programs
        ls /bin /usr/bin | sort | less

        Count number of programs
        ls /bin /usr/bin | sort | uniq | wc -l 

        All programs with 'zip'
        ls /bin /usr/bin | sort | uniq | grep zip

        Last 5 programs in program file
        ls /usr/bin | tail -n 5


## 7 - Seeing the World as the Shell Sees it

echo    - Display a line of text

        This can be used to see how the shell will interpret a command
        Example:
        echo *      Will print out in the interpretation
        echo D*
        echo *s
        echo [[:upper:]]*
        echo .[!.]* Will show hidden files without the ".." file

Using math  

        $((2+2))            Will output 4
        $(($((5**2))*3))    Will output (5^2)*3

Brace Expansion - SUPER useful for file/directory creationg

        echo Front-{A,B,C}-Back  
        echo Number{1..5}
        echo {01..15}
        echo {001..15}
        echo {Z..A}
        echo a{A{1,2},B{3,4}}b
        Example:file directories for months and years.
            mkdir {2007..2009}-{01..12} 

Parameter Expansion - some words are variables more later

        echo $USER
        printenv | less     - use less to keep bash from filling up

Command Substitution- use output of command as input

        Example:
            ls -l $(which cp)   - list cp location details
            file $(ls -d /usr/bin/* | grep zip) show file details for all files
            returned by command in $().
            $() will treat the stuff inside as an input for command

Quoting: Lots of stuff here. Just kind of skipping it

        Use quoting to keep format
        echo $(cal)     No formatting
        echo "$(cal)"   Includes formatting



### 8 - Advanced Keyboard Tricks
Lots of information on moving around - using Vi so whatever

clear - Clears the screen

history - Display history list
