# Seemannlab webpage

## How to update publication list

`curl "https://rth.dk/publications/get_publications.php?PubWords=Seemann" > _data/publications.json`
`python scripts/convert-publ-html2json.py`
