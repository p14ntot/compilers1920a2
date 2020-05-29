import re

def cb(m):  #dimiourgei sinartisi pou pragmatopoiei antikatastasi twn xaraktirwn &amp;,&gt;,&lt;,nbsp;

  if(m.group(0)=='&amp;'):
    return '&'
 
 elif (m.group(0)=='&gt;'):
    return '>'
 
 elif (m.group(0)=='&lt;'):
    return '<'
 
 elif (m.group(0)=='&nbsp;'):
    return ' '
    
    
