To build this image, simply be in this subdirectory and execute the following command:

```docker build --pull --no-cache -t dosage:latest .```


Example usage:

```docker run --rm -v /home/Webcomics:/webcomics dosage:latest -b /webcomics IncredibleWebcomic```

This will save comics under /home/Webcomics.
You can use all the options of Dosage as normal.

Additionally you may also set custom scraper classes by adding an additional mount volume, like so:

```docker run --rm -v /home/Webcomics:/webcomics -v /home/Webcomics/custom_scrapers.py:/dosage/dosagelib/plugins/custom.py dosage:latest IncredibleWebcomic```

Make sure the custom_scrapers.py file exists at the specified location