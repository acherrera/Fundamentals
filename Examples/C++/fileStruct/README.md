# Example of how to use test structure for building a program

All directories have a .txt file that tells what should go in them.
The Makefile is how the program is put together and kind of the heart
of the operation. 

## Building Program
Run 'make' from the terminal and it will take the Makefile and put 
it all together nice and neat. 

Output will be under the /bin directory and called 'runner'

## More notes
In order for vim-syntastic to work, a little config file must be 
include that has '-I include/' to let sytastic know what is going on
