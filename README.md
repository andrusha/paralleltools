[![Build Status](https://secure.travis-ci.org/andrusha/paralleltools.png?branch=master)](http://travis-ci.org/andrusha/paralleltools)

License
=======

This software is free to use and modify, and licensed under MIT License (see LICENSE file).  


About
=====

Parallel tools (named in manner to itertools & functools) is a set of commonly used list traversal functions, which is working in parallel (fault-tolerant) in synchronous or asynchronous manner.  

Implementation is based on python `threading` module, so be aware of GIL.  

Currently implemented functions are (both sync & async):  

* `filter` - filters the list by predicate you provide;   
* `map` - applies a function to each element of the list.  

**Important**: Due to nature of parallel processing the order of results isn't guranteed. Although, function is returns a `list` because the objects you want to process might not be hashable, hence you can't use a `set`.  

Usage
=====

This module is useful if you do I/O-heavy task, e.g. collecting a RSS-feeds or determining if site is alive or not.

Map
---

Synchronous with default parameters:  

```python
import urllib
import paralleltools

feeds = ['http://xkcd.com/rss.xml',
         'http://www.smbc-comics.com/rss.php']

comics = paralleltools.map(urllib.urlopen, feeds)
```

Asynchronous:  

```python
import Image
import logging
import paralleltools

images = ['cat1.jpg', 'cat2.jpg', 'cat3.jpg', ..., 'catN.jpg']

def rotate(img):
	Image.open(img).rotate(720).save(img)
	return img

def done(results):
    logging.info("Yay!")

paralleltools.async_map(rotate, images, threads=20, callback=done)
logging.info("Cats being processed")
```

Filter
------

Synchronous with default parameters:  

```python
import ping
import paralleltools

sites = ['http://github.com',
		 'http://python.org',
		 'http://no-one-read-the-docs-any.way']

def alive(site):
	return ping(site) > 100

result = paralleltools.filter(alive, sites)
```

Asynchronous:  

```python
import lxml
import paralleltools

docs = ['wikileaks_doc1.xml', 'wikileaks_doc2.xml', 'wikileaks_doc3.xml']

def valid(doc):
	try:
		lxml.etree.parse(doc)
		return True
	except lxml.etree.XMLSyntaxError:
		return False

def upload_documents(docs):
	# conspiracy

paralleltools.async_filter(valid, docs, callback=upload_documents)
find_more_documents()  # while these are processed
```

API
---

Methods available:  

* `map`
* `async_map`
* `filter`
* `async_filter`

Parameters:

* `function`
* `iterable`
* `threads` (default = 5)
* `result_callback` (sync) or `callback` (async)

You can create your own workers by extending `AbstractWorker` in `workers.py` module. Or altering supervisor behaviour in `supervisors.py`.