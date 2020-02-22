output "nginx_dns_name" {
  value = aws_instance.nginx.public_dns
}
output "Worker-node1_Private_IP" {
  value = aws_instance.server1.private_ip
}
output "Worker-node22_Private_IP" {
  value = aws_instance.server2.private_ip
}
