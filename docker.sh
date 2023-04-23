CONTAINER_NAME="restart_pi"

docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME
docker build --tag $CONTAINER_NAME --build-arg container_name=$CONTAINER_NAME .
docker run -d --name $CONTAINER_NAME --restart unless-stopped -v $(pwd)/:/$CONTAINER_NAME $CONTAINER_NAME