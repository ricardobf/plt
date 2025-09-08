output "project_file" {
  value = local_file.bitbucket_project.filename
}

output "repo_file" {
  value = local_file.bitbucket_repo.filename
}
