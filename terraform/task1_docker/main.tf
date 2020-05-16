provider "docker" {
  host = "unix:///var/run/docker.sock"
}
resource "docker_image" "nginx" {
  name = var.nginx
}
resource "docker_image" "php-fpm" {
  name = var.php-fpm
}

resource "docker_network" "private_network"{
  name = var.network
}

resource "docker_container" "nginx-server" {
  name = "nginx-server"
  image = docker_image.nginx.latest
  ports {
    internal = 80
    external = 8080
  }
  networks_advanced {
    name = docker_network.private_network.name
  }
  upload {
    content = file("files/default.conf")
    file = "/etc/nginx/conf.d/default.conf"
  }
}

resource "docker_container" "php-fpm" {
  name = "php.epam"
  image = docker_image.php-fpm.latest
  hostname = "php.epam"
  networks_advanced {
    name = docker_network.private_network.name
  }
  upload {
    content = file("files/index.php")
    file = "/var/www/html/index.php"
  }
}