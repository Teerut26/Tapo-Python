# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = HarddiskInfofromdict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, cast, Callable


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


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


@dataclass
class Harddisk:
    name: Optional[str] = None
    type: Optional[str] = None
    loop: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Harddisk':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get(".name"))
        type = from_union([from_str, from_none], obj.get(".type"))
        loop = from_union([from_str, from_none], obj.get("loop"))
        return Harddisk(name, type, loop)

    def to_dict(self) -> dict:
        result: dict = {}
        result[".name"] = from_union([from_str, from_none], self.name)
        result[".type"] = from_union([from_str, from_none], self.type)
        result["loop"] = from_union([from_str, from_none], self.loop)
        return result


@dataclass
class HDInfo1:
    diskname: Optional[int] = None
    looprecordstatus: Optional[int] = None
    percent: Optional[int] = None
    writeprotect: Optional[int] = None
    recordstarttime: Optional[int] = None
    recordfreeduration: Optional[int] = None
    recordduration: Optional[int] = None
    videototalspace: Optional[str] = None
    msgpushtotalspace: Optional[str] = None
    msgpushfreespace: Optional[str] = None
    type: Optional[str] = None
    picturetotalspace: Optional[str] = None
    detectstatus: Optional[str] = None
    rwattr: Optional[str] = None
    videofreespace: Optional[str] = None
    totalspace: Optional[str] = None
    picturefreespace: Optional[str] = None
    freespace: Optional[str] = None
    status: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'HDInfo1':
        assert isinstance(obj, dict)
        diskname = from_union([from_none, lambda x: int(from_str(x))], obj.get("disk_name"))
        looprecordstatus = from_union([from_none, lambda x: int(from_str(x))], obj.get("loop_record_status"))
        percent = from_union([from_none, lambda x: int(from_str(x))], obj.get("percent"))
        writeprotect = from_union([from_none, lambda x: int(from_str(x))], obj.get("write_protect"))
        recordstarttime = from_union([from_none, lambda x: int(from_str(x))], obj.get("record_start_time"))
        recordfreeduration = from_union([from_none, lambda x: int(from_str(x))], obj.get("record_free_duration"))
        recordduration = from_union([from_none, lambda x: int(from_str(x))], obj.get("record_duration"))
        videototalspace = from_union([from_str, from_none], obj.get("video_total_space"))
        msgpushtotalspace = from_union([from_str, from_none], obj.get("msg_push_total_space"))
        msgpushfreespace = from_union([from_str, from_none], obj.get("msg_push_free_space"))
        type = from_union([from_str, from_none], obj.get("type"))
        picturetotalspace = from_union([from_str, from_none], obj.get("picture_total_space"))
        detectstatus = from_union([from_str, from_none], obj.get("detect_status"))
        rwattr = from_union([from_str, from_none], obj.get("rw_attr"))
        videofreespace = from_union([from_str, from_none], obj.get("video_free_space"))
        totalspace = from_union([from_str, from_none], obj.get("total_space"))
        picturefreespace = from_union([from_str, from_none], obj.get("picture_free_space"))
        freespace = from_union([from_str, from_none], obj.get("free_space"))
        status = from_union([from_str, from_none], obj.get("status"))
        return HDInfo1(diskname, looprecordstatus, percent, writeprotect, recordstarttime, recordfreeduration, recordduration, videototalspace, msgpushtotalspace, msgpushfreespace, type, picturetotalspace, detectstatus, rwattr, videofreespace, totalspace, picturefreespace, freespace, status)

    def to_dict(self) -> dict:
        result: dict = {}
        result["disk_name"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.diskname)
        result["loop_record_status"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.looprecordstatus)
        result["percent"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.percent)
        result["write_protect"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.writeprotect)
        result["record_start_time"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.recordstarttime)
        result["record_free_duration"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.recordfreeduration)
        result["record_duration"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.recordduration)
        result["video_total_space"] = from_union([from_str, from_none], self.videototalspace)
        result["msg_push_total_space"] = from_union([from_str, from_none], self.msgpushtotalspace)
        result["msg_push_free_space"] = from_union([from_str, from_none], self.msgpushfreespace)
        result["type"] = from_union([from_str, from_none], self.type)
        result["picture_total_space"] = from_union([from_str, from_none], self.picturetotalspace)
        result["detect_status"] = from_union([from_str, from_none], self.detectstatus)
        result["rw_attr"] = from_union([from_str, from_none], self.rwattr)
        result["video_free_space"] = from_union([from_str, from_none], self.videofreespace)
        result["total_space"] = from_union([from_str, from_none], self.totalspace)
        result["picture_free_space"] = from_union([from_str, from_none], self.picturefreespace)
        result["free_space"] = from_union([from_str, from_none], self.freespace)
        result["status"] = from_union([from_str, from_none], self.status)
        return result


@dataclass
class HDInfo:
    hdinfo1: Optional[HDInfo1] = None

    @staticmethod
    def from_dict(obj: Any) -> 'HDInfo':
        assert isinstance(obj, dict)
        hdinfo1 = from_union([HDInfo1.from_dict, from_none], obj.get("hd_info_1"))
        return HDInfo(hdinfo1)

    def to_dict(self) -> dict:
        result: dict = {}
        result["hd_info_1"] = from_union([lambda x: to_class(HDInfo1, x), from_none], self.hdinfo1)
        return result


@dataclass
class HarddiskManage:
    harddisk: Optional[Harddisk] = None
    hdinfo: Optional[List[HDInfo]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'HarddiskManage':
        assert isinstance(obj, dict)
        harddisk = from_union([Harddisk.from_dict, from_none], obj.get("harddisk"))
        hdinfo = from_union([lambda x: from_list(HDInfo.from_dict, x), from_none], obj.get("hd_info"))
        return HarddiskManage(harddisk, hdinfo)

    def to_dict(self) -> dict:
        result: dict = {}
        result["harddisk"] = from_union([lambda x: to_class(Harddisk, x), from_none], self.harddisk)
        result["hd_info"] = from_union([lambda x: from_list(lambda x: to_class(HDInfo, x), x), from_none], self.hdinfo)
        return result


@dataclass
class ResponseResult:
    harddiskmanage: Optional[HarddiskManage] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResponseResult':
        assert isinstance(obj, dict)
        harddiskmanage = from_union([HarddiskManage.from_dict, from_none], obj.get("harddisk_manage"))
        return ResponseResult(harddiskmanage)

    def to_dict(self) -> dict:
        result: dict = {}
        result["harddisk_manage"] = from_union([lambda x: to_class(HarddiskManage, x), from_none], self.harddiskmanage)
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
class HarddiskInfoResult:
    responseData: Optional[ResponseData] = None

    @staticmethod
    def from_dict(obj: Any) -> 'HarddiskInfoResult':
        assert isinstance(obj, dict)
        responseData = from_union([ResponseData.from_dict, from_none], obj.get("responseData"))
        return HarddiskInfoResult(responseData)

    def to_dict(self) -> dict:
        result: dict = {}
        result["responseData"] = from_union([lambda x: to_class(ResponseData, x), from_none], self.responseData)
        return result


@dataclass
class HarddiskInfo:
    errorcode: Optional[int] = None
    result: Optional[HarddiskInfoResult] = None

    @staticmethod
    def from_dict(obj: Any) -> 'HarddiskInfo':
        assert isinstance(obj, dict)
        errorcode = from_union([from_int, from_none], obj.get("error_code"))
        result = from_union([HarddiskInfoResult.from_dict, from_none], obj.get("result"))
        return HarddiskInfo(errorcode, result)

    def to_dict(self) -> dict:
        result: dict = {}
        result["error_code"] = from_union([from_int, from_none], self.errorcode)
        result["result"] = from_union([lambda x: to_class(HarddiskInfoResult, x), from_none], self.result)
        return result


def HarddiskInfofromdict(s: Any) -> HarddiskInfo:
    return HarddiskInfo.from_dict(s)


def HarddiskInfotodict(x: HarddiskInfo) -> Any:
    return to_class(HarddiskInfo, x)
