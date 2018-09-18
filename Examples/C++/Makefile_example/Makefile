# Excrutiatingly simple Makefile. Good starting point before looking
# and digging around in the filestructure make file.

# Each section defines how to the specified part. Will run down through
# linked sections when call. I.E. the RUNME will runn through the 
# other main.o, Mother.o, Daughter.o to make the .exe



all: RUNME clean

RUNME: main.o Daughter.o Mother.o
	g++ main.o Mother.o Daughter.o -o RUNME

main.o: main.cpp
	g++ -c main.cpp

Mother.o: Mother.cpp Mother.h
	g++ -c Mother.cpp Mother.h

Daughter.o: Daughter.cpp Daughter.h
	g++ -c Daughter.cpp Daughter.h

clean:
	rm *.o *.gch

# General format - indents are important
# target:dependancies
# 	actions
