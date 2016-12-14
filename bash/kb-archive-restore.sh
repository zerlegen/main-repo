#!/bin/bash
IN_FILE=$1
cd ~/
TIMESTAMP=`date +%Y-%m-%d-%H-%M`
STAGING_DIR="archive-staging-$TIMESTAMP"
mkdir $STAGING_DIR
cp $IN_FILE $STAGING_DIR
IN_BASE_FILE=${IN_FILE##*/}
gpg $STAGING_DIR/$IN_BASE_FILE
GZ_FILE=${IN_BASE_FILE%.gpg}
cd $STAGING_DIR
tar -xvf $GZ_FILE 
cd ..
echo "Archive file restored to: $STAGING_DIR/"

