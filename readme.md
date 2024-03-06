docker run --name tracker-db --network app -v mysql-volume:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=password -p 3306:3306 -d mysql:latest

docker run --name phpmyadmin --network app -d --link tracker-db:db -p 8080:80 phpmyadmin

