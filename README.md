# MicroService-Architecture
This is basic set of web applications with simple monitoring
For running you must pull repositiory:

    git pull https://github.com/sasha-egorov-01/MicroService-Architecture.git

And run docker-compose file:

    cd ./MicroService-Architecture 
    docker-compose up -d 

If prometheus container give an error with permissions, you will have to add chmod on "data" folder:
    chmod 777 -R ./data
