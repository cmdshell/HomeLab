# version >= :Python 3.7.3
# need: mkdir -p conf.d
# author: cmdshell
# To be continue...

import os
import re
import urllib.request
from bs4 import BeautifulSoup

def get_last_line(filename):
    try:
        filesize = os.path.getsize(filename)
        if filesize == 0:
            return None
        else:
            with open(filename, "r", encoding='utf-8') as f1:
                lines = f1.readlines()

            lines[-1] = lines[-1].replace(',','')

            with open(filename, "w", encoding='utf-8') as f2:
                f2.writelines(lines)
                f2.close()

            with open(filename, "r+", encoding='utf-8') as f3:
                content = f3.read()      
                filename = filename.replace('.conf','')  
                f3.seek(0, 0)
                f3.write('define '+filename+' = [\n'+content+'];\n')
                f3.close()

    except FileNotFoundError:
        print(filename + ' not found!')
        return None


china_asn = 'conf.d/china_asn.conf'
telecom_asn = 'conf.d/telecom_asn.conf'
mobile_asn = 'conf.d/mobile_asn.conf'
unicom_asn = 'conf.d/unicom_asn.conf'
education_asn = 'conf.d/education_asn.conf'
broadcasting_asn = 'conf.d/broadcasting_asn.conf'
other_asn = 'conf.d/other_asn.conf'

asn_keyword = {
'telecom': [
'chinanet',
'telecom',
'xinhuanet'
],

'mobile': [
'mobile',
'cmnet',
'tietong',
'cttnet'
],

'unicom': [
'unicom',
'china169',
'cncgroup'
],

'education': [
'education',
'university',
'cernet'
],

'broadcasting': [
'media',
'broadcasting',
'tv'
]

}

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
headers = {'User-Agent': user_agent}

datas_source = 'https://whois.ipip.net/iso/CN'
response = urllib.request.urlopen(datas_source)
#html = response.read().decode('utf-8')

soup = BeautifulSoup(response,'lxml')

table = soup.select('tr')
del table[:1]

for td in table:
    tr = td.select('td')
    ipv4 = tr[2].string.replace(',', '')
    asn = tr[0].a.string.replace('AS', '')
    asn_number = asn + ","
    if int(ipv4) > 0:
        k = 0
        for i,j in asn_keyword.items():
            if i == 'telecom':
                for keyword in asn_keyword[i]:
                    pattern = re.compile(keyword,re.I)
                    match = pattern.search(tr[1].string)
                    if match:
                        with open(telecom_asn, 'a') as f:
                            f.write(asn_number+'\n') 
                        with open(china_asn, 'a') as f:
                            f.write(asn_number+'\n') 
                        k = k+1
                        break
            
            elif i == 'mobile':
                for keyword in asn_keyword[i]:
                    pattern = re.compile(keyword,re.I)
                    match = pattern.search(tr[1].string)
                    if match:
                        with open(mobile_asn, 'a') as f:
                            f.write(asn_number+'\n') 
                        with open(china_asn, 'a') as f:
                            f.write(asn_number+'\n') 
                        k = k+1
                        break

            elif i == 'unicom':
               for keyword in asn_keyword[i]:
                    pattern = re.compile(keyword,re.I)
                    match = pattern.search(tr[1].string)
                    if match:
                        with open(unicom_asn, 'a') as f:
                            f.write(asn_number+'\n') 
                        with open(china_asn, 'a') as f:
                            f.write(asn_number+'\n') 
                        k = k+1
                        break

            elif i == 'education':
               for keyword in asn_keyword[i]:
                    pattern = re.compile(keyword,re.I)
                    match = pattern.search(tr[1].string)
                    if match:
                        with open(education_asn, 'a') as f:
                            f.write(asn_number+'\n') 
                        with open(china_asn, 'a') as f:
                            f.write(asn_number+'\n') 
                        k = k+1
                        break

            elif i == 'broadcasting':
               for keyword in asn_keyword[i]:
                    pattern = re.compile(keyword,re.I)
                    match = pattern.search(tr[1].string)
                    if match:
                        with open(broadcasting_asn, 'a') as f:
                            f.write(asn_number+'\n') 
                        with open(china_asn, 'a') as f:
                            f.write(asn_number+'\n') 
                        k = k+1
                        break

        if k == 0:
            with open(other_asn, 'a') as f:
                f.write(asn_number+'\n') 
            with open(china_asn, 'a') as f:
                f.write(asn_number+'\n') 

get_last_line(telecom_asn)
get_last_line(mobile_asn)
get_last_line(unicom_asn)
get_last_line(education_asn)
get_last_line(broadcasting_asn)
get_last_line(other_asn)
get_last_line(china_asn)









