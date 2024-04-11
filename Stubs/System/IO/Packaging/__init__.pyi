import typing, abc
from System import IDisposable, Uri, DateTime
from System.IO import FileAccess, Stream, FileMode, FileShare
from System.Collections.Generic import IEnumerable_1, IEnumerator_1

class CompressionOption(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Normal : CompressionOption # 0
    Maximum : CompressionOption # 1
    Fast : CompressionOption # 2
    SuperFast : CompressionOption # 3
    NotCompressed : CompressionOption # -1


class Package(IDisposable, abc.ABC):
    @property
    def FileOpenAccess(self) -> FileAccess: ...
    @property
    def PackageProperties(self) -> PackageProperties: ...
    def Close(self) -> None: ...
    def DeletePart(self, partUri: Uri) -> None: ...
    def DeleteRelationship(self, id: str) -> None: ...
    def Flush(self) -> None: ...
    def GetPart(self, partUri: Uri) -> PackagePart: ...
    def GetParts(self) -> PackagePartCollection: ...
    def GetRelationship(self, id: str) -> PackageRelationship: ...
    def GetRelationships(self) -> PackageRelationshipCollection: ...
    def GetRelationshipsByType(self, relationshipType: str) -> PackageRelationshipCollection: ...
    def PartExists(self, partUri: Uri) -> bool: ...
    def RelationshipExists(self, id: str) -> bool: ...
    # Skipped CreatePart due to it being static, abstract and generic.

    CreatePart : CreatePart_MethodGroup
    class CreatePart_MethodGroup:
        @typing.overload
        def __call__(self, partUri: Uri, contentType: str) -> PackagePart:...
        @typing.overload
        def __call__(self, partUri: Uri, contentType: str, compressionOption: CompressionOption) -> PackagePart:...

    # Skipped CreateRelationship due to it being static, abstract and generic.

    CreateRelationship : CreateRelationship_MethodGroup
    class CreateRelationship_MethodGroup:
        @typing.overload
        def __call__(self, targetUri: Uri, targetMode: TargetMode, relationshipType: str) -> PackageRelationship:...
        @typing.overload
        def __call__(self, targetUri: Uri, targetMode: TargetMode, relationshipType: str, id: str) -> PackageRelationship:...

    # Skipped Open due to it being static, abstract and generic.

    Open : Open_MethodGroup
    class Open_MethodGroup:
        @typing.overload
        def __call__(self, path: str) -> Package:...
        @typing.overload
        def __call__(self, stream: Stream) -> Package:...
        @typing.overload
        def __call__(self, path: str, packageMode: FileMode) -> Package:...
        @typing.overload
        def __call__(self, stream: Stream, packageMode: FileMode) -> Package:...
        @typing.overload
        def __call__(self, path: str, packageMode: FileMode, packageAccess: FileAccess) -> Package:...
        @typing.overload
        def __call__(self, stream: Stream, packageMode: FileMode, packageAccess: FileAccess) -> Package:...
        @typing.overload
        def __call__(self, path: str, packageMode: FileMode, packageAccess: FileAccess, packageShare: FileShare) -> Package:...



class PackagePart(abc.ABC):
    @property
    def CompressionOption(self) -> CompressionOption: ...
    @property
    def ContentType(self) -> str: ...
    @property
    def Package(self) -> Package: ...
    @property
    def Uri(self) -> Uri: ...
    def DeleteRelationship(self, id: str) -> None: ...
    def GetRelationship(self, id: str) -> PackageRelationship: ...
    def GetRelationships(self) -> PackageRelationshipCollection: ...
    def GetRelationshipsByType(self, relationshipType: str) -> PackageRelationshipCollection: ...
    def RelationshipExists(self, id: str) -> bool: ...
    # Skipped CreateRelationship due to it being static, abstract and generic.

    CreateRelationship : CreateRelationship_MethodGroup
    class CreateRelationship_MethodGroup:
        @typing.overload
        def __call__(self, targetUri: Uri, targetMode: TargetMode, relationshipType: str) -> PackageRelationship:...
        @typing.overload
        def __call__(self, targetUri: Uri, targetMode: TargetMode, relationshipType: str, id: str) -> PackageRelationship:...

    # Skipped GetStream due to it being static, abstract and generic.

    GetStream : GetStream_MethodGroup
    class GetStream_MethodGroup:
        @typing.overload
        def __call__(self) -> Stream:...
        @typing.overload
        def __call__(self, mode: FileMode) -> Stream:...
        @typing.overload
        def __call__(self, mode: FileMode, access: FileAccess) -> Stream:...



class PackagePartCollection(IEnumerable_1[PackagePart]):
    def GetEnumerator(self) -> IEnumerator_1[PackagePart]: ...


class PackageProperties(IDisposable, abc.ABC):
    @property
    def Category(self) -> str: ...
    @Category.setter
    def Category(self, value: str) -> str: ...
    @property
    def ContentStatus(self) -> str: ...
    @ContentStatus.setter
    def ContentStatus(self, value: str) -> str: ...
    @property
    def ContentType(self) -> str: ...
    @ContentType.setter
    def ContentType(self, value: str) -> str: ...
    @property
    def Created(self) -> typing.Optional[DateTime]: ...
    @Created.setter
    def Created(self, value: typing.Optional[DateTime]) -> typing.Optional[DateTime]: ...
    @property
    def Creator(self) -> str: ...
    @Creator.setter
    def Creator(self, value: str) -> str: ...
    @property
    def Description(self) -> str: ...
    @Description.setter
    def Description(self, value: str) -> str: ...
    @property
    def Identifier(self) -> str: ...
    @Identifier.setter
    def Identifier(self, value: str) -> str: ...
    @property
    def Keywords(self) -> str: ...
    @Keywords.setter
    def Keywords(self, value: str) -> str: ...
    @property
    def Language(self) -> str: ...
    @Language.setter
    def Language(self, value: str) -> str: ...
    @property
    def LastModifiedBy(self) -> str: ...
    @LastModifiedBy.setter
    def LastModifiedBy(self, value: str) -> str: ...
    @property
    def LastPrinted(self) -> typing.Optional[DateTime]: ...
    @LastPrinted.setter
    def LastPrinted(self, value: typing.Optional[DateTime]) -> typing.Optional[DateTime]: ...
    @property
    def Modified(self) -> typing.Optional[DateTime]: ...
    @Modified.setter
    def Modified(self, value: typing.Optional[DateTime]) -> typing.Optional[DateTime]: ...
    @property
    def Revision(self) -> str: ...
    @Revision.setter
    def Revision(self, value: str) -> str: ...
    @property
    def Subject(self) -> str: ...
    @Subject.setter
    def Subject(self, value: str) -> str: ...
    @property
    def Title(self) -> str: ...
    @Title.setter
    def Title(self, value: str) -> str: ...
    @property
    def Version(self) -> str: ...
    @Version.setter
    def Version(self, value: str) -> str: ...
    def Dispose(self) -> None: ...


class PackageRelationship:
    @property
    def Id(self) -> str: ...
    @property
    def Package(self) -> Package: ...
    @property
    def RelationshipType(self) -> str: ...
    @property
    def SourceUri(self) -> Uri: ...
    @property
    def TargetMode(self) -> TargetMode: ...
    @property
    def TargetUri(self) -> Uri: ...


class PackageRelationshipCollection(IEnumerable_1[PackageRelationship]):
    def GetEnumerator(self) -> IEnumerator_1[PackageRelationship]: ...


class TargetMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Internal : TargetMode # 0
    External : TargetMode # 1

