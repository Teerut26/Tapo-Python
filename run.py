import requests
from Modules import Tapo,TapoLogin

#email and password of Tapo Account
token = TapoLogin(email, password)
tapo = Tapo(token)

def main():
    print(tapo.getHarddiskInfo(deviceId))
    print(tapo.getPlaybackEvent(deviceId, start_date, end_date))
    ListCamera()
    # CameraDetail()
    # print(token.getToken())


def ListCamera():
    result = tapo.getCameraList(limit=20)
    print(f"=================================")
    for data in result.result.deviceList:
        print(f"Name : {data.alias}")
        print(f"DeviceName : {data.deviceName}")
        print(f"DeviceHwVer : {data.deviceHwVer}")
        print(f"FwVer : {data.fwVer}")
        print(f"DeviceType : {data.deviceType}")
        print(f"DeviceId : {data.deviceId}")
        if(data.status != 0):
            print(f"Status : Online")
        else:
            print(f"Status : Offline")
        print(f"=================================")

def CameraDetail():
    result = tapo.getCameraDetail(deviceId)
    print(result.result.responseData.result.responses[0])

if __name__ == "__main__":
    main()