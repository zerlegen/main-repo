#!/usr/bin/bash

# run xmind-xml.py and build a test xmind workbook
cd build
unzip build.xmind.original 
../xmind-xml.py > content.xml
zip build.xmind content.xml META-INF Thumbnails meta.xml Revisions
rm -rf *.xml META-INF Thumbnails Revisions
