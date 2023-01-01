
#### pip install requests

import json
import requests
import sys
import re

#f = open('work.csv', 'w')

args = sys.argv
ll=int(args[1])
nn=int(args[2])

l_r=[]





for num in range(ll,nn+1):
#  if num < 2 :
#    continue
  url = "https://api.mainnet.minepi.com/ledgers/" + str(num) + "/operations?limit=110"


  #url = "https://api.mainnet.minepi.com/ledgers/4712031/operations"
  session = requests.Session()
  dd = session.get(url)
  jd = json.loads(dd.text)


  l_r=jd['_embedded']['records']
  num_op = len(l_r)
  if num_op != 0:
    print("num,"+str(num)+",opealation(s),"+str(num_op))


# 