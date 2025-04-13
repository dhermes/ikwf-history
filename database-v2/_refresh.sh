#!/bin/bash

set -e -x

rm -f ./ikwf.sqlite
sqlite3 ./ikwf.sqlite < ./migrations/0001-initialize-schema.sql
sqlite3 ./ikwf.sqlite < ./migrations/0002-populate-enums.sql
