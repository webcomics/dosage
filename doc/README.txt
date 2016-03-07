Dosage
======

Dosage is a comic strip downloader and archiver.

Dosage is designed to keep a local copy of specific webcomics and other
picture-based content such as Picture of the Day sites.  With the dosage
commandline script you can get the latest strip of a webcomic, or catch-up to
the last strip downloaded, or download a strip for a particular date/index (if
the webcomic's site layout allows this).

Multiple webcomics can be downloaded in parallel, making the update of comic
strips faster.

See http://dosage.rocks/ for more info.

Docker Dosage
=============

You can use dosage as a Docker container.
* create on your host the storage directory ie :
```
mkdir -p /srv/dosage
```
* build your container :
```
docker build -t dosagedocker .
```
* then configure your dosage :
```
# List available comics :
docker run --rm -ti dosagedocker dosage -l

# add your comics
docker run --rm -ti -v /srv/dosage:/app/dosage dosagedocker dosage YourComic #add -a to download all of the comic pages
docker run --rm -ti -v /srv/dosage:/app/dosage dosagedocker dosage AnotherComic
```
* Once the initial setup is done simply run :
```
docker run -v /srv/dosage:/app/dosage dosagedocker
# This will tell dosage to get latest pages from all the comics you configured
# it will also do that endlessly (unless you destroy the container) every 3600seconds (1 hours)
# To change this 1 hour interval to 2 hours (aka 7200 seconds) :
docker run -v /srv/dosage:/app/dosage -e RUNEVERY=7200 dosagedocker
# If you want to add more options to the automated run :
docker run -e OPTIONS="--adult -v" -v /srv/dosage:/app/dosage dosagedocker
```
* Remeber you can still get help :
```
docker run --rm -ti dosagedocker dosage -h
```
