# Meta Workspace: Bootstrap (`ikwf-history-website` project)

This is the bottom of the stack of turtles. All other Terraform workspaces
assume there is a GCP resource available:

- The `ikwf-history-terraform-states` GCS bucket for storing Terraform state
  and locks

This workspace brings these up as the bare minimum to create all other
resources.
