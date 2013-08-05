#!/usr/bin/python3

import os
import tempfile
import shutil
from org.zerlegen.pyXmind.xmind_manifest import XMindManifest
import org.zerlegen.pyXmind.xmind_utils as xmind_utils

import zipfile


################################################################################
# Wrapper over an Xmind workbook with methods for assembly
################################################################################

class XMindWorkbookBuilder:
    _in_content_xml = ""
    _in_meta_xml = ""

    _in_attachments = []

    _in_thumbnails = []
    _in_revisions = []
    #_build_dir = None

    ###########################################################################
    # Constructor
    #
    #
    
    def _init(in_template = None):
        pass

    ########################################################################### 
    # set_from_template
    #
    # Prepopulate a builder object using an existing workbook
    #
    # in_book - workbook to use for prepopulating this object
    #
    #

    def set_from_template(self, in_template):

        extract_dir = tempfile.mkdtemp()
        test_wkbk = zipfile.ZipFile(in_template, 'r') 
        test_wkbk.extractall(extract_dir)
    
        self.set_content_xml(os.path.join(extract_dir, 'content.xml'))
        self.set_meta_xml(os.path.join(extract_dir, 'meta.xml'))

        for file in os.listdir(os.path.join(extract_dir, 'attachments')):
            self.add_attachment(os.path.join(extract_dir, 'attachments', file)) 
        

    def set_content_xml(self, content_xml):
        self._in_content_xml = content_xml

    def set_meta_xml(self, meta_xml):
        self._in_meta_xml = meta_xml


    ###########################################################################
    # Add an attachement to this workbook
    # 
    # attachment_file - path to the file to add
    # id - id string to use in manifest 
    # 

    def add_attachment(self, attachment_file, id):
        #
        #print("adding attachment: " + attachment_file )
        #
        self._in_attachments.append((attachment_file, id))


    
    ###########################################################################
    def add_thumbnail(self, thumbnail_file):
        self._in_thumbnails.append(thumbnail_file)


    ###########################################################################
    def add_revision(self, revision_file):
        self._in_revisions.append(revision_file)


    ###########################################################################
    #
    # out_file - output Xmind workbook
    #
    #  

    def build(self, out_file):

        
        #######################################################################
        # Populate attachments in a subdirectory for this workbook
        # 
        #
        # sub_name - name of workbook sub directory
        # abs_file_list - list of files to copy to sub_name (absolute paths)
        #
        #

        def populate_attachments():
            #
            print("creating attachments dir")
            #
            att_path = os.path.join(build_path, "attachments")
            os.mkdir(att_path)
            for (abs_file, id) in self._in_attachments:
                split_filename = os.path.basename(abs_file).split('.')
                if (len(split_filename) > 1):
                    dest = os.path.join(att_path, (id + '.' + split_filename[-1]))
                else:
                    dest = os.path.join(att_path, id)
                #
                print("copying file: " + abs_file + " to: " + dest)
                #
                shutil.copyfile(abs_file, dest)

        #######################################################################
        def zipup_workbook(build_path, out_file):
            print("zipping up workbook...")
            
            tmp_dir = os.getcwd()
            os.chdir(build_path)

            print("zip out: " + os.path.join(tmp_dir, out_file))
            outzip = zipfile.ZipFile(os.path.join(tmp_dir, out_file), 'w')
            for (dir, subs, files) in os.walk('.'):
                for file in files:
                    print("adding file: " + file + " to zip...")
                    outzip.write(os.path.join(dir, file))

            outzip.close()
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

                    # determine path relative to workbook root
                    rel_path = dir.replace(build_path, "")
                    rel_path = rel_path.replace(os.path.sep, "", 1)
                    #
                    #print("rel path: " + str(rel_path.startswith(os.path.sep)))
                    #
                    if len(rel_path) == 0:
                        print("adding manifest file: " + file )
                        manifest.add_file_entry(file)
                    else:
                        print("adding manifest file: " + 
                              os.path.join(rel_path, file)) 
                        manifest.add_file_entry(os.path.join(rel_path, file))

                for sub in subs:
                    print("adding manifest dir: " + sub)
                    manifest.add_file_entry(sub + os.path.sep)

            manifest.add_file_entry(os.path.join("META-INF", "manifest.xml"))
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
        ###
        #shutil.copyfile('./content.xml', os.path.join(build_path, "content.xml"))

        if len(self._in_meta_xml) > 0:
            print("copying meta xml: " + self._in_meta_xml + " to: " + build_path)
            #
            shutil.copyfile(self._in_meta_xml, os.path.join(build_path, "meta.xml"))


        #
        print("populating attachments...")
        #
        #print(self._in_attachments)
        populate_attachments()
                         
        #
        #print("populating thumbnails...")
        #
        #populate_sub_dir("Thumbnails", self._in_thumbnails, preserve_filenames)
        # 
        #print("populating revisions...")
        #
        #populate_sub_dir("Revisions", self._in_revisions, True)

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

    builder = XMindWorkbookBuilder()
    builder.set_content_xml(os.path.join(extract_dir, 'content.xml'))
    builder.set_meta_xml(os.path.join(extract_dir, 'meta.xml'))
    builder.add_attachment(os.path.join(extract_dir, 'attachments', 
                                        "0g9t76dl47617sja3r840po3ug.txt"), 
                                        "0g9t76dl47617sja3r840po3ug")
    builder.add_attachment(os.path.join(extract_dir, "attachments", 
                                        "5s33aeq5fc2bmb1qcnlhbqh69t.jpg"),
                                        "5s33aeq5fc2bmb1qcnlhbqh69t")
                                        

    #    builder.add_attachment_dir(os.path.join(extract_dir, 'attachments'))
    builder.build(os.path.join(os.curdir, out_book))

if (__name__ == "__main__"):
    test_build_workbook('test-build.xmind', 'test-out.xmind')





