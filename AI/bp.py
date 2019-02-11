from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import TanhLayer
from pybrain.tools.customxml import NetworkWriter
from pybrain.tools.customxml import NetworkReader
import os
curdir = os.path.dirname(__file__)

"""columns = ['having_IP_Address',
'URL_Length',
'Shortining_Service',
'having_At_Symbol',
'double_slash_redirecting',
'Prefix_Suffix',
'having_Sub_Domain',
'SSLfinal_State',
'Domain_registeration_length',
'Favicon',
'port',
'HTTPS_token',
'Request_URL',
'URL_of_Anchor',
'Links_in_tags',
'SFH',
'Submitting_to_email',
'Abnormal_URL',
'Redirect',
'on_mouseover',
'RightClick',
'popUpWidnow',
'Iframe',
'age_of_domain',
'DNSRecord',
'web_traffic ',
'Page_Rank',
'Google_Index',
'Links_pointing_to_page',
'Statistical_report',
'Result']
"""
net = None
def build_bp():
    global net
    net = NetworkReader.readFrom(os.path.join(curdir,'../collect_data/data/bpstudy.xml'))

def activate_bp(input):
    return net.activate(input)

