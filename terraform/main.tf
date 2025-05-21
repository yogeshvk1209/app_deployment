################ Configure the AWS provider ##########################
provider "aws" {
  region = "us-west-2"
}

########################## terraform #################################
terraform {
  required_providers {
    aws = "~> 5.90.0"
  }
  required_version = "= 1.12.0"
}
########################## terraform #################################
