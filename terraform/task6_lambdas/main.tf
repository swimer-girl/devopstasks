provider "aws" {
  region = "us-east-1"
}

module "lambdas" {
  source = "./modules/lambdas"
}

terraform {
  backend "s3" {
    bucket = "devops-bagrova-mybucket"
    key    = "task6_lambdas/terraform.tfstate"
    region = "us-east-1"
  }
}