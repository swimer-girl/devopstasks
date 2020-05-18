resource "aws_s3_bucket" "b" {
  bucket = "devops-bagrova-mybucket"
  acl    = "private"

  tags = {
    Name        = "My bucket for task 4"
    Environment = "Dev"
  }
}