# Use the official Nginx image as the base
FROM nginx:latest
 
# Copy your custom nginx configuration file (optional)
COPY nginx.conf /etc/nginx/nginx.conf
 
# Copy your custom website files (optional)
COPY html /usr/share/nginx/html