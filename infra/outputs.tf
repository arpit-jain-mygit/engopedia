output "app_url" {
  description = "Open this in a browser. Web app and API both live behind this URL."
  value       = "https://${aws_cloudfront_distribution.web.domain_name}"
}

output "api_url" {
  description = "Direct API Gateway URL (the app uses /api through CloudFront instead)."
  value       = aws_apigatewayv2_api.api.api_endpoint
}

output "table_name" {
  value = aws_dynamodb_table.game.name
}

output "web_bucket" {
  value = aws_s3_bucket.web.id
}

output "cloudfront_distribution_id" {
  value = aws_cloudfront_distribution.web.id
}
