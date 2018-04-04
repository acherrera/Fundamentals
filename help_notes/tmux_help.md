# Help notes for tmux #


### Session creations and removal ###
tmux new -s foo             # new attached session called 'foo'
tmux new -s foo -d          # Detached session
tmux ls                     # list sessions
tmux attach                 # attached session
tmux kill-session -t foo    # kills foo session


### Ctrl + b window commands ###

c                           # new window
s                           # Switch session
n                           # next window
p                           # previous window
w                           # show windows


### ctrl + b pane commands ###
%                           # split left and right
"                           # split top and bottom
o                           # Switch
C-o                         # Rotate panes
!                           # break pane into window
q                           # display pane number 
*arrow keys*                # move that direction
