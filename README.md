# LinkedIn scraper #
A simple scraper which queries LinkedIn people database for given string and
scrap personal details from result page.

## Installing ##
Installation method uses [Docker](https://docs.docker.com/engine/installation/) and [Docker-compose](https://docs.docker.com/compose/install/).

Use helper script:
```bash
./run.sh
```

`docker-compose` will manage to download and install dependencies that
you need before running the scraper.

## Usage ##
```bash
./run.sh "John Smith"
```

This uses `docker-compose run` command under the hood. For more options
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
By default crawler tries to find best possible matches using list of
english professions, names and surnames. If you need to find people
from countries where English is not used, then you should replace content
of these files:

* `data/names_list.txt` - fill it with most popular names in desired language (by
default it contains US names),
* `data/surnames_list.txt` - fill it with most popular surnames in desired language (
by default it contains US surnames),
* `data/professions_list.txt` - fill it with profession names from desired language (by
default english profession names),
* `data/surname_affixes_list.txt` - it already contains international affixes based
on [Wikipedia](https://en.wikipedia.org/wiki/List_of_family_name_affixes).

Without modifying these files classification will still work but not as good as it could.
