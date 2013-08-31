#!/usr/bin/python3

import re
import os.path

class XMindManifest:
    
    #_file_entries
    _mappings = {
        "jpg":"image/jpeg",
        "jpeg":"image/jpeg",
        "png":"image/png",
        "gif":"image/gif",
        "bmp":"image/bmp",
        "xml":"text/xml"
    }
        

    def __init__(self):
        self._file_entries = []

#    MEDIA_TYPE_PNG = "image/png"
#    MEDIA_TYPE_JPG = "image/jpeg"
#    MEDIA_TYPE_GIF = "image/gif"
#    MEDIA_TYPE_TEXT_XML = "text/xml"
#    MEDIA_TYPE_NONE = ""
#
    def get_media_type(self, file_extension):
        if file_extension in self._mappings:
            return self._mappings[file_extension]
        else:
            return ""

    def add_file_entry(self, full_path):
        fext = os.path.basename(full_path).split('.')[-1]
        media_type = self.get_media_type(fext)
        self._file_entries.append("<file-entry full-path=\"" + full_path +
                                  "\"" + " media-type=\"" + media_type +
                                  "\"" + "/>")

    def write_manifest_file(self, out_file_path):
        out = open(out_file_path, "w")
        out.write("<manifest>")
        for entry in self._file_entries:
            print("writing entry: " + entry)
            out.write(entry)
        out.write("</manifest>")
        out.close()

    
###########################################################################
# BEGIN UNIT TESTS
###########################################################################

def test_simple_manifest():
    xmanif = XMindManifest()
    xmanif.add_file_entry("content.xml")
    xmanif.add_file_entry("Revisions/0edvkf59qnh1u4r03uk9rg5opd/revisions.xml")
    xmanif.add_file_entry("attachments/239847304586234587.jpg")
    xmanif.add_file_entry("attachments/89723489734958724.jpeg")
    xmanif.add_file_entry("attachments/2143234258723424.png")
    xmanif.add_file_entry("attachments/noextension")
    xmanif.add_file_entry("attachments/unknown-extension.ggg")
    xmanif.write_manifest_file("test-manifest.xml")
        
     
if (__name__ == "__main__"):
    test_simple_manifest()        
