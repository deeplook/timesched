# A basic world-time scheduler in Angular.

Forked from https://github.com/mitsuhiko/timesched as available at http://timesched.pocoo.org/

## Quick-Run

```
git clone https://github.com/deeplook/timesched.git
cd timesched/data/raw
wget http://download.geonames.org/export/dump/cities1000.zip
unzip cities1000.zip
wget http://download.geonames.org/export/dump/cities15000.zip
unzip cities15000.zip
wget http://download.geonames.org/export/dump/countryInfo.txt
cd ../..
npm install uglify-js
mkdir lib/generated
make all
open timesched.html
```
