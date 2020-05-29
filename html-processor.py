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
    
 
rexp1 = re.compile('<title>(.+?)</title>') #erwtima1:Ektyposi tou titlou

rexp2 = re.compile('<!--.*?-->',re.DOTALL) #erwtima2: apaloifi sxwliwn

rexp3 = re.compile(r'<(script|style).*?>.*?</(script|style)>',re.DOTALL) #erwtima3: apaloifi tws script kai style tags

rexp4 = re.compile(r'<a.+?href="(.*?)".*?>(.*?)</a>',re.DOTALL) #erwtima4: eksagwgi kai ektypwsi tou syndesmou

rexp51 = re.compile(r'<.+?>|</.+?>',re.DOTALL) #erwtima5.1 :  apaloifi twn  tags typou <>  </>
rexp52 = re.compile(r'<.+?/>',re.DOTALL) #erwtima5.2: apaloifi twn tags typou </>

rexp6 = re.compile(r'&(amp|gt|lt|nbsp);') #erwtima6: metatropi twn eidikwn html entities pou yparxoun sto keimeno

rexp7 = re.compile(r'\s+') #erwtima7: metatropi sinexomenwn xaraktirwn whitespace

with open('testpage.txt','r') as fp: #diavasma keimenou
    
    text = fp.read()
    m = rexp1.search(text) 
    print(m.group(1))
    text = rexp2.sub(' ',text)
    text = rexp3.sub(' ',text)
    for m in rexp4.finditer(text): 
       print('{}    {}'.format(m.group(1),m.group(2)))  
    text = rexp51.sub(' ',text)  
    text = rexp52.sub(' ',text)
    text = rexp6.sub(cb,text)
    text = rexp7.sub(' ',text)
    
    print(text)

