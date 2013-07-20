#!/usr/bin/python3

class XMindManifest:
    
    _file_entries = []

    MEDIA_TYPE_IMAGE = "image/png"
    MEDIA_TYPE_TEXT_XML = "text/xml"
    MEDIA_TYPE_NONE = ""

    def add_file_entry(self, full_path, media_type):
        self._file_entries.append("<file-entry full-path=\"" + full_path +
                                  "\"" + " media-type=\"" + media_type +
                                  "\"" + "/>")

    def write_manifest_file(self, out_file_path):
        out = open(out_file_path, "w")
        out.write("<manifest>")
        for entry in self._file_entries:
            out.write(entry)
        out.write("</manifest>")
        out.close()

    
###########################################################################
# BEGIN UNIT TESTS
###########################################################################

def test_simple_manifest():
    xmanif = XMindManifest()
    xmanif.add_file_entry("content.xml", XMindManifest.MEDIA_TYPE_XML)
    xmanif.add_file_entry("Revisions/0edvkf59qnh1u4r03uk9rg5opd/revisions.xml",
                          XMindManifest.MEDIA_TYPE_NONE)
    xmanif.write_manifest_file("test-manifest.xml")
        
     
if (__name__ == "__main__"):
    test_simple_manifest()        
