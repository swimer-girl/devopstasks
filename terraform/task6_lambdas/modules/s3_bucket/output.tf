output "bucket_ids" {
  description = "bucket_id"
  value = element(concat(aws_s3_bucket.b.*.id, [""]), 0)
}