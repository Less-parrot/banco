# Archivo makefile para correr el script de github.

run:
	find $HOME -name "github.sh" -execdir sh -c 'echo "Ejecutando {}"; chmod +x {}; {}' \;
clean:
	rm -rf .git
	
all:
	run clean
