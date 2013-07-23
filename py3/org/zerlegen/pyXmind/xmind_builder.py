#!/usr/bin/python3

import os
import tempfile
import shutil
from xmind_manifest import XMindManifest
import zipfile


################################################################################
# Simple wrapper over an Xmind workbook
################################################################################

class XMindBuilder:
    _in_content_xml = ""
    _in_meta_xml = ""

    # list of pairs - each pair is (<path to file>, <media-type>)
    _in_attachments = []

    _in_thumbnails = []
    _in_revisions = []
    #_build_dir = None

    ###########################################################################
    # Constructor
    # in_template - optional existing workbook used to pre-populate this workbook
    #
    #
     
    def _init(in_template = None):
        # unzip workbook
        # pre-populate fields
        pass

    def set_content_xml(self, content_xml):
        self._in_content_xml = content_xml

    def set_meta_xml(self, meta_xml):
        self._in_meta_xml = meta_xml


    ###########################################################################
    # Add an attachement to this workbook
    # 
    # abs_attachment_file - path to the file to add
    # media_type - manifest type of the attachment file
    # 

    def add_attachment(self, abs_attachment_file, media_type):
        #
        #print("adding attachment: " + attachment_file + " as: " + media_type)
        #
        self._in_attachments.append((abs_attachment_file, media_type))


    
    ###########################################################################
    def add_thumbnail(self, thumbnail_file):
        self._in_thumbnails.append(thumbnail_file)


    ###########################################################################
    def add_revision(self, revision_file):
        self._in_revisions.append(revision_file)


    ###########################################################################
    def build(self, out_file):

        #######################################################################
        def populate_sub_dir(sub_name, abs_file_list):
            #
            print("creating build sub dir: " + sub_name)
            #
            path_to_sub = os.path.join(build_path, sub_name)
            os.mkdir(path_to_sub)
            for abs_file in abs_file_list:
                filename = os.path.basename(abs_file)
                #
                print("copying file: " + abs_file + " to: " + os.path.join(path_to_sub, filename))
                #
                shutil.copyfile(abs_file, os.path.join(path_to_sub, filename))

        #######################################################################
        def zipup_workbook(build_path, out_file):
            print("zipping up workbook...")
            #
            with zipfile.ZipFile(out_file, 'w') as outzip:
                tmp_dir = os.curdir
                os.chdir(build_path)
                for (dir, subs, files) in os.walk('.'):
                    for file in files:
                        #
                        print("adding file: " + file + " to zip...")
                        outzip.write(os.path.join(dir, file))
                os.chdir(tmp_dir)

        #######################################################################
        def build_manifest(build_path):
            #
            print("building manifest...")
            #
            meta_inf = os.path.join(build_path, "META-INF")
            os.mkdir(meta_inf)


            manifest = XMindManifest() 
            for (dir, subs, files) in os.walk(build_path):
                print("subs: " + str(subs))
                for file in files:

                    # determine media type
                    if file.endswith(".txt") or file.endswith(".xml"):
                        media_t = manifest.MEDIA_TYPE_TEXT_XML
                    elif file.endswith(".jpg") or \
                         file.endswith(".png") or \
                         file.endswith(".jpeg") or \
                         file.endswith(".bmp"):
                        media_t = manifest.MEDIA_TYPE_IMAGE
                    else:
                        media_t = manifest.MEDIA_TYPE_NONE

                    # determine path relative to workbook root
                    rel_path = dir.replace(build_path, "")
                    rel_path = rel_path.replace(os.path.sep, "", 1)
                    #
                    #print("rel path: " + str(rel_path.startswith(os.path.sep)))
                    #
                    if len(rel_path) == 0:
                        print("adding manifest file: " + file + " as: " + media_t)
                        manifest.add_file_entry(file, media_t)
                    else:
                        print("adding manifest file: " + 
                              os.path.join(rel_path, file) + "as: " + media_t)
                        manifest.add_file_entry(os.path.join(rel_path, file), media_t)

                for sub in subs:
                    print("adding manifest dir: " + sub)
                    manifest.add_file_entry(sub + os.path.sep, manifest.MEDIA_TYPE_NONE)

            manifest.add_file_entry(os.path.join("META-INF", "manifest.xml"), 
                                    manifest.MEDIA_TYPE_TEXT_XML)
            print("writing manifest file to: " + os.path.join(meta_inf, "manifest.xml"))
            #
            manifest.write_manifest_file(os.path.join(meta_inf, "manifest.xml"))


        #
        #print("creating build dir: " + self._build_dir)
        #
        #build_path = tempfile.mkdtemp(self._build_dir)
        build_path = tempfile.mkdtemp()


        # populate build dir
        #
        print("copying content xml: " + self._in_content_xml + " to: " + build_path)
        #
        shutil.copyfile(self._in_content_xml, os.path.join(build_path, "content.xml"))

        print("copying meta xml: " + self._in_meta_xml + " to: " + build_path)
        #
        shutil.copyfile(self._in_meta_xml, os.path.join(build_path, "meta.xml"))


        #
        print("populating attachments...")
        #
        #print(self._in_attachments)
        populate_sub_dir("attachments", 
                         [pair[0] for pair in self._in_attachments])
        #
        print("populating thumbnails...")
        #
        populate_sub_dir("Thumbnails", self._in_thumbnails)
        # 
        print("populating revisions...")
        #
        populate_sub_dir("Revisions", self._in_revisions)

        build_manifest(build_path)
        zipup_workbook(build_path, out_file)
        

        # cleanup build dir
        try:
            shutil.rmtree(build_path)
        except OSError:
            print("Error deleting build dir: " + str(OSError))

################################################################################
# BEGIN UNIT TESTS
################################################################################


################################################################################
# Basic unit test - manually duplicate a specified workbook

def test_build_workbook(in_book, out_book):
    extract_dir = tempfile.mkdtemp()
    test_wkbk = zipfile.ZipFile(in_book, 'r') 
    test_wkbk.extractall(extract_dir)

    builder = XMindBuilder()
    builder.set_content_xml(os.path.join(extract_dir, 'content.xml'))
    builder.set_meta_xml(os.path.join(extract_dir, 'meta.xml'))
    builder.add_attachment(os.path.join(extract_dir, 'attachments', 
                                        "0g9t76dl47617sja3r840po3ug.txt"), 
                           XMindManifest.MEDIA_TYPE_TEXT_XML)
    builder.add_attachment(os.path.join(extract_dir, "attachments", 
                                        "5s33aeq5fc2bmb1qcnlhbqh69t.jpg"),
                           XMindManifest.MEDIA_TYPE_IMAGE)
                                        

    #    builder.add_attachment_dir(os.path.join(extract_dir, 'attachments'))
    builder.build(os.path.join(os.curdir, out_book))

if (__name__ == "__main__"):
    test_build_workbook('test-build.xmind', 'test-out.xmind')





