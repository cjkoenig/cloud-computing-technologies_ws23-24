# Introduction to Docker Part 2

**DO NOT DEPLOY THIS SETUP PERMANTELY TO THE INTERNET- IT IS VERY SIMPLIFIED BUT TOTALLY INSECURE! USE IT ONLY FOR TESTING AND LEARNING PURPOSES.**

In this exercise, we will orchestrate multiple containers that form a web application (wordpress with mysql). Futhermore, we install phpMyAdmin as data base administration tool.

Have a look at the docker-compose.yml file in the directory and understand the setup: which containers expose ports to the outside, which container is depended from another, which container stores data on the host, etc.

This deployment can be done locally or in the cloud.

 1.  Enter this directory and start the containers: 
	 `docker-compose up -d`
 2. Display running containers:
	 `docker ps -a`
 3. Display informations from a running container, e.g., *wordpress_mysql_pma-wordpress-1:*
	 `docker inspect wordpress_mysql_pma-wordpress-1`
 4. To do the wordpress setup, browse through [http://hostname](http://hostname) in a webbrowser
 5. To access the MySQL db with phpMyAdmin open [http://hostname:8080](http://hostname:8080)
 6. Shutdown and delete the containers: 
	 `docker-compose down`
 7. Display volumes stored on host:
	 `docker volume ls`
 8. Remove volume data from host:
	 `docker volume rm wordpress_mysql_pma_dbdata`
	 `docker volume rm wordpress_mysql_pma_wordpress`

Reference:
- https://docs.docker.com/compose/
