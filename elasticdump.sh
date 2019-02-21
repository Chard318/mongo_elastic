#!/bin/bash

# wait for data transport to elasticsearch database
sleep 35

# index the data using the customized autocomplete indexer
elasticdump \
	--input=http://es:9200/shellfish_db \
	--output=http://es:9200/shellfish_db_opt