#!/bin/bash
yum update -y
yum install docker -y
systemctl start docker
systemctl enable docker
usermod -aG docker ec2-user
docker run -d -p 8080:8080 yogeshvk1209/pywebapp2025:latest
