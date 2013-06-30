#!/usr/bin/bash
#
# build an xmind workbook
# 
# Expects a "content-in.xml" containing the mind map tree content in 
#   $PY_XMIND_HOME/build
#

HOME_DIR="/home/epom/test-repo"
PY_XMIND_HOME="$HOME_DIR/py3/org/zerlegen/pyXMind"

cd $PY_XMIND_HOME/build
unzip build.xmind.original 
rm content.xml
mv content-in.xml content.xml
zip build.xmind content.xml META-INF Thumbnails meta.xml Revisions
rm -rf *.xml META-INF Thumbnails Revisions
