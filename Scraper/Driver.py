import pageTurner
from pageTurner import pageTurner_Done 
import URLextractor
from URLextractor import URLextractor_Done
import URL_Sort
from URL_Sort import URL_Sort_Done
import urlFetch
from urlFetch import urlFetch_Done
import fileMover
from fileMover import fileMover_Done  
import fileSort 
from fileSort import fileSort_Done



exec('pageTurner.py').read()

if pageTurner_Done == True:
    exec(open('URLextractor.py')).read()

if URLextractor_Done == True:
    exec(open('URL_Sort.py')).read()

if URL_Sort_Done == True:
    exec(open('urlFetch.py')).read()

if fileMover_Done == True:
    exec(open('fileMover.py')).read()

if fileSort_Done == True:
    exec(open('fileSort.py'))

print("DONE")





