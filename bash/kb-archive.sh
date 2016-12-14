#!/bin/bash
cd ~/
TIMESTAMP=`date +%Y-%m-%d-%H-%M`
STAGING_DIR="archive-staging-$TIMESTAMP"
mkdir $STAGING_DIR
tar -cvf $STAGING_DIR/archive-$TIMESTAMP.tar vimwiki
gzip -cf $STAGING_DIR/archive-$TIMESTAMP.tar > $STAGING_DIR/archive-$TIMESTAMP.tar.gz
gpg --symmetric $STAGING_DIR/archive-$TIMESTAMP.tar.gz
cp $STAGING_DIR/archive-$TIMESTAMP.tar.gz.gpg ~/Dropbox/
rm -rf $STAGING_DIR
