#!/bin/zsh -ex

#--dbpath
mkdir -p /var/lib/mongodb/replication1
chown -R mongodb:mongodb /var/lib/mongodb/replication1  #setting correct permission

mongod --port 27018 --dbpath /var/lib/mongodb/replication1 --replSet rs0
