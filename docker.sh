CONTAINER_NAME="restart_pi"
SCRIPT_NAME="server.py"

docker rmi -f $CONTAINER_NAME

docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME
docker build --tag $CONTAINER_NAME --no-cache	--build-arg container_name=$CONTAINER_NAME --build-arg script_name=$SCRIPT_NAME .
docker run -d --name $CONTAINER_NAME --restart unless-stopped -v $(pwd)/:/$CONTAINER_NAME $CONTAINER_NAME
