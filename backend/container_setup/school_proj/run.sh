docker build --quiet -t dj-img .

docker run --rm \
  -p 8000:8000 \
  -v $(pwd)/:/app/ \
  --name dj-container \
  --link db-container:dj-container \
  dj-img
