#!/bin/zsh -ex

# --dbpath
mkdir -p /var/lib/mongodb/replication
chown -R mongodb:mongodb /var/lib/mongodb/replication   #setting correct permission

mongod --port 27017 --dbpath /var/lib/mongodb/replication --replSet rs0
