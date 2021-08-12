# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = PlaybackEventfromdict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, Dict, TypeVar, Type, Callable, cast


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


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


@dataclass
class SearchResult:
    date: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SearchResult':
        assert isinstance(obj, dict)
        date = from_union([from_none, lambda x: int(from_str(x))], obj.get("date"))
        return SearchResult(date)

    def to_dict(self) -> dict:
        result: dict = {}
        result["date"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.date)
        return result


@dataclass
class Playback:
    searchresults: Optional[List[Dict[str, SearchResult]]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Playback':
        assert isinstance(obj, dict)
        searchresults = from_union([lambda x: from_list(lambda x: from_dict(SearchResult.from_dict, x), x), from_none], obj.get("search_results"))
        return Playback(searchresults)

    def to_dict(self) -> dict:
        result: dict = {}
        result["search_results"] = from_union([lambda x: from_list(lambda x: from_dict(lambda x: to_class(SearchResult, x), x), x), from_none], self.searchresults)
        return result


@dataclass
class ResponseResult:
    playback: Optional[Playback] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResponseResult':
        assert isinstance(obj, dict)
        playback = from_union([Playback.from_dict, from_none], obj.get("playback"))
        return ResponseResult(playback)

    def to_dict(self) -> dict:
        result: dict = {}
        result["playback"] = from_union([lambda x: to_class(Playback, x), from_none], self.playback)
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
class PlaybackEventResult:
    responseData: Optional[ResponseData] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PlaybackEventResult':
        assert isinstance(obj, dict)
        responseData = from_union([ResponseData.from_dict, from_none], obj.get("responseData"))
        return PlaybackEventResult(responseData)

    def to_dict(self) -> dict:
        result: dict = {}
        result["responseData"] = from_union([lambda x: to_class(ResponseData, x), from_none], self.responseData)
        return result


@dataclass
class PlaybackEvent:
    errorcode: Optional[int] = None
    result: Optional[PlaybackEventResult] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PlaybackEvent':
        assert isinstance(obj, dict)
        errorcode = from_union([from_int, from_none], obj.get("error_code"))
        result = from_union([PlaybackEventResult.from_dict, from_none], obj.get("result"))
        return PlaybackEvent(errorcode, result)

    def to_dict(self) -> dict:
        result: dict = {}
        result["error_code"] = from_union([from_int, from_none], self.errorcode)
        result["result"] = from_union([lambda x: to_class(PlaybackEventResult, x), from_none], self.result)
        return result


def PlaybackEventfromdict(s: Any) -> PlaybackEvent:
    return PlaybackEvent.from_dict(s)


def PlaybackEventtodict(x: PlaybackEvent) -> Any:
    return to_class(PlaybackEvent, x)
