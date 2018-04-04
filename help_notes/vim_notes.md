
# Vim notes

Right now these are just personal notes for vim. Starting to add more basic
commands


## Movement

### Simple movment
Moving to the top and bottom of file

    G       # Move to bottom of file
    gg      # Move to top of file
    xx gg   # Move 'xx' down. Ex: 'xx' = 12


### Marking Position
Can mark position and jump back and forth
    m+a     # mark position as 'a'. Can be an lowercase letter
    '+a     # Jump to beginning of marked position 'a'
    `+a     # move to position 'a'

## File management

To open the previously opened file

    ctrl+6

## Open and closing indents

Note, you must have folding turned on in .vimrc

   zj                       - move down a fold 
   zk                       - move up a fold
   zo                       - open fold
   zc                       - closes fold
   zM                       - closes all folds
   zO                       - Opens all folds


# Running programs without closeing vim
Neat trick used to run programs in the same window while keeping change
history. Useful for testing out quick changes and then undoing them if needed 

    ctrl-z                  - will pause currenty session
    $python3 whatever.py    - runs program whatever.py
    $fg                     - bring VIM back to foreground

    
# Find and replace 
%s is substitute command

    :%s/foo/bar/gc          - replace 'foo' with 'bar' and confirm 'c'

## Range searches

    :s/foo/bar/gc           - replace on current line
    :%s/foo/bar/gc          - replace on all lines
    :5,12s/foo/bar/g        - replace from 5 to 12. Note not prompt here
    :.,+2s/foo/bar/g        - current line (.) and next two lines
        
# Split pane

    :sp filename            - will open file
    ctrl-w[hjkl]            - move to pane. Use keys hjkl
                            - good candidate for remapping
    ctrl -ww                - next window

# Tabs
Use tabs to open lots of files and lots of movement. In NERDtree use 't' to
open a file in a new tab

    vim -p 1.txt 2.txt      - opens files in new tabs
    gt                      - go to next tab
    gT                      - go to previous tab
    
