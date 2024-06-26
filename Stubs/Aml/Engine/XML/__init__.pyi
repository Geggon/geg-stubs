import typing, abc
from System.Xml.Linq import XDocument, XElement, XName, XNode
from System.IO import Stream
from System import IDisposable

class IDocument(typing.Protocol):
    @property
    def XDocument(self) -> XDocument: ...
    @abc.abstractmethod
    def SaveToStream(self, prettyPrint: bool) -> Stream: ...


class IXMLWrapper(typing.Protocol):
    @property
    def Document(self) -> XDocument: ...
    @property
    def Exists(self) -> bool: ...
    @property
    def Node(self) -> XElement: ...
    @property
    def Owner(self) -> XElement: ...
    @property
    def TagName(self) -> str: ...


class XDocumentWrapper(IDisposable, IDocument):
    @property
    def XDocument(self) -> XDocument: ...
    @XDocument.setter
    def XDocument(self, value: XDocument) -> XDocument: ...
    def Dispose(self) -> None: ...
    def SaveToFile(self, filename: str, prettyPrint: bool) -> None: ...
    def SaveToStream(self, prettyPrint: bool) -> Stream: ...
    def Unload(self) -> None: ...
    def XName(self, tagname: str) -> XName: ...
    # Skipped Document due to it being static, abstract and generic.

    Document : Document_MethodGroup
    class Document_MethodGroup:
        @typing.overload
        def __call__(self, node: XNode) -> IDocument:...
        @typing.overload
        def __call__(self, xObject: IXMLWrapper) -> IDocument:...


