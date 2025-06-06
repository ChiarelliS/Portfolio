# variables.tf
variable "project" {
  description = "GCP project ID"
  type        = string
}

variable "region" {
  description = "GCP region"
  type        = string
  default     = "europe-west10"
}

variable "zone" {
  description = "GCP zone"
  type        = string
  default     = "europe-west10"
}
