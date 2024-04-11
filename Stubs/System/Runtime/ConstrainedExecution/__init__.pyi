import typing, abc
from System import Attribute

class Cer(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : Cer # 0
    MayFail : Cer # 1
    Success : Cer # 2


class Consistency(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    MayCorruptProcess : Consistency # 0
    MayCorruptAppDomain : Consistency # 1
    MayCorruptInstance : Consistency # 2
    WillNotCorruptState : Consistency # 3


class CriticalFinalizerObject(abc.ABC):
    pass


class PrePrepareMethodAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class ReliabilityContractAttribute(Attribute):
    def __init__(self, consistencyGuarantee: Consistency, cer: Cer) -> None: ...
    @property
    def Cer(self) -> Cer: ...
    @property
    def ConsistencyGuarantee(self) -> Consistency: ...
    @property
    def TypeId(self) -> typing.Any: ...

