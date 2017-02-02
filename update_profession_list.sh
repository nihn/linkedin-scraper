#!/bin/sh

set -e

docker-compose run --entrypoint scrapy crawler crawl career_update -o tmp.csv

sed '1d' tmp.csv > ./data/professions_list.txt

# Add common corporate titles
echo "CEO\nCTO\nCAO\nCBO\nCFO\n" >> ./data/professions_list.txt
