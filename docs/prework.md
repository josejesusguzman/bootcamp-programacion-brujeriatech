# Prework
En este modulo se abarca la instalación y configuración de las herramientas necesarias, para trabajar en el curso, teniendo en cuenta los tres Sistemas Operativos comerciales. 

Estos son los enlaces e instrucciones para cada herramienta:
- Git --> https://git-scm.com/downloads

  <details>
  <summary>Windows</summary>

  1 Descargar el ejecutable en su ultima versión

  2 Seguir las instrucciones y configuración por defecto

  3 Abrir una terminal de CMD 

  4 Verificar la instalación
  ```
  git --version
  ```
  </details>
  
  
  <details>
  <summary>Linux</summary>
  
  1 Abrir una terminal
  
  2 Colocar el comando segun la distribución

  Para distribuciones basadas en debian
  ```
  apt-get install git
  ```
  
  Para otras distribuciones
  ```
  yum install git
  ```
  
  3 Verificar instalación
  ```
  git --version
  ```
  </details>
  
  
  <details>
  <summary>Mac</summary>

  1 Abrir una terminal

  2 Colocar el comando
  ```
  brew install git
  ```

  3 Verificar instalación
  ```
  git --version
  ```
  </details>

- VS Code --> https://code.visualstudio.com/download

  <details>
  <summary>Windows</summary>

    Microsoft Store

     1 Abrir la Microsoft Store

     2 Buscar visual studio code

     3 Instalar
     
     Ejecutable
     
     1 Descargar el ejecutable en su ultima versión

     2 Seguir las instrucciones y configuración por defecto
    
  </details>
  
  
  <details>
  <summary>Linux</summary>

  1 Descargar el .deb
 

  2 Abrir una terminal
  
  3 colocar el comando 
  ```
  sudo apt install ./nombrearchivo
  ```
  </details>
  
  
  <details>
  <summary>Mac</summary>

  1 Abrir una terminal

  2 Colocar el comando
  ```
  brew install --cask visual-studio-code
  ```
  </details>

- Python --> desde Microsoft store o https://www.python.org/downloads/

  <details>
  <summary>Windows</summary>

    Microsoft Store

     1 Abrir la Microsoft Store

     2 Buscar Python
     
     3 Elegir la versión

     3 Instalar
     
     Ejecutable
     
     1 Descargar el ejecutable en su ultima versión

     2 Seguir las instrucciones y configuración por defecto
     
     > Importante: Verificar la casilla para agregar el Path a las variables de entorno del sistema
     
     Para verificar la instalación
     ```
     python --version
     ```
    
  </details>
  
  
  <details>
  <summary>Linux</summary>

  1 Abrir una terminal

  2 Colocar el comando
  ```
  sudo apt-get install git
  ```

  3 Verificar la instalación
  ```
  git --version
  ```
  </details>
  
  
  <details>
  <summary>Mac</summary>

  1 Descargar la ultima versión

  2 Abrir el archivo .pkg y seguir las instrucciones
  
  3 Verificar la instalación
  ```
  python --version
  ```
  </details>

- PSeInt --> https://pseint.sourceforge.net/?page=descargas.php

> Para cada Sistema Operativo seguir las instrccuines del sitio web

- Node --> https://nodejs.org/es/download/

  <details>
  <summary>Windows</summary>
     
     1 Descargar el ejecutable en su ultima versión (LTS)

     2 Seguir las instrucciones y configuración por defecto
     
     > Opcional: Verificar la casilla para instalar chocolatey
     
     3 Para verificar la instalación
     ```
     node --version
     ```
    
  </details>
  
  
  <details>
  <summary>Linux</summary>

  1 Abrir una terminal

  2 Para instalar node
  ```
  sudo apt install nodejs -y
  ```

  3 Para instalar npm
  ```
  sudo apt install npm -y
  ```
  
  4 Para verifivar node
  ```
  nodejs --version
  ```
  
  5 Para verificar npm
  ```
  npm --version
  ```
  </details>
  
  
  <details>
  <summary>Mac</summary>

  1 Abrir una terminal

  2Colocar el comando
  ```
  brew install node
  ```
  </details>
  
- MongoDB --> https://www.mongodb.com/try/download/community
  <details>
  <summary>Windows</summary>
     
     1 Descargar el ejecutable en su ultima versión (LTS)

     2 Seguir las instrucciones y configuración por defect
    
  </details>
  
  
  <details>
  <summary>Linux</summary>

  1 Abrir una terminal

  2Colocar el comando
  ```
  sudo apt-get install -y mongodb-org
  ```
  </details>
  
  
  <details>
  <summary>Mac</summary>
  
  mongodb community server

  1 descargar el archivo .pkg
  
  2 Ingresar a la carpeta bin
  
  3 Doble clic en 
  
  - install compass
  - mongodb
  - mongos
  
  community edition
  

  1 Colocar el comando para descarga
  ```
  brew tap mongodb/brew
  ```
  
  2 Actualizar homebrew
  ```
  brew update
  ```
  
  3 Instalar mongodb
  ```
  brew install mongodb-community@6.0
  ```
  
  </details>

- MySQL Server --> https://dev.mysql.com/downloads/mysql/

  <details>
    <summary>Windows</summary>

     1Descargar el ejecutable en su ultima versión

     2 Seguir las instrucciones

     > Nota: se pedira crear las credenciales del server, guardarlas para conectarse despues

    </details>


    <details>
    <summary>Linux</summary>

    1 Descargar el archivo .deb

    2 cd Downloads

    3 Colocar los comandos
    ``` 	
    sudo apt install -y wget
    sudo apt install ./nombre archivo .deb
    ```
    </details>


    <details>
    <summary>Mac</summary>

    mongodb community server

    2 Abrir una terminal

    1 Colocar el comando para descarga
    ```
    brew install mysql
    ```

    2 Actualizar homebrew

    </details>

- MySQL Workbench --> https://www.mysql.com/products/workbench/

  <details>
    <summary>Windows</summary>

     1Descargar el ejecutable en su ultima versión

     2 Seguir las instrucciones

    </details>

- MySQL Installer --> https://dev.mysql.com/downloads/installer/

> Este instalador sirve para instalar el server y workbench 

- Azure CLI --> https://learn.microsoft.com/en-us/cli/azure/install-azure-cli

  <details>
    <summary>Windows</summary>

     1 Descargar el ejecutable en su ultima versión

     2 seguir instrucciones

     3 Abrir un CMD

     2 Para verificar
    ```
    az
    ```  
    </details>


    <details>
    <summary>Linux</summary>

    1 Escoger el archivo conforme a la distribución

    2 Seguir instrucciones del sitio web

    2 Para verificar
    ```
    az
    ```

    > Nota: si no se instalo, aparace una pregunta para poder hacerlo, introducir y/Y.
    </details>


    <details>
    <summary>Mac</summary> 

    1 Colocar el comando para descarga y actualización de homebrew
    ```
    brew update && brew install azure-cli
    ```

    2 Si pide reinstalar
    ```
    brew reinstall azure-cli
    ```

    </details>
  
    Para iniciar sesión en Azure colocar
    ```
    az login
    ```
  
  Se abrirar una pestaña de tu navegador iniciar sesión en tu cuenta de Azure y estara terminado el proceso

- Docker --> https://www.docker.com/products/docker-desktop/
   <details>
    <summary>Windows</summary>

       1 Descargar el ejecutable en su ultima versión (LTS)

       2 Seguir las instrucciones

       3 Ejecutar docker

       > Nota: es caso de pedir el WSL, introducir en una terminal de CDM wsl --update

    </details>


    <details>
    <summary>Linux</summary>

    1 Abrir una terminal

    2 Colocar el comando
    ```
    sudo apt install -y docker.io
    ```
    </details>


    <details>
    <summary>Mac</summary>

    1 Seguir las instrucciones del sitio web

    </details>

Cabe aclarar que las instrucciones para Linux son para distribuciones basadas en debian; en caso de tener una diferente siga las instrucciones que vienen en cada sitio web

## Homebrew

Para los usuarios Mac instalar Homebrew con el siguiente comando
 ```
 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```

## Virtualización

Si tienes Windows y quieres trabajar en Linux, puede virtualizar Kali Linux con los siguientes recursos.

- VirtualBox --> https://www.virtualbox.org/wiki/Downloads
- Kali Linux --> https://www.kali.org/get-kali/
- Curso Udemy: Kali Linux. Instalación, comandos y practica de herramientas --> https://tinyurl.com/2lvtr5qn

### ¿Porque Kali Linux?
Tiene la ventaja de tener instaladas mas herramientas que en otras distribuciones, por lo que solo tendras que actualizarlas.

## Extensiones para VSCode:

| Nombre | URL |
| --------- |-------|
|Microsoft Edge Tools for VS Code| <a href="https://marketplace.visualstudio.com/items?itemName=ms-edgedevtools.vscode-edge-devtools"><img src="https://tinyurl.com/2zzjkdbv" witdth="70px" height="70px"></a> |
|Docker| <a href="https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker"><img src="https://tinyurl.com/2meg2qg2" witdth="70px" height="70px"></a> |
|Error Lens| <a href="https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens"><img src="https://tinyurl.com/2hsh4cpr" witdth="70px" height="70px"></a> |
|Code GPT| <a href="https://marketplace.visualstudio.com/items?itemName=DanielSanMedium.dscodegpt"><img src="https://tinyurl.com/2js5yvwe" witdth="70px" height="70px"></a> |
|ES7+ React/Redux/React-Native snippets| <a href="https://marketplace.visualstudio.com/items?itemName=dsznajder.es7-react-js-snippets"><img src="https://tinyurl.com/2jkdhfom" witdth="70px" height="70px"></a> |
|ESLint| <a href="https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint"><img src="https://tinyurl.com/2fb3pckc" witdth="70px" height="70px"></a> |
|GitHub Pull Requests and Issues| <a href="https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github"><img src="https://tinyurl.com/2zud7nqd" witdth="70px" height="70px"></a> |
|indent-rainbow| <a href="https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow"><img src="https://tinyurl.com/2ll4cdut" witdth="70px" height="70px"></a> |
|isort| <a href="https://marketplace.visualstudio.com/items?itemName=ms-python.isort"><img src="https://tinyurl.com/2jz45y8b" witdth="70px" height="70px"></a> |
|IntelliCode| <a href="https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode"><img src="https://tinyurl.com/2k368jnj" witdth="70px" height="70px"></a> |
|Jupyter| <a href="https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter"><img src="https://tinyurl.com/2ml2lf2f" witdth="70px" height="70px"></a> |
|JavaScript and TypeScript Nightly| <a href="https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-typescript-next"><img src="https://tinyurl.com/2puxjnwy" witdth="70px" height="70px"></a> |
|Polacode| <a href="https://marketplace.visualstudio.com/items?itemName=pnp.polacode"><img src="https://tinyurl.com/2kxs3qf6" witdth="70px" height="70px"></a> |
|Pylance| <a href="https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance"><img src="https://tinyurl.com/2fzrj5gu" witdth="70px" height="70px"></a> |
|Python| <a href="https://marketplace.visualstudio.com/items?itemName=ms-python.python"><img src="https://tinyurl.com/2m7ukkgf" witdth="70px" height="70px"></a> |
|Stream Deck for Visual Studio Code| <a href="https://marketplace.visualstudio.com/items?itemName=nicollasr.vscode-streamdeck"><img src="https://tinyurl.com/2zr9nsur" witdth="70px" height="70px"></a> |
|vscode-pets| <a href="https://marketplace.visualstudio.com/items?itemName=tonybaloney.vscode-pets"><img src="https://tinyurl.com/2otyb54o" witdth="70px" height="70px"></a> |
|WSL| <a href="(https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl"><img src="https://tinyurl.com/2fduxyx7" witdth="70px" height="70px"></a> |
