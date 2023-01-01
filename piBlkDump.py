
#### pip install requests

import json
import requests
import sys
import re

f = open('piblk.csv', 'w')

args = sys.argv
ll=int(args[1])
nn=int(args[2])
c_tp=0
l_r=[]




l_val=['type','source_account','account','created_at','starting_balance','amount','balance_id','claimant']

s_head=""
for sss in l_val:
  exec("{} = ''".format(sss))
  s_head = s_head + sss + ","

  
s_head=re.sub(',$', '\n', s_head)
#print(s_head)
f.write(s_head)


for num in range(ll,nn+1):
  if num < 2 :
    continue
  url = "https://api.mainnet.minepi.com/ledgers/" + str(num) + "/operations?limit=110"

  #url = "https://api.mainnet.minepi.com/ledgers/4712031/operations"
  session = requests.Session()
  dd = session.get(url)
  #json_data = json.loads(dd.text)
  jd        = json.loads(dd.text)

  #print(dd.text)
  #print(type(dd.text))  #str


  #jd=json_data

  l_r=jd['_embedded']['records']
  if len(l_r) == 0 :
    continue

  #print(l_r)
  #exit


  c_tp=0

  for xx in l_r:
    c_tp=c_tp+1

    

    for sss in  l_val:
      if sss in xx:
        exec("{} = xx['{}']".format(sss, sss))

    s_main=""
    for sss in l_val:
      if sss in xx:
        exec("s_main = s_main + xx['{}'] + ','".format(sss))
      else:
        s_main = s_main + ','

      
    s_main=re.sub(',$', '\n', s_main)
    #print(s_main)
    f.write(s_main)
    print("num,c_tp="+str(num)+", "+str(c_tp) )

    '''
    print(
     str(num) + ", " + str(c_tp) 
     + ", " + type
     + ", " + created_at
     + ", " + source_account
     + ", " + account
     + ", " + starting_balance
    )
    '''



  c_tp=0



f.close()

# 