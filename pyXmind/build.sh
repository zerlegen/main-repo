#!/usr/bin/bash

# run xmind-xml.py and build a test xmind workbook
./xmind-xml.py > build/content.xml
zip build/build.xmind build/content.xml build/META-INF build/Thumbnails build/meta.xml build/Revisions
