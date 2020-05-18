# put variables here
variable memorysize {
  description = "Memory Size"
  default     = "131"
}
variable runtime {
  description = "Python's version"
  default     = "python2.7"
}
variable timeout {
  description = "TimeOut"
  default     = "120"
}
variable schedule_start {
  description = "Time to start"
  default     = "cron(30 * ? * * *)"
}
variable schedule_stop {
  description = "Time to stop"
  default     = "cron(59 * ? * * *)"
}
