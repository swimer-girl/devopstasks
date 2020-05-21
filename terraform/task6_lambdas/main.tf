provider "aws" {
  region = "us-east-1"
}

module "s3_bucket" {
  source = "./modules/s3_bucket"
}

module "lambdas" {
  source = "./modules/lambdas"
  bucket_id = module.s3_bucket.bucket_ids
}

terraform {
  backend "s3" {
    bucket = "devops-bagrova-mybucket"
    key    = "task6_lambdas/terraform.tfstate"
    region = "us-east-1"
  }
}