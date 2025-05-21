########################## Get latest AMI ##########################
data "aws_ami" "lt_ami" {
  most_recent = true
  owners      = ["amazon"]
  filter {
    name   = "architecture"
    values = ["arm64"]
  }
  filter {
    name   = "name"
    values = ["al2023-ami-2023*"]
  }
}

##################### Auto Scaling Group ##########################
resource "aws_autoscaling_group" "flask_app" {
  name                = "flask-app-asg"
  max_size            = 1
  min_size            = 1
  desired_capacity    = 1
  target_group_arns   = [aws_lb_target_group.flask_app.arn]
  vpc_zone_identifier = aws_subnet.public[*].id

  launch_template {
    id      = aws_launch_template.flask_app.id
    version = "$Latest"
  }

  tag {
    key                 = "Name"
    value               = "flask-app-asg"
    propagate_at_launch = true
  }
}

#################### Launch Template ##########################
resource "aws_launch_template" "flask_app" {
  name          = "flask-app-launch-template"
  image_id      = data.aws_ami.lt_ami.id
  instance_type = "t4g.micro"

  instance_market_options {
    market_type = "spot"
    spot_options {
      max_price                      = "0.003" # Max price for t4g.micro (adjust based on region)
      spot_instance_type             = "one-time"
      instance_interruption_behavior = "terminate"
    }
  }

  network_interfaces {
    associate_public_ip_address = true
    security_groups            = [aws_security_group.ec2_sg.id]
  }
  
  key_name = "terrakey"
  user_data = filebase64("userdata.sh")
  
  tag_specifications {
    resource_type = "instance"
    tags = {
      Name = "flask-app-ec2"
    }
  }
}

