# Juego Piedra, Papel o Tijera ✊✋✌️ — README
[![js_test](https://github.com/Alejandra211102/Juego-piedra-papel-o-tijera/actions/workflows/Javascript.yml/badge.svg)](https://github.com/Alejandra211102/Juego-piedra-papel-o-tijera/actions/workflows/Javascript.yml)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)


Proyecto web estático (HTML/CSS/JS) con despliegue en GitHub y AWS EC2 (Nginx)

---

## 📌 Descripción de la aplicación

Juego de **Piedra, Papel o Tijera** contra la computadora, con interfaz gráfica simple, marcador (victorias/derrotas/empates) y botón de reinicio. No requiere backend: se desarrolla íntegramente en el navegador.

**Características principales**

* Interfaz responsive y ligera.
* Lógica en JavaScript puro.
* Despliegue: GitHub Pages
* Servidor: EC2 con Nginx.

---

## 🛠️ Tecnologías utilizadas

* **HTML5**: estructura de la interfaz.
* **CSS3**: estilos y layout.
* **JavaScript**: lógica del juego y manejo del DOM.
* **Nginx** (para EC2): servidor web estático.
* **Git & GitHub**: control de versiones y hosting estático.
* **AWS EC2**: hosting en servidor propio (Ubuntu 22.04 LTS sugerido).
* Node.js + Express: Para las pruebas automáticas con supertest.
* Jest: Framework para pruebas unitarias.
* GitHub Actions: Para la integración continua y validación automática con ESLint.

---

## 🌍 URL de la aplicación desplegada

* **GitHub Pages**: `https://github.com/Alejandra211102/Juego-piedra-papel-o-tijera.git`
* **EC2 (HTTP)**: `http://3.82.27.207/`
  
---

## 🧭 Paso a paso completo del despliegue

### A) Publicar en GitHub

1. Crea el repositorio **público** en GitHub (ej: `Juego-piedra-papel-o-tijera`).
2. En tu carpeta del proyecto (con `index.html`, `style.css`, `script.js`):

   ```bash
   git init
   git add .
   git commit -m "Primer commit - juego piedra papel tijera"
   git branch -M main
   git remote add origin https://github.com/Alejandra211102/Juego-piedra-papel-o-tijera.git
   git push -u origin main
   ```
3. Abre la URL que aparece (puede tardar 1–2 minutos en estar activa).

---
### B) Desplegar en AWS EC2 con Nginx (Ubuntu 22.04)

**1) Crear y conectar a la instancia**

* AMI: *Ubuntu Server 22.04 LTS*.
* Tipo: `t2.micro`/`t3.micro`.
* Disco: 8–10 GB gp3 (suficiente.
* Security Group: abrir **80/TCP** (HTTP) a Internet, **22/TCP** (SSH) idealmente solo tu IP.

Conéctate por SSH desde tu PC:

```bash
ssh -i llave-juego-ec2.pem ubuntu@3.82.27.207

**2) Instalar Nginx y Git**

```bash
sudo apt update
sudo apt install -y nginx git
sudo systemctl enable nginx
sudo systemctl start nginx
```

**Clonar desde GitHub** :

  ```bash
  git clone https://github.com/Alejandra211102/Juego-piedra-papel-o-tijera.git
  ```

**3) Publicar con Nginx**

```bash
sudo rm -rf /var/www/html/*
sudo cp -r Juego-piedra-papel-o-tijera/* /var/www/html/
```

**4) Probar**

* Navega a http://3.82.27.207/ y verifica que cargue el juego.

---

## 🧰 Comandos exactos utilizados

```bash
# Subir rama (primer push)
git init
git add .
git commit -m "Primer commit - juego piedra papel tijera"
git branch -M main
git remote add origin https://github.com/Alejandra211102/Juego-piedra-papel-o-tijera.git
git push -u origin main

# Resolver rechazo por historial distinto (si aparece)
git pull origin main --allow-unrelated-histories
git add .
git commit -m "Merge inicial y subida del proyecto"
git push origin main

# EC2 (Ubuntu): instalar y publicar
sudo apt update && sudo apt install -y nginx git
sudo systemctl enable nginx && sudo systemctl start nginx
git clone https://github.com/Alejandra211102/Juego-piedra-papel-o-tijera.git
sudo rm -rf /var/www/html/*
sudo cp -r Juego-piedra-papel-o-tijera/* /var/www/html/
sudo systemctl restart nginx
```

---

## ☁️ Configuraciones de AWS

**Instancia**

* AMI: *Ubuntu Server 22.04 LTS*.
* Tipo: `t2.micro` o `t3.micro`.
* Almacenamiento: 8–10 GB gp3.
* Par de claves: `mi-llave.pem` (descárgala 1 vez y guárdala).

**Security Group (Inbound)**

* **HTTP (80/TCP)**: `0.0.0.0/0` (público).
* **SSH (22/TCP)**: tu IP (recomendado) o `0.0.0.0/0` solo para pruebas.

---

## ✅ Verificación del funcionamiento

* **Local**: abrir `index.html` y probar botones.
* **GitHub Pages**: URL pública responde con el juego.
* **EC2**:

  * `systemctl status nginx` muestra `active (running)`.
  * `curl -I http://3.82.27.207/ devuelve `HTTP/1.1 200 OK`.
  * Navegador carga el juego y actualiza puntajes al hacer clic.

---
## 🧩 Problemas y soluciones encontrados durante el despliegue

1. **Página en blanco** al abrir `index.html`.
** Soluciòn:** 
* Unificar estructura simple `index.html`, `style.css`, `script.js` y enlazar script al final del `<body>`.
  
2. **JS de Node (`readline`)** no funciona en navegador.
 ** Soluciòn:**
   Mi app estaba en python sin con funcionamiento por consola, tuve que hacer la migración de lógica de **Node (readline)** a **DOM Events** en navegador.

4. **Archivos del visual y el repositorio no tenian los mismos archivos
** Soluciòn:**
*Abri nuevamente en el visual
*Se deben ejecutar los siguientes códigos:

git init
git remote add origin https://github.com/usuario/repositorio.git
git branch -M main
git pull origin main


5. **Nginx muestra default**: archivos no copiados a `/var/www/html`.
** Soluciòn:** 
* Unificar estructura simple `index.html`, `style.css`, `script.js` y enlazar script al final del `<body>`.
* Copiar a `/var/www/html` y **reiniciar Nginx**.
* Abrir **puerto 80** en Security Group y verificar `systemctl status nginx`.

## Github Actions
## Proceso para configurar GitHub Actions

1. Configurar workflow en GitHub Actions

En tu repositorio de GitHub, creaste un workflow para ejecutar ESLint en cada push o pull request.

Para eso, agregaste un archivo YAML en .github/workflows/js_test.yml (o similar).

Por ejemplo, un workflow básico para ESLint:

`name: ESLint Check`
`on: [push, pull_request]`
`jobs:`
`lint:`

    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v2

      - name: Set up Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '16'

      - name: Install dependencies
        run: npm install

      - name: Run ESLint
        run: npm run lint`

Esto configura que GitHub Actions ejecute ESLint en cada cambio.

2. Comandos usados en local

Para inicializar ESLint y crear configuración:

`npx eslint --init`
Modificar el package.json para que el script test use ESLint:

`"scripts": {
  "lint": "eslint .",
  "test": "npm run lint"
}`

## 🧩 Problemas y soluciones encontrados durante el despliegue

### 1️⃣ Problema: Error en GitHub Actions (Badge "failing")  
**Descripción:** El badge aparecía en estado `failing` porque no existía un archivo de configuración de ESLint y el linting fallaba.  

**Solución:**  

Se generó el archivo `.eslintrc.json` con:  

bash

`npx eslint --init`

2️⃣ Problema: Error al ejecutar npm test sin tests definidos

Descripción:
Al ejecutar npm test, aparecía el siguiente error:

Error: no test specified

El error sucedía en el script test ya que en package.json no estaba configurado correctamente.
✔️ Solución:
Se modificó el script para ejecutar ESLint como prueba:

`"scripts": {
  "lint": "eslint .",
  "test": "npm run lint"`
}

3️⃣ Problema: Badge mostraba "failing" después de corregir errores

Descripción:
Aunque los errores ya se habían corregido, el badge seguía mostrando el estado como "failing".

✔️ Solución:
Se esperó la actualización automática de GitHub Actions. En caso de persistir, se puede reiniciar manualmente desde:

`GitHub → Actions → Re-run jobs`

✅ Estado actual:
El badge ahora refleja correctamente el estado actualizado del workflow.

4️⃣ Problema: Badge mostraba "failing" aunque los tests pasaban

Descripción:
El badge indicaba un estado incorrecto, a pesar de que los logs no contenían errores.

Causa:
La URL del badge en el README.md estaba mal configurada (por ejemplo, apuntaba a otro archivo de workflow o a una rama incorrecta).

✔️ Solución:
Se generó el badge correcto desde:

`GitHub → Actions → Create status badge`

Y se reemplazó la URL del badge en el README.md.

✅ Estado actual:
El badge refleja correctamente el estado real del workflow.

## 💡 Consejos y mejores prácticas aprendidas

* Mantener proyectos estáticos **sin dependencias** para despliegue rápido.
* Enlazar JS **al final del `body`** para asegurar que el DOM esté listo.
* Proteger SSH (22/TCP) a tu IP; cerrar cuando no se use.
* Nombrar carpetas/repos **sin espacios** y en minúsculas.
* Usar `curl -I` y `systemctl status` para diagnosticar rápido.

---
