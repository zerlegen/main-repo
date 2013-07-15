Source Analyzer v 0.1.

--------------------------------------------------------------------------------
OVERVIEW:
--------------------------------------------------------------------------------

This source analyzer uses the pyXmind package to generate XMind mind maps
showing the layout of a source code tree.  Currently the analyzer has two ways
of organizing source files: by similar filenames, and by type hierarchy. The
first case operates on the notion that source files with similar names
will have categorically similar functionality. The second case scans the
source files and parses out class names and class parent names (currently
only for Java).  Additionally, the analyzer can load external jar files to
scan for types that the source code tree inherits.  Once all files have been
scanned to determine type relationships, a mind map is generated for each
type hierarchy found in the source code tree.

The top most node of the mind map is the name of the top level directory of
the source code tree.  The next level holds the names of "root" level types.
These are types that are either 1) in the source code tree and have no parent
type (other than java.lang.Object), or 2) are found in an external jar file
which source code types then inherit.

--------------------------------------------------------------------------------
REQUIREMENTS:
--------------------------------------------------------------------------------

 * python3 for running the analyzer * XMind (www.xmind.net) for viewing
 generated mind maps * a bash shell supporting "zip" and "unzip" commands
 for running build scripts * a java source code tree to analyze (this readme
 will use the open source
   cryptography tool portecle as a demo - download portecle from
   http://portecle.sourceforge.net/)


--------------------------------------------------------------------------------
ANALYZER USAGE:
--------------------------------------------------------------------------------

The mindmap_generator.py script takes three arguments:

(from test-repo/py3/org/zerlegen/source_analyzer/)

    ./mindmap_generator.py <src dir> <dep dir> <output xml>

<src dir> - the root directory of the source code tree to analyze
<dep dir> - the root directory containing dependencies to include in the type
            analysis
<output xml> - the output xml file representing the mindmap content which will
               then be built into a complete XMind mind map


For portecle, the included "analyze-portecle.sh" script is included which runs
this command automatically.

--------------------------------------------------------------------------------
GENERATING THE MIND MAP:
--------------------------------------------------------------------------------

Once the analyzer completes, it will write a "content-in.xml" file to the build
directory of the pyXMind package. The complete mind map can then be built with
the following command:

(from test-repo/py3/org/zerlegen/pyXmind/)

    ./build-xmind-book.sh

This will generate a file called "build.xmind" in the ".../pyXmind/build"
directory, which can then be opened with the normal XMind application.

For the portecle demo, this command is run automatically.  build.xmind is
written to the ".../source_analyzer" directory.


   

