I will attempt to follow along with the ROS programming book to create
something useful. Notes are taken in a psuedo-python code



# Going through the package and catkin process


## Createing a workspace for catkin. 
Note that you must add the source. I prefer to do this in the .bashrc by adding
source /opt/ros/<version>/setup.bash. This means I don't have to source it
manually every time.

### how to make a workspace

    mkdir -p ~/catkin_ws/src
    cd ~/catkin_ws/
    catkin_make

The catkin_make command handles all the hard parts for you. Now you have to
source the new setup file.

    source devel/setup.bash







# Here are the basic functions of ROS

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

### Rostopic intro. 

Get help with *rostopic -h*. Can also press tab key to show the possible sub-comands

Use 'echo' to show the data published on a topic. This will show the turtle
sim data

    rostopic echo /turtle1/cmd_vel 

Use rostopic list to get all the topics being published

    rostopic list -h        help
    rostopic list -v        For verbose output

### ROS messages

Use *rostopic type* to get the type of data the is being output.
    
    rostopic type /turtle1/cmd_vel      Outputs geometry_msgs/Twist
 
Use rosmsg to show details of messages. Must be a message
    
    rosmsg show geometry_msgs/Twist     Found using above command


### ROStopic pub

Use *rostopic pub [topic] [msg_type] [args]* to publish your down data to a stream of data

    rostopic pub    rostopic pub -1 /turtle/cmd_vel geometery_msgs/Twist -- '[2.0,0.0,0.0]' '[0.0, 0.0, 1.8]'

From the *rostopic type* and *rostopic show* commands we know what the topic is
expecting. linear [float64, float64, float64] angular
[float64,float64,float64]. Run *rosmsg show* command to see. *-1* means that it
will only publish once. *--* tells it that none of the next input is an option.
That is, it's an input

Publish data once every second. The rate is in Hz: here is one hertz 

    rostopic pub /turtle/cmd_vel geometery_msgs/Twist -r 1 -- '[2.0,0.0,0.0]' '[0.0, 0.0, 1.8]'

Now would be a good time to check rqt-graph to see what's going on

### Rostopic hz

Use *rostopic hz* to show the rate at which data is being published. 

    rostopic hz /turtle1/pose

Can use *rostopic type* and *rosmsg show* together to quickly get in depth
information about a topic

    rostopic type /turtle1/cmd_vel | rosmsg show


### Using rqt_plot

Use *rosrun rqt_plot rqt_plot* to get graph a data coming in. After running
this command, you can select which data to plot 

    rosrun rqt_plot rqt_plot


*end of understanding topics*


## Service and Parameters

Services are just another way that ros nodes talk to each other. Instead of
publishing and subscribing, they canrequest and get a response.

    rosservice - list   List services
               - call   call service with args
               - type   type of service
               - find   find services by type
               - uri    print ROSRPC uri

Use *rosservice list* to show the services that are available.

    rosservice list

Use *rosservice type [service]* to show the type of service that is available. In the
case below the service takes no arguments. That is, no data sent or received
during request or response

    rosservice type    rosservice type /clear      returns std_srvs/Empty

Use *rosservice call [service] [args]* to call a service

    rosservice call /clear  In turtle sim, this clears the screen.

Use *rossrv show* the same way that you would use *rosmsg show*.

    rosservice type /spawn | rossrv show    Shows inputs of /spawn

    output:
    float32 x
    float32 y
    float32 theta
    string name
    ---
    string name     <== optional

Calling the spawn service no name. Still need an empty string though. Returns
*name: "turtle2"*. 

    rosservice call /spawn 2 2 0.2 ""

### Using rosparam
Use *rosparam [args]* to store and manipulate data on the ROS parameter server.
The parameter service can store data of typical types. An example would be the
background color of the turtle sim. 
    
    rosparam set    set parameter
    rosparam get    get parameter
    rosparam load   load parameters from file 
    rosparam dump   dump parameters to file
    rosparam delete delete parameter
    rosparam list   list parameter names

#### rosparam list

    rosparam list   show parameters

#### rosparam set and get
Set background color
    
    rosparam set /background_r 150  

Need to update the simulator to see effects

    rosservice call /clear

Get background color
    
    rosservice get /background_g

Get all contents of parameter server

    rosservice get /

#### rosparam dump and load
Use *rosparam [dump/load] [file_name] [namespace]*. To dump the parameters to a
file.

    rosparam dump params.yaml   Will dump to 'params.yaml'

Load these parameters into a new namespace - i.e. copy.
    
    rosparam load params.yaml copy
    rosparam get /copy/background_b


*end of service and params*


#### Using rqt_console and roslaunch
rqt_console and rqt_logger_level can be used to aid in debugging. Use roslaunch
for starting many nodes at once

rqt_console displays output from nodes while rqt_logger_level lets us decide
what level of messages we want to see. DEBUG, WARN, INFO, ERROR. 

Will start by looking at the turtlesim nodes. First, run console and logger
    
    rosrun rqt_console rqt_console
    rosrun rqt_logger_level rqt_logger_level

From here can change many options. Can show the severity of the output messages
and change which message you see.











=========================================================================
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
