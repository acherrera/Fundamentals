
RUNME: main.o Daughter.o Mother.o
	g++ main.o Mother.o Daughter.o -o RUNME

main.o: main.cpp
	g++ -c main.cpp

Mother.o: Mother.cpp Mother.h
	g++ -c Mother.cpp Mother.h

Daughter.o: Daughter.cpp Daughter.h
	g++ -c Daughter.cpp Daughter.h

clean:
	rm *.o RUNME

# General format - indents are important
# target:dependancies
# 	actions
