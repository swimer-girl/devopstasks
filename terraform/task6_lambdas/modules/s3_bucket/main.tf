resource "aws_s3_bucket" "b" {
  bucket = "devops-bagrova-mybucket-task6"
  acl    = "private"

  tags = {
    Name        = "My bucket for task 6"
    Environment = "Dev"
  }
}