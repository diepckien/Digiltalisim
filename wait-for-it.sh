#!/bin/bash

# wait-for-it.sh
# Usage: ./wait-for-it.sh host:port

host="$1"
shift
cmd="$@"

until mysql -h"$host" -uroot -p"$MYSQL_ROOT_PASSWORD" -e 'SELECT 1;' ; do
  >&2 echo "MySQL is unavailable - sleeping"
  sleep 1
done

>&2 echo "MySQL is up - executing command"
exec $cmd
