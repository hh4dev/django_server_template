#!/bin/bash
USER='appdev'
PASS='appdev'
ROOT_USER='root'
ROOT_PASS='root'

mysql -u "$ROOT_USER" -p"$ROOT_PASS" -e "GRANT ALL PRIVILEGES On *.* TO appdev@localhost IDENTIFIED BY 'appdev';"

SQL_PATH='/docker-entrypoint-initdb.d/query/create-database.sql'
echo 'creating databases';
mysql -u "$USER" -p"$PASS" < "$SQL_PATH"
echo 'done'