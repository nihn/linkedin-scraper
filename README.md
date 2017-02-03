# LinkedIn scraper #
Simple scraper which query LinkedIn people database for given string and
scrap the people from result page.

## Installing ##
Installation method uses [Docker](https://docs.docker.com/engine/installation/) and [Docker-compose](https://docs.docker.com/compose/install/).

Use helper script:
```bash
./run.sh
```

docker-compose will manage to download and install every dependencies
you need before running scraper.

## Usage ##
```bash
./run.sh "John Smith"
```

This use `docker-compose run` command under the hood. For more options
see `./run.sh -h`.
Be aware that you will be asked for your LinkedIn credentials in order
to allow the scraper to login and do actual query.
By default results are stored in `results.csv`, you can change this by
explicitly passed `-o` option.

## Tests ##
```
./tests.sh
```


## Working with queries in languages other than English ##
By default crawler try to find best possible matches using list of
english professions, names and surnames. If you need to find people
from country where English is not used then you should replace content
of these files:

* `names_list.txt` - fill with names most popular in desired language (by
default it contains US names),
* `surnames_list.txt` - fill with surnames most popular in desired language (
by default in contains US surnames),
* `professions_list.txt` - fill with profession names from desired language (by
default english profession names),
* `surname_affixes_list.txt` - it already contains international suffixes based
on [Wikipedia](https://en.wikipedia.org/wiki/List_of_family_name_affixes).

Without it classification will still work but not as good as it could.
