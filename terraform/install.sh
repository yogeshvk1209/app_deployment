#!/bin/sh
systemctl enable docker
systemctl start docker
docker run -dit -p 8080:8080 yogeshvk1209/demoapp3
