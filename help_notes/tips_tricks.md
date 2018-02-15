# Here I'm going to try and put in some helpful tips and tricks for various
things that I do.


Time Lapse creation

    ffmpeg -r 30 -start_number 0329 -i FILE%04d.JPG -s 1280x720 -vcodec libx264 new_file.mp4 

        -r 30               frame rate
        -start_number       file number to start at (assumes sequential)
        -i                  input format. Here FILE0000-FILE9999
        -s                  size of output
        -vcodec             I would assume codec type. libx264 is ?? 
        new_file.mp4        Output file name




Tar commands

    Compressing a directory
        tar -czvf archive_name.tar.gz path/to/directory/name
            -c  create archive
            -z  compress with gzip
            -v  verbose: show the output
            -f  file name is specified


    Extracting a directory
        tar -xvf path/to/directory
            -x  extract directory
            -v  verbose: show the output
            -f  specify the name
            

