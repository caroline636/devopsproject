output "droplet_ip" {
  description = "The public IP address of the Droplet"
  value       = digitalocean_droplet.web.ipv4_address
}

output "droplet_id" {
  description = "The ID of the Droplet"
  value       = digitalocean_droplet.web.id
}

output "droplet_name" {
  description = "The name of the Droplet"
  value       = digitalocean_droplet.web.name
}
