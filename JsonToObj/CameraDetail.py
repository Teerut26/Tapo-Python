# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = CameraDetailfromdict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, cast, Callable


T = TypeVar("T")


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
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


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


@dataclass
class ResponseResult:
    rssi: Optional[int] = None
    linktype: Optional[str] = None
    rssiValue: Optional[int] = None
    ssid: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResponseResult':
        assert isinstance(obj, dict)
        rssi = from_union([from_none, lambda x: int(from_str(x))], obj.get("rssi"))
        linktype = from_union([from_str, from_none], obj.get("link_type"))
        rssiValue = from_union([from_int, from_none], obj.get("rssiValue"))
        ssid = from_union([from_str, from_none], obj.get("ssid"))
        return ResponseResult(rssi, linktype, rssiValue, ssid)

    def to_dict(self) -> dict:
        result: dict = {}
        result["rssi"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.rssi)
        result["link_type"] = from_union([from_str, from_none], self.linktype)
        result["rssiValue"] = from_union([from_int, from_none], self.rssiValue)
        result["ssid"] = from_union([from_str, from_none], self.ssid)
        return result


@dataclass
class Response:
    result: Optional[ResponseResult] = None
    method: Optional[str] = None
    errorcode: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Response':
        assert isinstance(obj, dict)
        result = from_union([ResponseResult.from_dict, from_none], obj.get("result"))
        method = from_union([from_str, from_none], obj.get("method"))
        errorcode = from_union([from_int, from_none], obj.get("error_code"))
        return Response(result, method, errorcode)

    def to_dict(self) -> dict:
        result: dict = {}
        result["result"] = from_union([lambda x: to_class(ResponseResult, x), from_none], self.result)
        result["method"] = from_union([from_str, from_none], self.method)
        result["error_code"] = from_union([from_int, from_none], self.errorcode)
        return result


@dataclass
class ResponseDataResult:
    responses: Optional[List[Response]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResponseDataResult':
        assert isinstance(obj, dict)
        responses = from_union([lambda x: from_list(Response.from_dict, x), from_none], obj.get("responses"))
        return ResponseDataResult(responses)

    def to_dict(self) -> dict:
        result: dict = {}
        result["responses"] = from_union([lambda x: from_list(lambda x: to_class(Response, x), x), from_none], self.responses)
        return result


@dataclass
class ResponseData:
    result: Optional[ResponseDataResult] = None
    errorcode: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResponseData':
        assert isinstance(obj, dict)
        result = from_union([ResponseDataResult.from_dict, from_none], obj.get("result"))
        errorcode = from_union([from_int, from_none], obj.get("error_code"))
        return ResponseData(result, errorcode)

    def to_dict(self) -> dict:
        result: dict = {}
        result["result"] = from_union([lambda x: to_class(ResponseDataResult, x), from_none], self.result)
        result["error_code"] = from_union([from_int, from_none], self.errorcode)
        return result


@dataclass
class CameraDetailResult:
    responseData: Optional[ResponseData] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CameraDetailResult':
        assert isinstance(obj, dict)
        responseData = from_union([ResponseData.from_dict, from_none], obj.get("responseData"))
        return CameraDetailResult(responseData)

    def to_dict(self) -> dict:
        result: dict = {}
        result["responseData"] = from_union([lambda x: to_class(ResponseData, x), from_none], self.responseData)
        return result


@dataclass
class CameraDetail:
    errorcode: Optional[int] = None
    result: Optional[CameraDetailResult] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CameraDetail':
        assert isinstance(obj, dict)
        errorcode = from_union([from_int, from_none], obj.get("error_code"))
        result = from_union([CameraDetailResult.from_dict, from_none], obj.get("result"))
        return CameraDetail(errorcode, result)

    def to_dict(self) -> dict:
        result: dict = {}
        result["error_code"] = from_union([from_int, from_none], self.errorcode)
        result["result"] = from_union([lambda x: to_class(CameraDetailResult, x), from_none], self.result)
        return result


def CameraDetailfromdict(s: Any) -> CameraDetail:
    return CameraDetail.from_dict(s)


def CameraDetailtodict(x: CameraDetail) -> Any:
    return to_class(CameraDetail, x)
