
SHELL = /bin/bash
#MAC
LIBPATH += -L"/System/Library/Frameworks/OpenGL.framework/Libraries"
#MACLIBRARIES = -lGL -lGLU -lglut -lm -lobjc -lstdc++ trying to merge mac and linux libraries
#MACLIBRARIES = -lGL -lGLU -lm -lobjc -lstdc++  from an example makefile
FRAMEWORK = -framework GLUT
FRAMEWORK += -framework OpenGL 
#ENDMAC

#LINUX
LINUXLIBRARIES = -lGL -lglut -lGLU
#ENDLINUX

#COMMON
COMPILERFLAGS = -Wall -O3
CFLAGS = $(COMPILERFLAGS) 
CC = g++ 

EXE = mcviewer

SOURCES = element.cpp magchainglviewer.cpp
OBJECTS = $(SOURCES:.cpp=.o)

all:
	@echo ""
	@echo "PLEASE SELECT OS: make linux (or make mac)"
	@echo "exit"
	@echo ""

linux: $(SOURCES) $(OBJECTS) 
	$(CC) $(CFLAGS) -o $(EXE)-$@ $(OBJECTS) $(LINUXLIBRARIES)

mac: $(SOURCES) $(OBJECTS) 
	$(CC) $(FRAMEWORK) $(CFLAGS) -o $(EXE)-$@ $(LIBPATH) $(OBJECTS) $(LIBRARIES)

clean:
	rm $(OBJECTS)
.cpp.o:
	$(CC) $< -c -o $@
