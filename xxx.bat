rem python prCountCreateAccout.py 4818376 118376 > o.csv


rem python pi65B.py 1000
rem python pi65B.py 100000 > o.csv


rem python aaa.py  100000 200000 > o2.csv

rem python aaa.py  6488170 6488172

rem python piBlkDump.py  2 19 > o2.csv

powershell -command "Measure-Command { python piBlkDump.py  2 100000 >log.txt  }



