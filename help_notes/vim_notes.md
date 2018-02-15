
Vim notes

    Open and closing indents
        ** Note, you must have folding turned on in .vimrc
       zj                       - move down a fold 
       zk                       - move up a fold
       zo                       - open fold
       zc                       - closes fold
       zM                       - closes all folds
       zO                       - Opens all folds


    Running Python
        ctrl-z                  - will pause currenty session
        $python3 whatever.py    - runs program whatever.py
        $fg                     - bring VIM back to foreground

    
    Find and replace %s is substitute command
        :%s/foo/bar/gc          - replace 'foo' with 'bar' and confirm 'c'

    Range searches
        :s/foo/bar/gc           - replace on current line
        :%s/foo/bar/gc          - replace on all lines
        :5,12s/foo/bar/g        - replace from 5 to 12. Note not prompt here
        :.,+2s/foo/bar/g        - current line (.) and next two lines
        
    Split pane
        :sp filename            - will open file
        ctrl-w[hjkl]            - move to pane. Use keys hjkl
                                - good candidate for remapping
        ctrl -ww                - next window
