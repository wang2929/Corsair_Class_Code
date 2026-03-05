docker build -t db-img .

# -d detach which runs the container in the background
docker run -d --rm --name db-container db-img

# lists running containers
docker ps