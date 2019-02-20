#!/bin/bash

sleep 30

python3 /app/pymongo_run.py
mongo-connector -m mongo:27017 -t es:9200 -d elastic2_doc_manager


 curl -H 'Content-Type: application/json' \
   -X PUT http://es:9200/shellfish_db_opt \
   -d \
  "{ \
      \"settings\": { \
          \"number_of_shards\": 1, \
          \"analysis\": { \
              \"filter\": { \
                  \"autocomplete_filter\": { \
                      \"type\":     \"edge_ngram\", \
                      \"min_gram\": 3, \
                      \"max_gram\": 20 \
                  } \
              }, \
              \"analyzer\": { \
                  \"autocomplete\": { \
                      \"type\":      \"custom\", \
                      \"tokenizer\": \"standard\", \
                      \"filter\": [ \
                          \"lowercase\", \
                          \"autocomplete_filter\" \
                      ] \
                  } \
              } \
          } \
      } \
  }"

  curl -H 'Content-Type: application/json' \
        -X PUT http://es:9200/shellfish_db_opt/_mapping/employee \
        -d \
       "{ \
           \"employee\": { \
               \"_all\": {\"enabled\": \"false\"}, \
               \"properties\": { \
                   \"About_me\": { \
                       \"type\":     \"text\", \
                       \"analyzer\": \"autocomplete\" \
                   }, \
                   \"Ask_me_about\": { \
                       \"type\":     \"text\", \
                       \"analyzer\": \"autocomplete\" \
                   }, \
                   \"Business_Unit\": { \
                       \"type\":     \"text\" \
                   }, \
                   \"Certifications_accreditations\": { \
                       \"type\":     \"text\", \
                       \"analyzer\": \"autocomplete\" \
                   }, \
                   \"Company_Name_1\": { \
                       \"type\":     \"text\" \
                   }, \
                   \"Company_Name_2\": { \
                       \"type\":     \"text\" \
                   }, \
                   \"Company_Name_3\": { \
                       \"type\":     \"text\" \
                   }, \
                   \"Company_Name_4\": { \
                       \"type\":     \"text\" \
                   }, \
                   \"Company_Name_5\": { \
                       \"type\":     \"text\" \
                   }, \
                   \"Company_Name_6\": { \
                       \"type\":     \"text\" \
                   }, \
                   \"Company_Name_7\": { \
                       \"type\":     \"text\" \
                   }, \
                   \"Department\": { \
                       \"type\":     \"text\", \
                       \"analyzer\": \"autocomplete\" \
                   }, \
                   \"Discipline\": { \
                       \"type\":     \"text\", \
                       \"analyzer\": \"autocomplete\" \
                   }, \
                   \"Education\": { \
                       \"type\":     \"text\" \
                   }, \
                   \"Function\": { \
                       \"type\":     \"text\", \
                       \"analyzer\": \"autocomplete\" \
                   }, \
                   \"Job_title\": { \
                       \"type\":     \"text\", \
                       \"analyzer\": \"autocomplete\" \
                   }, \
                   \"Last_Updated\": { \
                       \"type\":     \"text\" \
                   }, \
                   \"Location_1\": { \
                       \"type\":     \"text\" \
                   }, \
                   \"Location_2\": { \
                       \"type\":     \"text\" \
                   }, \
                   \"Location_3\": { \
                       \"type\":     \"text\" \
                   }, \
                   \"Location_4\": { \
                       \"type\":     \"text\" \
                   }, \
                   \"Location_5\": { \
                       \"type\":     \"text\" \
                   }, \
                   \"Location_6\": { \
                       \"type\":     \"text\" \
                   }, \
                   \"Location_7\": { \
                       \"type\":     \"text\" \
                   }, \
                   \"Name\": { \
                       \"type\":     \"keyword\" \
                   }, \
                   \"Professional_Memberships\": { \
                       \"type\":     \"text\", \
                       \"analyzer\": \"autocomplete\" \
                   }, \
                   \"Profile_Complete\": { \
                       \"type\":     \"keyword\" \
                   }, \
                   \"Publications\": { \
                       \"type\":     \"text\", \
                       \"analyzer\": \"autocomplete\" \
                   }, \
                   \"Ref_Indicator\": { \
                       \"type\":     \"text\" \
                   }, \
                   \"Role_1\": { \
                       \"type\":     \"text\", \
                       \"analyzer\": \"autocomplete\" \
                   }, \
                   \"Role_2\": { \
                       \"type\":     \"text\", \
                       \"analyzer\": \"autocomplete\" \
                   }, \
                   \"Role_3\": { \
                       \"type\":     \"text\", \
                       \"analyzer\": \"autocomplete\" \
                   }, \
                   \"Role_4\": { \
                       \"type\":     \"text\", \
                       \"analyzer\": \"autocomplete\" \
                   }, \
                   \"Role_5\": { \
                       \"type\":     \"text\", \
                       \"analyzer\": \"autocomplete\" \
                   }, \
                   \"Role_6\": { \
                       \"type\":     \"text\", \
                       \"analyzer\": \"autocomplete\" \
                   }, \
                   \"Role_7\": { \
                       \"type\":     \"text\", \
                       \"analyzer\": \"autocomplete\" \
                   }, \
                   \"Role_Description_1\": { \
                       \"type\":     \"text\", \
                       \"analyzer\": \"autocomplete\" \
                   }, \
                   \"Role_Description_2\": { \
                       \"type\":     \"text\", \
                       \"analyzer\": \"autocomplete\" \
                   }, \
                   \"Role_Description_3\": { \
                       \"type\":     \"text\", \
                       \"analyzer\": \"autocomplete\" \
                   }, \
                   \"Role_Description_4\": { \
                       \"type\":     \"text\", \
                       \"analyzer\": \"autocomplete\" \
                   }, \
                   \"Role_Description_5\": { \
                       \"type\":     \"text\", \
                       \"analyzer\": \"autocomplete\" \
                   }, \
                   \"Role_Description_6\": { \
                       \"type\":     \"text\", \
                       \"analyzer\": \"autocomplete\" \
                   }, \
                   \"Role_Description_7\": { \
                       \"type\":     \"text\", \
                       \"analyzer\": \"autocomplete\" \
                   }, \
                   \"Shell_Business\": { \
                       \"type\":     \"text\" \
                   }, \
                   \"Skills\": { \
                       \"type\":     \"text\", \
                       \"analyzer\": \"autocomplete\" \
                   }, \
                   \"Timespan_1\": { \
                       \"type\":     \"text\" \
                   }, \
                   \"Timespan_2\": { \
                       \"type\":     \"text\" \
                   }, \
                   \"Timespan_3\": { \
                       \"type\":     \"text\" \
                   }, \
                   \"Timespan_4\": { \
                       \"type\":     \"text\" \
                   }, \
                   \"Timespan_5\": { \
                       \"type\":     \"text\" \
                   }, \
                   \"Timespan_6\": { \
                       \"type\":     \"text\" \
                   }, \
                   \"Timespan_7\": { \
                       \"type\":     \"text\" \
                   } \
               } \
           } \
       }"

