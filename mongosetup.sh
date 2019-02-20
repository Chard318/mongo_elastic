#!/bin/bash

# MONGODB1=`ping -c 1 mongo | head -1  | cut -d "(" -f 2 | cut -d ")" -f 1`

# echo "**********************************************" ${MONGODB1}
# echo "Waiting for startup.."
# until curl http://${MONGODB1}:28017/serverStatus\?text\=1 2>&1 | grep uptime | head -1; do
#   printf '.'
#   sleep 1
# done

# echo curl http://${MONGODB1}:28017/serverStatus\?text\=1 2>&1 | grep uptime | head -1
# echo "Started.."

sleep 15


echo SETUP.sh time now: `date +"%T" `
mongo --host mongo:27017 <<EOF
rs.initiate()
EOF