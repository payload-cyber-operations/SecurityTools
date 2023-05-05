#!/bin/bash


for x in $(ls /var/lib/mysql/ | grep "binlog.*");
do
    rm "/var/lib/mysql/$x";
done
