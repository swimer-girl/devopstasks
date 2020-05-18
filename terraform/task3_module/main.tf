provider "aws" {
  region = "us-east-1"
}

module "lambda" {
  source = "./modules/lambda"
}

terraform {
  backend "s3" {
    bucket = "devops-bagrova-mybucket"
    key    = "task3_module/terraform.tfstate"
    region = "us-east-1"
  }
}