# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = TapoClassfromdict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class DeviceList:
    deviceType: Optional[str] = None
    role: Optional[int] = None
    fwVer: Optional[str] = None
    appServerUrl: Optional[str] = None
    deviceRegion: Optional[str] = None
    deviceId: Optional[str] = None
    deviceName: Optional[str] = None
    deviceHwVer: Optional[str] = None
    alias: Optional[str] = None
    deviceMac: Optional[str] = None
    oemId: Optional[str] = None
    deviceModel: Optional[str] = None
    hwId: Optional[str] = None
    fwId: Optional[str] = None
    isSameRegion: Optional[bool] = None
    status: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DeviceList':
        assert isinstance(obj, dict)
        deviceType = from_union([from_str, from_none], obj.get("deviceType"))
        role = from_union([from_int, from_none], obj.get("role"))
        fwVer = from_union([from_str, from_none], obj.get("fwVer"))
        appServerUrl = from_union([from_str, from_none], obj.get("appServerUrl"))
        deviceRegion = from_union([from_str, from_none], obj.get("deviceRegion"))
        deviceId = from_union([from_str, from_none], obj.get("deviceId"))
        deviceName = from_union([from_str, from_none], obj.get("deviceName"))
        deviceHwVer = from_union([from_str, from_none], obj.get("deviceHwVer"))
        alias = from_union([from_str, from_none], obj.get("alias"))
        deviceMac = from_union([from_str, from_none], obj.get("deviceMac"))
        oemId = from_union([from_str, from_none], obj.get("oemId"))
        deviceModel = from_union([from_str, from_none], obj.get("deviceModel"))
        hwId = from_union([from_str, from_none], obj.get("hwId"))
        fwId = from_union([from_str, from_none], obj.get("fwId"))
        isSameRegion = from_union([from_bool, from_none], obj.get("isSameRegion"))
        status = from_union([from_int, from_none], obj.get("status"))
        return DeviceList(deviceType, role, fwVer, appServerUrl, deviceRegion, deviceId, deviceName, deviceHwVer, alias, deviceMac, oemId, deviceModel, hwId, fwId, isSameRegion, status)

    def to_dict(self) -> dict:
        result: dict = {}
        result["deviceType"] = from_union([from_str, from_none], self.deviceType)
        result["role"] = from_union([from_int, from_none], self.role)
        result["fwVer"] = from_union([from_str, from_none], self.fwVer)
        result["appServerUrl"] = from_union([from_str, from_none], self.appServerUrl)
        result["deviceRegion"] = from_union([from_str, from_none], self.deviceRegion)
        result["deviceId"] = from_union([from_str, from_none], self.deviceId)
        result["deviceName"] = from_union([from_str, from_none], self.deviceName)
        result["deviceHwVer"] = from_union([from_str, from_none], self.deviceHwVer)
        result["alias"] = from_union([from_str, from_none], self.alias)
        result["deviceMac"] = from_union([from_str, from_none], self.deviceMac)
        result["oemId"] = from_union([from_str, from_none], self.oemId)
        result["deviceModel"] = from_union([from_str, from_none], self.deviceModel)
        result["hwId"] = from_union([from_str, from_none], self.hwId)
        result["fwId"] = from_union([from_str, from_none], self.fwId)
        result["isSameRegion"] = from_union([from_bool, from_none], self.isSameRegion)
        result["status"] = from_union([from_int, from_none], self.status)
        return result


@dataclass
class Result:
    totalNum: Optional[int] = None
    deviceList: Optional[List[DeviceList]] = None
    currentIndex: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Result':
        assert isinstance(obj, dict)
        totalNum = from_union([from_int, from_none], obj.get("totalNum"))
        deviceList = from_union([lambda x: from_list(DeviceList.from_dict, x), from_none], obj.get("deviceList"))
        currentIndex = from_union([from_int, from_none], obj.get("currentIndex"))
        return Result(totalNum, deviceList, currentIndex)

    def to_dict(self) -> dict:
        result: dict = {}
        result["totalNum"] = from_union([from_int, from_none], self.totalNum)
        result["deviceList"] = from_union([lambda x: from_list(lambda x: to_class(DeviceList, x), x), from_none], self.deviceList)
        result["currentIndex"] = from_union([from_int, from_none], self.currentIndex)
        return result


@dataclass
class TapoClass:
    errorcode: Optional[int] = None
    result: Optional[Result] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TapoClass':
        assert isinstance(obj, dict)
        errorcode = from_union([from_int, from_none], obj.get("error_code"))
        result = from_union([Result.from_dict, from_none], obj.get("result"))
        return TapoClass(errorcode, result)

    def to_dict(self) -> dict:
        result: dict = {}
        result["error_code"] = from_union([from_int, from_none], self.errorcode)
        result["result"] = from_union([lambda x: to_class(Result, x), from_none], self.result)
        return result


def TapoClassfromdict(s: Any) -> TapoClass:
    return TapoClass.from_dict(s)


def TapoClasstodict(x: TapoClass) -> Any:
    return to_class(TapoClass, x)
