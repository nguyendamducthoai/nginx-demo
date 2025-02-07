# Use the official NGINX base image
FROM nginx:latest

# Remove default NGINX config
RUN rm /etc/nginx/nginx.conf

# Copy custom NGINX configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Create the directory for serving JSON files
RUN mkdir -p /usr/share/nginx/html

# Copy JSON response file into the container
COPY response.json /usr/share/nginx/html/response.json

# Expose port 80
EXPOSE 80

# Start NGINX
CMD ["nginx", "-g", "daemon off;"]