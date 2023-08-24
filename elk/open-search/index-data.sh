#HOST adress where elasticsearch is running
HOST="https://localhost:9200"
#STATUS sends a curl request to elasticsearch and saves the response
STATUS=$(curl $HOST/_cluster/health?pretty --silent --insecure -u admin:admin | grep "status")
#DATA_FOLDER_PATH location of all .json files that will be send to elastic search
DATA_FOLDER_PATH="$(pwd)/data"
#JSON_LIST list with all json files
JSON_LIST=$(ls $DATA_FOLDER_PATH)
# Check if elasticsearch is already running and the cluster health status is green or yellow
if [[ "$STATUS" == *"green"* ]] || [[ "$STATUS" == *"yellow"* ]]; then
    for FILE in ${JSON_LIST[@]}
    do
        SUFFIX=".json"
        NAME=${FILE%"$SUFFIX"}
        curl -H "Content-Type: application/x-ndjson" -XPOST $HOST/$NAME/_bulk --data-binary "@$DATA_FOLDER_PATH/$FILE" --insecure -u admin:admin
    done
else
    echo "Check if Elasticsearch is running"
fi