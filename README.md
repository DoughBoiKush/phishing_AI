copyright 2017 phishfeeds Inc
email:phishfeeds@yahoo.com
https://github.com/yanjinjin/phishing_AI.git

# phishing
#apache+wsgi+webpy
yum install apache2
yum install mod_wsgi
yum install python-pip
pip install pythonwhois
pip install lxml
yum install scipy
#webpy 
see http://webpy.org/
#apache conf
see apache_phishing.conf
#close selinux
setenforce 0

#web and check work
python phishing or loading in apache
#spider,analysis,bp etc. task
python schedule.py 
#version
1.0
base on 2017.10.30
2.0
add AI on 2019.02.01
