resource "aws_dynamodb_table" "basic-dynamodb-table" {
  name              = "task5_dynamodb"
  billing_mode      = "PROVISIONED"
  read_capacity     = 5
  write_capacity    = 5
  hash_key          = "file_name"

  attribute {
    name = "file_name"
    type = "S"
  }

  tags = {
    Name        = "dynamodb-table-1"
    Environment = "production"
  }
}