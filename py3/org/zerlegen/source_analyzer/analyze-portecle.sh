#!/usr/bin/bash

SRC_DIR="/home/epom/test-repo/portecle/src/main/net/sf/portecle/"
DEP_DIR="/cygdrive/c/Program Files (x86)/Java/jre6/lib"

XMIND_BUILD_DIR="/home/epom/test-repo/py3/org/zerlegen/pyXmind/build"
OUT_XML="$XMIND_BUILD_DIR/content-in.xml"


./mindmap_generator.py "$SRC_DIR" "$DEP_DIR" "$OUT_XML" 
../pyXmind/build-xmind-book.sh

cp $XMIND_BUILD_DIR/build.xmind .
echo "Mind map generation complete.  Output file is: ./build.xmind"
