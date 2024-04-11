import abc
from System.Xml.Linq import XAttribute, XElement
from Aml.Engine.CAEX import CAEXWrapper

class XmlCAEXSchema(abc.ABC):
    pass


class XmlLinqExtensions(abc.ABC):
    @staticmethod
    def AddAfterSelf(self: XAttribute, value: XAttribute) -> None: ...
    @staticmethod
    def AddBeforeSelf(self: XAttribute, value: XAttribute) -> None: ...


class XmlOperation(abc.ABC):
    @staticmethod
    def CreateCAEXWrapper(element: XElement) -> CAEXWrapper: ...

