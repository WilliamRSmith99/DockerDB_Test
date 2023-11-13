# DockerDB_Test

Hey Rockstar team! 

Inside this repo you will find my completed take-home test with the given specifications.

These Images are available via dockerhub by running: 

    docker pull williamrsmith99/custom-postgres &&\
    docker pull williamrsmith99/custom-nginx

My first image, custom-postgres, is built on top of the official postgres base image. This image features customized networking configs for the database, and sql to create a custom DirectoryDB database, import sample data into our new database, and create service user RockstarUser permissioned only to DirectoryDB to access the data for the 2nd image. **This image is a dependency for my 2nd image, please have this container running before starting the 2nd container, custom-nginx.** 

This image can be ran optimally via the command:
    Docker run -d -p 35432:5432 --rm --name postgres williamrsmith99/custom-postgres

My second image, custom-nginx, is built on top of the official Ubuntu 20.04 image. This image features python scripts to connect to image 1's postgres database, use Smarty api to validate address authenticity, store the findings in the database, and then use the database's contents to generate an HTML document. That document is served via NGINX and avaialable on localhost:8080. 

This image can most optimally be ran as a container via the following command:
    Docker run -d -p 8080:8080 --rm --name nginx williamrsmith99/custom-nginx


Please let me know if you have any thoughts and/or questions! I look forward to speaking with you soon!

Best,
Will Smith
