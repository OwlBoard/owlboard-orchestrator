# api_gateway/Dockerfile

# Usar una imagen de Nginx ligera y moderna
FROM nginx:1.27-alpine

# Eliminar la configuración por defecto
RUN rm /etc/nginx/conf.d/default.conf

# Copiar nuestra configuración personalizada
COPY nginx.conf /etc/nginx/conf.d/default.conf