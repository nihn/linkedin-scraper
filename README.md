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

## Tests ##
```
./tests.sh
```
