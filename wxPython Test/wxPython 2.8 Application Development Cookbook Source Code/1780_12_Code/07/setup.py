# Chapter 12: Application Infrastructure,
#             Building and Managing Applications for Distribution
# Recipe 7: Distributing an Application
#
import wx
import sys

#---- Application Information ----#
APP = "FileEditor.py"
NAME = "File Editor"
VERSION = "1.0"
AUTHOR = "Author Name"
AUTHOR_EMAIL = "authorname@someplace.com"
URL = "http://fileeditor_webpage.foo"
LICENSE = "wxWidgets"
YEAR = "2010"

#---- End Application Information ----#

RT_MANIFEST = 24

def BuildPy2Exe():
    """Generate the Py2exe files"""
    from distutils.core import setup
    try:
        import py2exe
    except ImportError:
        print "\n!! You dont have py2exe installed. !!\n"
        exit()

    pyver = sys.version_info[:2]
    if pyver == (2, 6):
        fname = "py26manifest.xml"
    elif pyver == (2, 5):
        fname = "py25manifest.xml"
    else:
        vstr = ".".join(pyver)
        assert False, "Unsupported Python Version %s" % vstr
    with open(fname, 'rb') as handle:
        manifest = handle.read()
        manifest = manifest % dict(prog=NAME)

    OPTS = {"py2exe" : {"compressed" : 1,
                        "optimize" : 1,
                        "bundle_files" : 2,
                        "excludes" : ["Tkinter",],
                        "dll_excludes": ["MSVCP90.dll"]}}
    setup(
        name = NAME,
        version = VERSION,
        options = OPTS,
        windows = [{"script": APP,
                    "icon_resources": [(1, "Icon.ico")],
                    "other_resources" : [(RT_MANIFEST, 1,
                                          manifest)],
                  }],
        description = NAME,
        author = AUTHOR,
        author_email = AUTHOR_EMAIL,
        license = LICENSE,
        url = URL,
        )

def BuildOSXApp():
    """Build the OSX Applet"""
    from setuptools import setup

    # py2app uses this to generate the plist xml for
    # the applet.
    copyright = "Copyright %s %s" % (AUTHOR, YEAR)
    appid = "com.%s.%s" % (NAME, NAME)
    PLIST = dict(CFBundleName = NAME,
             CFBundleIconFile = 'Icon.icns',
             CFBundleShortVersionString = VERSION,
             CFBundleGetInfoString = NAME + " " + VERSION,
             CFBundleExecutable = NAME,
             CFBundleIdentifier = appid,
             CFBundleTypeMIMETypes = ['text/plain',],
             CFBundleDevelopmentRegion = 'English',
             NSHumanReadableCopyright = copyright
             )

    PY2APP_OPTS = dict(iconfile = "Icon.icns",
                       argv_emulation = True,
                       optimize = True,
                       plist = PLIST)

    setup(
        app = [APP,],
        version = VERSION,
        options = dict( py2app = PY2APP_OPTS),
        description = NAME,
        author = AUTHOR,
        author_email = AUTHOR_EMAIL,
        license = LICENSE,
        url = URL,
        setup_requires = ['py2app'],
        )

if __name__ == '__main__':
    if wx.Platform == '__WXMSW__':
        # Windows
        BuildPy2Exe()
    elif wx.Platform == '__WXMAC__':
        # OSX
        BuildOSXApp()
    else:
        print "Unsupported platform: %s" % wx.Platform
