Hal
===

Hal is an XMPP (Jabber) bot for LeanDog's studio.

Installation
------------

First, install [libspotify](http://developer.spotify.com/en/libspotify/overview/).  Copy
the framework into /Libraries/Frameworks

It appears that the setup.py file doesn't support the Mac, since it expects a
static library.  You can get it to build from the [github repository](https://github.com/mopidy/pyspotify)
and build it and install it with:

    sudo CFLAGS=-framework\ libspotify LDFLAGS=-framework\ libspotify python setup.py install

Then, run the following command to fix it up to run:

    sudo install_name_tool -change \
	@loader_path/../Frameworks/libspotify.framework/libspotify \
	/Library/Frameworks/libspotify.framework/libspotify \
	/Library/Python/2.7/site-packages/spotify/_spotify.so

You should then be able to load the spotify module:

    [jason@Max-Neef hal(master)]$ python
    Python 2.7.1 (r271:86832, Jun 16 2011, 16:59:05) 
    [GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import spotify
    >>> 

	
