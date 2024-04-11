import typing, abc
from Aml.Engine.CAEX import CAEXDocument
from System.Xml.Linq import XDocument, XElement, XAttribute
from System import EventArgs, EventHandler_1

class CaexCommand(ICAEXCommand, abc.ABC):
    @property
    def CAEXDocument(self) -> CAEXDocument: ...
    @CAEXDocument.setter
    def CAEXDocument(self, value: CAEXDocument) -> CAEXDocument: ...
    @property
    def DisplayName(self) -> str: ...
    @property
    def XDocument(self) -> XDocument: ...
    @abc.abstractmethod
    def Execute(self) -> None: ...
    @staticmethod
    def OnCAEXElementChangedEvent(document: XDocument, args: CAEXElementChangeEventArgs) -> None: ...
    @staticmethod
    def OnCAEXElementChangingEvent(document: XDocument, args: CAEXElementChangeEventArgs) -> None: ...
    @abc.abstractmethod
    def UnExecute(self) -> None: ...


class CAEXElementChangeEventArgs(EventArgs):
    @typing.overload
    def __init__(self, caexElement: XElement, caexParent: XElement, document: CAEXDocument, attribute: XAttribute, attributeName: str, oldValue: typing.Any, newValue: typing.Any, changeMode: CAEXElementChangeMode) -> None: ...
    @typing.overload
    def __init__(self, caexElement: XElement, caexParent: XElement, document: CAEXDocument, changeMode: CAEXElementChangeMode) -> None: ...
    @property
    def CAEXAttribute(self) -> XAttribute: ...
    @property
    def CAEXAttributeName(self) -> str: ...
    @property
    def CAEXDocument(self) -> CAEXDocument: ...
    @property
    def CAEXElement(self) -> XElement: ...
    @property
    def CAEXParent(self) -> XElement: ...
    @property
    def ChangeMode(self) -> CAEXElementChangeMode: ...
    @property
    def NewValue(self) -> typing.Any: ...
    @property
    def OldValue(self) -> typing.Any: ...


class CAEXElementChangeMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : CAEXElementChangeMode # 0
    Added : CAEXElementChangeMode # 1
    Deleting : CAEXElementChangeMode # 4
    IDChanged : CAEXElementChangeMode # 8
    IDChanging : CAEXElementChangeMode # 16
    IDRefChanged : CAEXElementChangeMode # 32
    IDRefChanging : CAEXElementChangeMode # 64
    NameChanged : CAEXElementChangeMode # 128
    NameChanging : CAEXElementChangeMode # 256
    NameRefChanged : CAEXElementChangeMode # 512
    NameRefChanging : CAEXElementChangeMode # 1024
    PathRefChanged : CAEXElementChangeMode # 2048
    PathRefChanging : CAEXElementChangeMode # 4096
    Deleted : CAEXElementChangeMode # 8192
    ValueChanged : CAEXElementChangeMode # 16384
    ValueChanging : CAEXElementChangeMode # 32768
    Moving : CAEXElementChangeMode # 65536
    ChangingEvent : CAEXElementChangeMode # 103764
    Moved : CAEXElementChangeMode # 131072
    ChangedEvent : CAEXElementChangeMode # 158377


class ICAEXCommand(typing.Protocol):
    @property
    def CAEXDocument(self) -> CAEXDocument: ...
    @property
    def DisplayName(self) -> str: ...
    @abc.abstractmethod
    def Execute(self) -> None: ...
    @abc.abstractmethod
    def UnExecute(self) -> None: ...


class WeakEventSource_GenericClasses(abc.ABCMeta):
    Generic_WeakEventSource_GenericClasses_WeakEventSource_1_TEventArgs = typing.TypeVar('Generic_WeakEventSource_GenericClasses_WeakEventSource_1_TEventArgs')
    def __getitem__(self, types : typing.Type[Generic_WeakEventSource_GenericClasses_WeakEventSource_1_TEventArgs]) -> typing.Type[WeakEventSource_1[Generic_WeakEventSource_GenericClasses_WeakEventSource_1_TEventArgs]]: ...

WeakEventSource : WeakEventSource_GenericClasses

WeakEventSource_1_TEventArgs = typing.TypeVar('WeakEventSource_1_TEventArgs')
class WeakEventSource_1(typing.Generic[WeakEventSource_1_TEventArgs]):
    def __init__(self) -> None: ...
    def Raise(self, sender: typing.Any, e: WeakEventSource_1_TEventArgs) -> None: ...
    def Subscribe(self, handler: EventHandler_1[WeakEventSource_1_TEventArgs]) -> None: ...
    def Unsubscribe(self, handler: EventHandler_1[WeakEventSource_1_TEventArgs]) -> None: ...

