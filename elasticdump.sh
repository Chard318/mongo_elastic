#!/bin/bash

sleep 35

elasticdump \
	--input=http://es:9200/shellfish_db \
	--output=http://es:9200/shellfish_db_opt