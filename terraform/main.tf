# terraform/main.tf

terraform {
  required_version = ">= 1.13.0"
  required_providers {
    local = {
      source = "hashicorp/local"
    }
    random = {
      source = "hashicorp/random"
    }
  }
}

provider "local" {}

# Simulate a project in Bitbucket
resource "local_file" "bitbucket_project" {
  filename = "tmp/bitbucket_project_${random_id.suffix.hex}.json"
  content = jsonencode({
    workspace  = var.workspace_name
    key        = var.project_key
    name       = var.project_name
    is_private = true
  })
}

# Simulate a repository
resource "local_file" "bitbucket_repo" {
  filename = "tmp/bitbucket_repo_${random_id.suffix.hex}.json"
  content = jsonencode({
    workspace   = var.workspace_name
    repo_slug   = var.repo_slug
    project_key = local_file.bitbucket_project.content
    is_private  = true
    scm         = "git"
  })
}

# Generate a random suffix to simulate uniqueness
resource "random_id" "suffix" {
  byte_length = 4
}
