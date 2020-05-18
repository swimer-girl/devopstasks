provider "aws" {
  region = "us-east-1"
}

module "s3_bucket" {
  source = "./modules/s3_bucket"
}

terraform {
  backend "s3" {
    bucket = "devops-bagrova-mybucket"
    key    = "task4_s3_bucket/terraform.tfstate"
    region = "us-east-1"
  }
}