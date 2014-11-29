

INCLUDE_PATHS=(
               "e:/backed-up"
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

PASSPH="$inpassph"


TAR_INCLUDE=""

for i in "${INCLUDE_PATHS[@]}"; do
  printf "adding directory: $i"
  #BASE_NAME=${i##*/} 
  TAR_INCLUDE="$TAR_INCLUDE $i" 
done

# Archive / Compress
OUT_NAME="backup-personal-$(date -I).tar"

tar -cvf $OUT_NAME $TAR_INCLUDE
bzip2 -cvf $OUT_NAME > $OUT_NAME.bz2
rm $OUT_NAME

# Encrypt
gpg -c -v --cipher-algo AES256 --passphrase $PASSPH -o $OUT_NAME.bz2.aes $OUT_NAME.bz2
gpg -c -v --cipher-algo TWOFISH --passphrase $PASSPH -o $OUT_NAME.bz2.gpg $OUT_NAME.bz2.aes
  
# Cleanup
rm $OUT_NAME.bz2
rm $OUT_NAME.bz2.aes

## Push to Google Drive
#cp $OUT_NAME.bz2.gpg "/cygdrive/c/users/epomerleau/Google Drive/" 

printf "Open google drive and upload file $OUT_NAME.bz2.gpg"

