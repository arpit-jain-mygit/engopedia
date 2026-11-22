variable "region" {
  description = "AWS region for every resource except the CloudFront certificate scope (none needed here)."
  type        = string
  default     = "ap-south-1"
}

variable "project" {
  description = "Short name used in resource names."
  type        = string
  default     = "word-wizard"
}

variable "environment" {
  description = "Environment name. One environment for now."
  type        = string
  default     = "dev"
}

variable "lambda_zip_path" {
  description = "Path to the backend zip built by scripts/build_lambda.sh."
  type        = string
  default     = "../backend/build/lambda.zip"
}

variable "frontend_dist_path" {
  description = "Folder with the built Angular app (ng build output)."
  type        = string
  default     = "../frontend/dist/word-wizard-web/browser"
}
