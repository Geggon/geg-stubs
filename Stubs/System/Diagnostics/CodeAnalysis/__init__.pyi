import typing
from System import Attribute, Array_1

class AllowNullAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class DisallowNullAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class DoesNotReturnAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class DoesNotReturnIfAttribute(Attribute):
    def __init__(self, parameterValue: bool) -> None: ...
    @property
    def ParameterValue(self) -> bool: ...
    @property
    def TypeId(self) -> typing.Any: ...


class DynamicallyAccessedMembersAttribute(Attribute):
    def __init__(self, memberTypes: DynamicallyAccessedMemberTypes) -> None: ...
    @property
    def MemberTypes(self) -> DynamicallyAccessedMemberTypes: ...
    @property
    def TypeId(self) -> typing.Any: ...


class DynamicallyAccessedMemberTypes(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : DynamicallyAccessedMemberTypes # 0
    PublicParameterlessConstructor : DynamicallyAccessedMemberTypes # 1
    PublicConstructors : DynamicallyAccessedMemberTypes # 3
    NonPublicConstructors : DynamicallyAccessedMemberTypes # 4
    PublicMethods : DynamicallyAccessedMemberTypes # 8
    NonPublicMethods : DynamicallyAccessedMemberTypes # 16
    PublicFields : DynamicallyAccessedMemberTypes # 32
    NonPublicFields : DynamicallyAccessedMemberTypes # 64
    PublicNestedTypes : DynamicallyAccessedMemberTypes # 128
    NonPublicNestedTypes : DynamicallyAccessedMemberTypes # 256
    PublicProperties : DynamicallyAccessedMemberTypes # 512
    NonPublicProperties : DynamicallyAccessedMemberTypes # 1024
    PublicEvents : DynamicallyAccessedMemberTypes # 2048
    NonPublicEvents : DynamicallyAccessedMemberTypes # 4096
    Interfaces : DynamicallyAccessedMemberTypes # 8192
    All : DynamicallyAccessedMemberTypes # -1


class DynamicDependencyAttribute(Attribute):
    @typing.overload
    def __init__(self, memberSignature: str) -> None: ...
    @typing.overload
    def __init__(self, memberSignature: str, type: typing.Type[typing.Any]) -> None: ...
    @typing.overload
    def __init__(self, memberSignature: str, typeName: str, assemblyName: str) -> None: ...
    @typing.overload
    def __init__(self, memberTypes: DynamicallyAccessedMemberTypes, type: typing.Type[typing.Any]) -> None: ...
    @typing.overload
    def __init__(self, memberTypes: DynamicallyAccessedMemberTypes, typeName: str, assemblyName: str) -> None: ...
    @property
    def AssemblyName(self) -> str: ...
    @property
    def Condition(self) -> str: ...
    @Condition.setter
    def Condition(self, value: str) -> str: ...
    @property
    def MemberSignature(self) -> str: ...
    @property
    def MemberTypes(self) -> DynamicallyAccessedMemberTypes: ...
    @property
    def Type(self) -> typing.Type[typing.Any]: ...
    @property
    def TypeId(self) -> typing.Any: ...
    @property
    def TypeName(self) -> str: ...


class ExcludeFromCodeCoverageAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def Justification(self) -> str: ...
    @Justification.setter
    def Justification(self, value: str) -> str: ...
    @property
    def TypeId(self) -> typing.Any: ...


class MaybeNullAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class MaybeNullWhenAttribute(Attribute):
    def __init__(self, returnValue: bool) -> None: ...
    @property
    def ReturnValue(self) -> bool: ...
    @property
    def TypeId(self) -> typing.Any: ...


class MemberNotNullAttribute(Attribute):
    @typing.overload
    def __init__(self, member: str) -> None: ...
    @typing.overload
    def __init__(self, members: Array_1[str]) -> None: ...
    @property
    def Members(self) -> Array_1[str]: ...
    @property
    def TypeId(self) -> typing.Any: ...


class MemberNotNullWhenAttribute(Attribute):
    @typing.overload
    def __init__(self, returnValue: bool, member: str) -> None: ...
    @typing.overload
    def __init__(self, returnValue: bool, members: Array_1[str]) -> None: ...
    @property
    def Members(self) -> Array_1[str]: ...
    @property
    def ReturnValue(self) -> bool: ...
    @property
    def TypeId(self) -> typing.Any: ...


class NotNullAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class NotNullIfNotNullAttribute(Attribute):
    def __init__(self, parameterName: str) -> None: ...
    @property
    def ParameterName(self) -> str: ...
    @property
    def TypeId(self) -> typing.Any: ...


class NotNullWhenAttribute(Attribute):
    def __init__(self, returnValue: bool) -> None: ...
    @property
    def ReturnValue(self) -> bool: ...
    @property
    def TypeId(self) -> typing.Any: ...


class RequiresAssemblyFilesAttribute(Attribute):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @property
    def Message(self) -> str: ...
    @property
    def TypeId(self) -> typing.Any: ...
    @property
    def Url(self) -> str: ...
    @Url.setter
    def Url(self, value: str) -> str: ...


class RequiresUnreferencedCodeAttribute(Attribute):
    def __init__(self, message: str) -> None: ...
    @property
    def Message(self) -> str: ...
    @property
    def TypeId(self) -> typing.Any: ...
    @property
    def Url(self) -> str: ...
    @Url.setter
    def Url(self, value: str) -> str: ...


class SuppressMessageAttribute(Attribute):
    def __init__(self, category: str, checkId: str) -> None: ...
    @property
    def Category(self) -> str: ...
    @property
    def CheckId(self) -> str: ...
    @property
    def Justification(self) -> str: ...
    @Justification.setter
    def Justification(self, value: str) -> str: ...
    @property
    def MessageId(self) -> str: ...
    @MessageId.setter
    def MessageId(self, value: str) -> str: ...
    @property
    def Scope(self) -> str: ...
    @Scope.setter
    def Scope(self, value: str) -> str: ...
    @property
    def Target(self) -> str: ...
    @Target.setter
    def Target(self, value: str) -> str: ...
    @property
    def TypeId(self) -> typing.Any: ...


class UnconditionalSuppressMessageAttribute(Attribute):
    def __init__(self, category: str, checkId: str) -> None: ...
    @property
    def Category(self) -> str: ...
    @property
    def CheckId(self) -> str: ...
    @property
    def Justification(self) -> str: ...
    @Justification.setter
    def Justification(self, value: str) -> str: ...
    @property
    def MessageId(self) -> str: ...
    @MessageId.setter
    def MessageId(self, value: str) -> str: ...
    @property
    def Scope(self) -> str: ...
    @Scope.setter
    def Scope(self, value: str) -> str: ...
    @property
    def Target(self) -> str: ...
    @Target.setter
    def Target(self, value: str) -> str: ...
    @property
    def TypeId(self) -> typing.Any: ...

