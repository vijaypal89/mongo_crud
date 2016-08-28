#!/bin/zsh -ex

#--dbpath
mkdir -p /var/lib/mongodb/replication2
chown -R mongodb:mongodb /var/lib/mongodb/replication2  #setting correct permission

mongod --port 27019 --dbpath /var/lib/mongodb/replication2 --replSet rs0
