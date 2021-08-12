import json
from JsonToObj.ListCamera import TapoClassfromdict
from JsonToObj.CameraDetail import CameraDetailfromdict
from JsonToObj.HarddiskInfo import HarddiskInfofromdict
from JsonToObj.PlaybackEvent import PlaybackEventfromdict
from JsonToObj.Login import Loginfromdict
import Funtions as func

class TapoLogin:
    def __init__(self,email,password):
        self.email = email
        self.password = password
        self.__BASE_URL = "https://n-wap-gw.tplinkcloud.com"
        self.__PARAMS = "?appName=TP-Link_Tapo_Android&appVer=2.2.39&netType=wifi&termID=9C-A5-C0-F2-4C-81&ospf=Android%206.0.1&brand=TPLINK&locale=th_TH"


    def getToken(self):
        url = self.__BASE_URL+self.__PARAMS
        payload = "{\"method\":\"login\",\"params\":{\"appType\":\"TP-Link_Tapo_Android\",\"appVersion\":\"2.2.39\",\"cloudPassword\":\""+self.password+"\",\"cloudUserName\":\""+self.email+"\",\"platform\":\"Android 6.0.1\",\"refreshTokenNeeded\":false,\"terminalUUID\":\"9C-A5-C0-F2-4C-81\"}}"
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Content-Length': '250',
            'Host': 'n-wap-gw.tplinkcloud.com',
            'Connection': 'close',
            'Accept-Encoding': 'gzip, deflate',
            'User-Agent': 'okhttp/3.12.12'
        }
        result = Loginfromdict(json.loads(func.getData(url,headers,payload))).result.token
        return result


class Tapo:
    def __init__(self, token):
        self.token = token
        self.__BASE_URL = "https://n-wap-gw.tplinkcloud.com"
        self.__PARAMS = "?appName=TP-Link_Tapo_Android&appVer=2.2.39&netType=wifi&termID=9C-A5-C0-F2-4C-81&ospf=Android%206.0.1&brand=TPLINK&locale=th_TH"

    def getCameraList(self, limit=20):
        url = self.__BASE_URL+self.__PARAMS+"&token="+self.token
        payload = '{"method":"getDeviceListByPage","params":{"deviceTypeList":["SMART.TAPOPLUG","SMART.TAPOBULB","SMART.IPCAMERA"],"index":0,"limit":'+str(
            limit)+'}}'
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Content-Length': '134',
            'Host': 'n-wap-gw.tplinkcloud.com',
            'Connection': 'close',
            'Accept-Encoding': 'gzip, deflate',
            'User-Agent': 'okhttp/3.12.12'
        }
        result = TapoClassfromdict(json.loads(func.getData(url,headers,payload)))
        return result

    def getCameraDetail(self, deviceId):
        url = self.__URL = self.__BASE_URL+self.__PARAMS+"&token="+self.token
        payload = "{\"method\":\"passthrough\",\"params\":{\"deviceId\":\""+str(
            deviceId)+"\",\"requestData\":{\"method\":\"multipleRequest\",\"params\":{\"requests\":[{\"method\":\"getConnectionType\",\"params\":{\"network\":{\"get_connection_type\":\"null\"}}}]}}}}\r\n"
        headers = {
            'Content-Type': 'text/plain'
        }
        result = CameraDetailfromdict(json.loads(func.getData(url,headers,payload)))
        return result

    def getHarddiskInfo(self,deviceId):
        url = self.__URL = self.__BASE_URL+self.__PARAMS+"&token="+self.token
        payload = "{\r\n  \"method\": \"passthrough\",\r\n  \"params\": {\r\n    \"deviceId\": \""+deviceId+"\",\r\n    \"requestData\": {\r\n      \"method\": \"multipleRequest\",\r\n      \"params\": {\r\n        \"requests\": [\r\n                {\r\n                    \"method\": \"getLedStatus\",\r\n                    \"params\": {\r\n                        \"harddisk_manage\": {\r\n                    \"name\": [\r\n                    \"harddisk\"\r\n                    ],\r\n                    \"table\": [\r\n                    \"hd_info\"\r\n                    ]\r\n                }\r\n            }\r\n          }\r\n        ]\r\n      }\r\n    }\r\n  }\r\n}"
        headers = {
            'Content-Type': 'text/plain'
        }
        result = HarddiskInfofromdict(json.loads(func.getData(url,headers,payload)))
        return result

    def getPlaybackEvent(self,deviceId,start_date,end_date):
        url = self.__URL = self.__BASE_URL+self.__PARAMS+"&token="+self.token
        payload = "{\r\n  \"method\": \"passthrough\",\r\n  \"params\": {\r\n    \"deviceId\": \""+deviceId+"\",\r\n    \"requestData\": {\r\n      \"method\": \"multipleRequest\",\r\n      \"params\": {\r\n        \"requests\": [\r\n                {\r\n        \"method\": \"searchDateWithVideo\",\r\n        \"params\": {\r\n          \"playback\": {\r\n            \"search_year_utility\": {\r\n              \"channel\": [\r\n                0\r\n              ],\r\n              \"end_date\": \""+end_date+"\",\r\n              \"start_date\": \""+start_date+"\"\r\n            }\r\n          }\r\n        }\r\n      }\r\n        ]\r\n      }\r\n    }\r\n  }\r\n}"
        headers = {
            'Content-Type': 'text/plain'
        }
        result = PlaybackEventfromdict(json.loads(func.getData(url,headers,payload))).result.responseData.result.responses[0].result.playback.searchresults
        return result