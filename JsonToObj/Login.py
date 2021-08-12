# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = Loginfromdict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast
from datetime import datetime
import dateutil.parser


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


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Result:
    accountId: Optional[int] = None
    regTime: Optional[datetime] = None
    countryCode: Optional[str] = None
    nickname: Optional[str] = None
    email: Optional[str] = None
    token: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Result':
        assert isinstance(obj, dict)
        accountId = from_union([from_none, lambda x: int(from_str(x))], obj.get("accountId"))
        regTime = from_union([from_datetime, from_none], obj.get("regTime"))
        countryCode = from_union([from_str, from_none], obj.get("countryCode"))
        nickname = from_union([from_str, from_none], obj.get("nickname"))
        email = from_union([from_str, from_none], obj.get("email"))
        token = from_union([from_str, from_none], obj.get("token"))
        return Result(accountId, regTime, countryCode, nickname, email, token)

    def to_dict(self) -> dict:
        result: dict = {}
        result["accountId"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.accountId)
        result["regTime"] = from_union([lambda x: x.isoformat(), from_none], self.regTime)
        result["countryCode"] = from_union([from_str, from_none], self.countryCode)
        result["nickname"] = from_union([from_str, from_none], self.nickname)
        result["email"] = from_union([from_str, from_none], self.email)
        result["token"] = from_union([from_str, from_none], self.token)
        return result


@dataclass
class Login:
    errorcode: Optional[int] = None
    result: Optional[Result] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Login':
        assert isinstance(obj, dict)
        errorcode = from_union([from_int, from_none], obj.get("error_code"))
        result = from_union([Result.from_dict, from_none], obj.get("result"))
        return Login(errorcode, result)

    def to_dict(self) -> dict:
        result: dict = {}
        result["error_code"] = from_union([from_int, from_none], self.errorcode)
        result["result"] = from_union([lambda x: to_class(Result, x), from_none], self.result)
        return result


def Loginfromdict(s: Any) -> Login:
    return Login.from_dict(s)


def Logintodict(x: Login) -> Any:
    return to_class(Login, x)
