import gzip, glob
from lxml import etree

def cowfiles(path='./'):
    "Wrapper for the glob module."
    return glob.glob(path+'*.xml.gz')

def sentence_generator(filename,separate=True,gzipped=True):
    """Returns metadata and the sentence: [(words),(tags),(lemmas)]
    
    Arguments
    ---------
    filename: filename
    separate: if False, changes sentence format to [(w1,t1,l1),(w2,t2,l2),...]
    gzipped : assumes the file is gzipped. Change to False for unpacked files
    """
    source = gzip.GzipFile(filename) if gzipped else filename
    parser = etree.iterparse(source,html=True)
    for x,y in parser:
        try:
            trips = [w.split('\t') for w in y.text.strip().split('\n')]
            yield y.attrib, zip(*trips) if separate else trips
        except AttributeError:
            print('No text for this element!')
            pass
        y.clear()
        for ancestor in y.xpath('ancestor-or-self::*'):
            while ancestor.getprevious() is not None:
                del ancestor.getparent()[0]

def sentences_for_dir(path='./',separate=True,gzipped=True):
    """Sentence generator for an entire corpus directory.
    Returns metadata and the sentence: [(words),(tags),(lemmas)]
    
    Arguments
    ---------
    path    : path to the COW files
    separate: if False, changes sentence format to [(w1,t1,l1),(w2,t2,l2),...]
    gzipped : assumes the file is gzipped. Change to False for unpacked files
    """
    for filename in cowfiles(path):
        for metadata, data in sentence_generator(filename,separate,gzipped):
            yield metadata, data
