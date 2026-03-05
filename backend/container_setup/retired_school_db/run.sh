# not needed since I ran the compose.yaml
docker build --quiet -t db-img .

docker run -d --rm --name db-container db-img

docker ps