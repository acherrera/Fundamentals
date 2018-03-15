# Commands relating to editing / moving / copying disks


# List all the disks attached

Use this command to see all the memory devices attached to computer

    sudo fdisk -l

# Copy paritions to new drive/location

CAREFUL - this command doesn't care about your data. If you mess up 'if' and
'of', it will ruin everything. It just doesn't care

    sudo dd if='dev/sda' of='/dev/sdb' -status=progress

Note that 'sda' and 'sdb' should be the drive associated with the the input and
output. *if* is what you want to copy *of* is where you want to copy to.


# Test hard disk speed

Use this to see how fast your hard drive is working. Useful for diagnosing slow
computers. I.E. Seeing if you should buy an SSD. 

    sudo hdparm -Tt /dev/sda

Where sda is the drive to test
