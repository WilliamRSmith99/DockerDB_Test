#!/bin/bash

echo "Entering shell"
echo "#####################################################################################################"

# Copy custom configuration files to the PostgreSQL data directory
cp /tmp/pg_hba.conf /var/lib/postgresql/data/pg_hba.conf

# restart server so conf changes take effect
echo "Restarting PostgreSQL server..."
pg_ctl restart -D "$PGDATA"