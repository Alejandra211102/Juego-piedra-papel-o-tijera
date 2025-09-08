# Imagen base de Node.js
FROM node:14

# Crear directorio de la app dentro del contenedor
WORKDIR /usr/src/app

# Copiar package.json y package-lock.json
COPY package*.json ./

# Instalar dependencias
RUN npm install

# Copiar todo el resto de los archivos del proyecto
COPY . .

# Exponer el puerto (el que use tu servidor, supongamos 8080)
EXPOSE 8080

# Comando para arrancar la app
CMD ["node", "app.js"]

