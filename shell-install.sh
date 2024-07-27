#!/bin/bash
 
# Update package lists
yum update -y
 
# Install Nginx
amazon-linux-extras install -y nginx1
 
# Start and enable Nginx service
systemctl start nginx
systemctl enable nginx
 
# Check Nginx status
systemctl status nginx
 
echo "Nginx installed and started successfully!"