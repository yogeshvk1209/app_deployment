# Demo app deployment

Demo Python web app creation, dockerization and deployment on AWS. Using terraform for AWS resources creation and Nginx (installed and configured on EC2, as part of terraform) for High availability and  Load balancing.


#  The app

Demo Python web app created using

  - flask module
  - flask serves a simple index.html
  - Updated for Python3

### Docker Image
For simplicity, compatibility and maintainability, we can dockerize the app.

 - Lightweight - Built directly from python:3.9-slim 
 - Tried and tested on ARM64 platforms
  - Create docker image by running below command
```sh
$ cd sampleapp
$ docker build -t demoapp .
```
  - App is managed and run  as non-root user inside the docker
  - One can skip this step if required and use already Created and pushed image from dockerhub (Image name: yogeshvk1209/pywebapp2025). Image has port exposed on 8080

#  The Deployment

Terraform docker setup.
  - Terraform docker setup Auto-Scaling groups with launch template and ALB frontend
  - AMI being used is Alinux2023 ARM64.
  - Outputs ALB Public DNS name
  - To access webapp, use URL http://<ALB_Public_dns>
  - Docker nodes can run multiple dockers at different port and nginx can be made to point them.
  - Working with provider.aws = 5.90.0 and Terraform = 1.12.xx

To run as is, run below commands

```sh
$ cd terraform
$ terraform init
$ terraform plan
$ terraform apply
```
