==force to remove all runnings images==
docker rm -f website
==list available images downloaded==
docker images
=====show runnings containers===
docker images ls
docker images
==show comntainers ==
docker container ls -a
docker ps -a
==mount container volume from host===
docker run --name website -v $(pwd):/usr/share/nginx/html -d -p 8080:80 nginx
===docker build with Dockerfile===
docker build --tag website:latest .
docker image 
==run an image==
docker run  --name website -p 8080:80 -d website:latest
docker run --name user-api -d -p 3000:3000 user-service-api:latest
===tagging help create our own container with own tag===
docker run  --name website -p 8080:80 -d amisgoscode-website:latest
docker tag amisgoscode-website:latest amigoscode-website:1
==logg in docker hub===
docker login
docker push amigocode/website:1


