docker build -t dj-img .

# --link existing_container:new_container
docker run --rm \
  -p 8000:8000 \
  -v $(pwd)/:/app/ \
  --name dj-container \
  --link db-container:dj-container \
  dj-img
