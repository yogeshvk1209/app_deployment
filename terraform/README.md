# Terraform Docker Nginx

Terraform docker setup.

  - Terraform docker setup using nginx LB at front. 
  - Worker-nodes have port 8080 exposed only to internal VPC IPs and Nginx node has only 80 port exposed.
  - AMI being used in ECS-optimised Alinux2 (as this has most of docker and docker dependencies pre-installed).
  - IPs added to /etc/hosts file using provisioner 'remote-exec'. Updating nginx conf files through user data.
  - Outputs Docker nodes private IP and Nginx nodes Public DNS name
  - To access webapp, user URL <Nginx_Public_dns>/app1
  - Docker nodes can run multiple dockers at different port and nginx can be made to point them.
  - Working with provider.aws ~> 2.50 and TF > 12.xx

# Further Mod
Need to variablise Docker image input and this can be generalised to any image
