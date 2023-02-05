# fampay-assignment
cron.py file contains a cronjob that calls the youtube search api and stores the data in mongo db. To run the cron use the following command.

python3 cron.py

main.py is the entry point for the flask application. To run the main file use the following command.

python3 main.py

API endpoint-
/search/<search_text>/<page_no>

Please set the Youtube API Key in the constants.py file before running the project.
