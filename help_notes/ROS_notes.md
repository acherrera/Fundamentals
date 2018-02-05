I will attempt to follow along with the ROS programming book to create
something useful. Notes are taken in a psuedo-python code


# Following along with the ROS online tutorial

## Understanding ROS nodes

Run roscore first thing when starting ROS

    roscore
    
Show nodes currently running

    rosnode list
    
To get information about a node use

    rosnode info /rosout
    
Can use rosrun to run without knowing the package path

Generally:

    rosrun [package_name] [node_name]
    
This will run turtlesim_node in turtilesim package

    rosrun turtlesim turtlesim_node
    
If you run 'rosnode list' here, you will see

    /rosout
    /turtlesim

ROS can assign names from the command line, which is very good. Notation is a
little strange though:

    rosrun turtlesime turtlesime_node __name:=my_turtle

If running rosnode list now:

    /rosout
    /my_turtle

Anthony note: this is useful with you want to run multiple nodes of the name
type - maybe you want 100 turtles, or you have two motors on a robot - you can
name each one individually without confusion

You can use *rosnode ping* to see that a rosnode is running

    rosnode ping my_turtle


** End of *Understanding Nodes* **




## Understanding Topics
Be sure that roscore is running

    roscore

Start turtlesim - see above for details

    rosrun turtlesim turtlesim_node

Start the input node so that we can drive the little guy around

    rosrun turtlesim turtle_teleop_key












# From here down is "legacy code". I.e. not organized well

This is notes from before 20180205 in which I became confused part way through

### NOTE: IF NOT SOURCED CORRECTLY, COMMANDS WON'T WORK


# Making a work space
    Obviously switch 'catkin_ws' to workspace name

    mkdir -p ~/catkin_ws/src    # Make directory
    cd ~/catkin_ws/src          # Go to source
    catkin_init_workspace       # Initiatie


    # Do this each time you make a new package to source package
    cd ~/catkin_ws              # go up one level
    catkin_make                 # This iniates it
    source devel/setup.bash     # soures the setup file
    """
    Make created build and devel. /build is for c++ which we
    mainly don't need anyways
    """



# Making a package

    cd ~/catkin_ws/src                          # to source
    catkin_create_pkg my_awesome_code rospy     # see below

    """
    here rospy is a dependancy and must be listed as such
    this is where you should list all dependencies
    Also, should edit the 'package.xml' file. 
    """


# Running a nodes
    # Use rosrun so you don't have to track down the packages all the time
    rosrun PACKAGE EXECUTABLE [ARGS]        # start roscore first

    roscore
    rosrun rospy_tutorials talker   # This will run no matter where you are


# Remapping Names
    """
    When calling a program, you can change the name of the topic to avoid
    naming conflicts. See book for more
    """


# Running a bunch of nodes
    roslaunch PACKAGE LAUNCH_FILE # general format
        # roslaunch files are .xml that describe the nodes to run
    """ Format for the launch file
        <launch>
          <node name="listener" pkg="rospy_tutorials" type="listener.py" output="screen"/>
          <node name="talker" pkg="rospy_tutorials" type="talker.py" output="screen"/>
        </launch>

        node    # ros graph name
        pkg     # where the package is located
        type    # type of node (just the filename to use)
        output  # where to put the output. "screen" is useful for bedugging

        roslaunch can restart crashed nodes and can start nodes over a
        network. Using crtl-C on the roslaunch terminal will close everything
    """




#### General Notes ####


ROS master
    # roscore is what tell the nodes where to get their data
    # roslaunch will also start the roscore
    # Note that the master is run on a network of some kind. This allows
      the program to work across a network if needed


nodes are litte programs
    # each node 'subscribes' or 'publishes' data
    # roscore keeps track of who wants what





#### Command Notes ####
rosnode - contains commands for examining ros nodes
    - rosnode info /EXAMPLE       
        - will show information for the EXAMPLE node

    - rosnode list                  
        - display list of nodes

rostopic - contains commands for examine topics within nodes. Use the
           rosnode command to find topics to examine
    - rostopic list
        - shows all the topics being published

    - rostopic info /EXAMPLE/TOPIC 
        - Will show more information on topic "TOPIC". Information 
          like type of data  

    - rostopic echo /some_topic
        - will show the data coming out of some topic

    - rostopic pub /some_topic msg/MessageType "data:value"
        - will put in data into a topic. 

                   

### Working with bag files ###
    # Note: must have roscore running #
rosbag
    - record
        - records information
    - info
        - show sumary of bag file
    - play
        - plays back the bag file
