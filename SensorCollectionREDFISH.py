#
# AggregationMetricValueCollectionREDFISH. Python script using Redfish API OEM extensoion to get iDRAC sensor collection data.
#
# _author_ = Texas Roemer <Texas_Roemer@Dell.com>
# _version_ = 1.0
#
# Copyright (c) 2019, Dell, Inc.
#
# This software is licensed to you under the GNU General Public License,
# version 2 (GPLv2). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
# along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
#

import requests, json, sys, re, time, os, warnings, argparse

from datetime import datetime

warnings.filterwarnings("ignore")

parser=argparse.ArgumentParser(description="Python script using Redfish API OEM extension to sensor collection data.")
parser.add_argument('-n', help='Get all Dell Numeric Sensor Collection data, pass in \"y\"', required=False)
parser.add_argument('-ps', help='Get all Dell PS(power supply) Numeric Sensor Collection data, pass in \"y\"', required=False)
parser.add_argument('-pss', help='Get all Dell Presence And Status Sensor Collection data, pass in \"y\"', required=False)
parser.add_argument('-s', help='Get all Dell Sensor Collection data, pass in \"y\"', required=False)
args=vars(parser.parse_args())

idrac_ip="185.53.160.137"
idrac_username="root"
idrac_password="T5n1iCoIgS!0k3u22&21"
try:
    os.remove("sensor_collection.txt")
except:
    pass

def check_supported_idrac_version():
    response = requests.get('https://%s/redfish/v1/Dell/Systems/System.Embedded.1/DellNumericSensorCollection' % idrac_ip,verify=False,auth=(idrac_username, idrac_password))
    print(response)
    data = response.json()
    if response.status_code != 200:
        print("\n- WARNING, iDRAC version installed does not support this feature using Redfish API")
        sys.exit()
    else:
        pass

check_supported_idrac_version()
