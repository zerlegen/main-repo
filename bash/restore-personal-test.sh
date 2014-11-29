#!/bin/bash

BACKUP_IN_FILE=$1

read -s -p "Enter passphrase for encrypted backup: " inpassph
printf "\n"

# decrypt
PASSPH=$inpassph
TRUN_1_EXT="${BACKUP_IN_FILE%.*}"
gpg -d --passphrase $PASSPH -o $BACKUP_IN_FILE.aes $BACKUP_IN_FILE
gpg -d --passphrase $PASSPH -o $TRUN_1_EXT $BACKUP_IN_FILE.aes
rm $BACKUP_IN_FILE.aes


TRUN_2_EXT="${TRUN_1_EXT%.*}"
bzip2 -df $TRUN_1_EXT > $TRUN_2_EXT

TRUN_3_EXT="${TRUN_2_EXT%.*}"
mkdir $TRUN_3_EXT
tar -xf $TRUN_2_EXT -C $TRUN_3_EXT

printf "Restored backup $BACKUP_IN_FILE to directory: $TRUN_3_EXT\n"




