# Demo app deployment

Demo Python web app creation, dockerization and deployment on AWS. Using terraform for AWS resources creation and Nginx (installed and configured on EC2, as part of terraform) for High availability and  Load balancing.


#  The app

Demo Python web app created using

  - flask module
  - wtforms
  - Validators in wtforms as well as pattern-matching in HTML

### Docker Image

For simplicity, compatibility and maintainability, we can dockerize the app.

  - Create docker image by running below command
```sh
$ cd sampleapp
$ docker build -t demoapp .
```
  - App is managed and run  as non-root user inside the docker

  - One can skip this step if required and use already Created and pushed image from dockerhub (Image name: yogeshvk1209/demoapp). Image has port exposed on 8080

#  The Deployment

Terraform docker setup.

  - Terraform docker setup using nginx LB at front.
  - Worker-nodes have port 8080 exposed only to internal VPC IPs and Nginx node has only 80 port exposed.
  - AMI being used in ECS-optimised Alinux2 (as this has most of docker and docker dependencies pre-installed).
  - IPs added to /etc/hosts file using provisioner 'remote-exec'. Updating nginx conf files through user data.
  - Outputs Docker nodes private IP and Nginx nodes Public DNS name
  - To access webapp, user URL <Nginx_Public_dns>/app1
  - Docker nodes can run multiple dockers at different port and nginx can be made to point them.
  - Working with provider.aws ~> 2.50 and TF > 12.xx

To run as is, run below commands

```sh
$ cd terraform
$ terraform init
$ terraform plan
$ terraform apply
```

