#!/bin/bash

#[Opciones(De momento)]
# Un pequeño script para automatizar los pull requests y mantener 
# varias versiones de nuestro codigo.

#[Recordar]
# Hacer los atajos de teclado en bspwm para usarlo desde
# cualquier lado del sistema, sugiero meterlo en /bin.


function github () {
    
    ruta_actual=$(pwd)
    git init $ruta_actual  # Iniciador
    clear
    read -p "nombre de su rama: " nombreRama # Pedir el nombre que quiere para su rama.
    git checkout -b $nombreRama # usamos el nombre
    
    git add $ruta_actual
    read -p "escriba un mensaje sobre lo que actualizó en el repositorio: " mensaje
    echo ""
    echo "Agregando sus archivos"
    echo ""
    git commit -m "$mensaje"
    clear
    read -p "dame la url de el repositorio: " url
    git remote add origin $url #Mandamos a agregar el repositorio de forma remota, o algo asi 
    git push origin $nombreRama
    echo "Su nueva version de codigo se ha hecho correctamente!"


}


# Esta va ser la funcion que va ha llamar a todo el script.
function main() {
    github
}


if [[ -f /usr/bin/git ]]; then # Solo si esta instalado git, se va ejecutar la funcion main
    main

else
    echo "Instalando github"
    sudo apt install git    # si no esta instalo git se va a instalar.
    main
fi

# 04 abr 2023 12:01:13 ultima actualizacion: Funciona.