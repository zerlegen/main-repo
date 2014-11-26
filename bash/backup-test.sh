#!/bin/bash

INCLUDE_PATHS=(
               "/cygdrive/c/shared/temp/backup-test"
               "/cygdrive/c/shared/temp/backup-test2"
              )

inpassph="foo"
inpassph2="bar"

while [ "$inpassph" != "$inpassph2" ]
do
  read -s -p "Enter passphrase for encryption key: " inpassph
  printf "\n"
  read -s -p "Enter passphrase again to confirm: " inpassph2
  printf "\n" 
  if [ "$inpassph" != "$inpassph2" ]
  then
    printf "passwords not equal\n"
  fi 
done

PASSPH=$inpassph
TAR_INCLUDE=""

for i in "${INCLUDE_PATHS[@]}"; do
  printf "processing path: $i\n"
  #BASE_NAME=${i##*/} 
  TAR_INCLUDE="$TAR_INCLUDE $i" 
done

# Archive / Compress
OUT_NAME="backup-$(date -I).tar"
tar -cf $OUT_NAME $TAR_INCLUDE
bzip2 -cf $OUT_NAME > $OUT_NAME.bz2
rm $OUT_NAME

# Encrypt
gpg -c --cipher-algo AES256 --passphrase $PASSPH -o $OUT_NAME.bz2.aes $OUT_NAME.bz2
gpg -c --cipher-algo TWOFISH --passphrase $PASSPH -o $OUT_NAME.bz2.gpg $OUT_NAME.bz2.aes
  
# Cleanup
rm $OUT_NAME.bz2
rm $OUT_NAME.bz2.aes
    

#read -s -p "Enter passphrase again to confirm: " inpasswd2

  #read -s -p "Enter passphrase for encryption key: " inpasswd


