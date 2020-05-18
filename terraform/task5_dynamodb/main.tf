provider "aws" {
  region = "us-east-1"
}

module "dynamodb" {
  source = "./modules/dynamodb"
}

terraform {
  backend "s3" {
    bucket = "devops-bagrova-mybucket"
    key    = "task5_dynamodb/terraform.tfstate"
    region = "us-east-1"
  }
}