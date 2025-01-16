MAIN=src/main.py
DISTPATH=bin
EXEC=tstr
COMPILER=pyinstaller
CFLAGS=--onefile --distpath=$(DISTPATH) --name=$(EXEC) $(MAIN)

compile:
	$(COMPILER) $(CFLAGS)
