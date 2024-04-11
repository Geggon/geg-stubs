import typing, clr, abc
from System import Attribute, Array, Array_1, IDisposable, SystemException, Exception
from System.Collections import ICollection, IEnumerator, Hashtable, ArrayList, IDictionary
from System.Runtime.Serialization import IDeserializationCallback, SerializationInfo, StreamingContext
from System.Security.Permissions import PermissionState
from System.Reflection import AssemblyName, MethodInfo, MethodBase

class AllowPartiallyTrustedCallersAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def PartialTrustVisibilityLevel(self) -> PartialTrustVisibilityLevel: ...
    @PartialTrustVisibilityLevel.setter
    def PartialTrustVisibilityLevel(self, value: PartialTrustVisibilityLevel) -> PartialTrustVisibilityLevel: ...
    @property
    def TypeId(self) -> typing.Any: ...


class IPermission(ISecurityEncodable, typing.Protocol):
    @abc.abstractmethod
    def Copy(self) -> IPermission: ...
    @abc.abstractmethod
    def Demand(self) -> None: ...
    @abc.abstractmethod
    def Intersect(self, target: IPermission) -> IPermission: ...
    @abc.abstractmethod
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    @abc.abstractmethod
    def Union(self, target: IPermission) -> IPermission: ...


class ISecurityEncodable(typing.Protocol):
    @abc.abstractmethod
    def FromXml(self, e: SecurityElement) -> None: ...
    @abc.abstractmethod
    def ToXml(self) -> SecurityElement: ...


class IStackWalk(typing.Protocol):
    @abc.abstractmethod
    def Assert(self) -> None: ...
    @abc.abstractmethod
    def Demand(self) -> None: ...
    @abc.abstractmethod
    def Deny(self) -> None: ...
    @abc.abstractmethod
    def PermitOnly(self) -> None: ...


class PartialTrustVisibilityLevel(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    VisibleToAllHosts : PartialTrustVisibilityLevel # 0
    NotVisibleByDefault : PartialTrustVisibilityLevel # 1


class PermissionSet(ICollection, IStackWalk, ISecurityEncodable, IDeserializationCallback):
    @typing.overload
    def __init__(self, permSet: PermissionSet) -> None: ...
    @typing.overload
    def __init__(self, state: PermissionState) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsReadOnly(self) -> bool: ...
    @property
    def IsSynchronized(self) -> bool: ...
    @property
    def SyncRoot(self) -> typing.Any: ...
    def AddPermission(self, perm: IPermission) -> IPermission: ...
    def Assert(self) -> None: ...
    def ContainsNonCodeAccessPermissions(self) -> bool: ...
    @staticmethod
    def ConvertPermissionSet(inFormat: str, inData: Array_1[int], outFormat: str) -> Array_1[int]: ...
    def Copy(self) -> PermissionSet: ...
    def CopyTo(self, array: Array, index: int) -> None: ...
    def Demand(self) -> None: ...
    def Deny(self) -> None: ...
    def Equals(self, o: typing.Any) -> bool: ...
    def FromXml(self, et: SecurityElement) -> None: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def GetHashCode(self) -> int: ...
    def GetPermission(self, permClass: typing.Type[typing.Any]) -> IPermission: ...
    def Intersect(self, other: PermissionSet) -> PermissionSet: ...
    def IsEmpty(self) -> bool: ...
    def IsSubsetOf(self, target: PermissionSet) -> bool: ...
    def IsUnrestricted(self) -> bool: ...
    def PermitOnly(self) -> None: ...
    def RemovePermission(self, permClass: typing.Type[typing.Any]) -> IPermission: ...
    @staticmethod
    def RevertAssert() -> None: ...
    def SetPermission(self, perm: IPermission) -> IPermission: ...
    def ToString(self) -> str: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, other: PermissionSet) -> PermissionSet: ...


class SecureString(IDisposable):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, value: clr.Reference[str], length: int) -> None: ...
    @property
    def Length(self) -> int: ...
    def AppendChar(self, c: str) -> None: ...
    def Clear(self) -> None: ...
    def Copy(self) -> SecureString: ...
    def Dispose(self) -> None: ...
    def InsertAt(self, index: int, c: str) -> None: ...
    def IsReadOnly(self) -> bool: ...
    def MakeReadOnly(self) -> None: ...
    def RemoveAt(self, index: int) -> None: ...
    def SetAt(self, index: int, c: str) -> None: ...


class SecurityCriticalAttribute(Attribute):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, scope: SecurityCriticalScope) -> None: ...
    @property
    def Scope(self) -> SecurityCriticalScope: ...
    @property
    def TypeId(self) -> typing.Any: ...


class SecurityCriticalScope(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Explicit : SecurityCriticalScope # 0
    Everything : SecurityCriticalScope # 1


class SecurityElement:
    @typing.overload
    def __init__(self, tag: str) -> None: ...
    @typing.overload
    def __init__(self, tag: str, text: str) -> None: ...
    @property
    def Attributes(self) -> Hashtable: ...
    @Attributes.setter
    def Attributes(self, value: Hashtable) -> Hashtable: ...
    @property
    def Children(self) -> ArrayList: ...
    @Children.setter
    def Children(self, value: ArrayList) -> ArrayList: ...
    @property
    def Tag(self) -> str: ...
    @Tag.setter
    def Tag(self, value: str) -> str: ...
    @property
    def Text(self) -> str: ...
    @Text.setter
    def Text(self, value: str) -> str: ...
    def AddAttribute(self, name: str, value: str) -> None: ...
    def AddChild(self, child: SecurityElement) -> None: ...
    def Attribute(self, name: str) -> str: ...
    def Copy(self) -> SecurityElement: ...
    def Equal(self, other: SecurityElement) -> bool: ...
    @staticmethod
    def Escape(str: str) -> str: ...
    @staticmethod
    def FromString(xml: str) -> SecurityElement: ...
    @staticmethod
    def IsValidAttributeName(name: str) -> bool: ...
    @staticmethod
    def IsValidAttributeValue(value: str) -> bool: ...
    @staticmethod
    def IsValidTag(tag: str) -> bool: ...
    @staticmethod
    def IsValidText(text: str) -> bool: ...
    def SearchForChildByTag(self, tag: str) -> SecurityElement: ...
    def SearchForTextOfTag(self, tag: str) -> str: ...
    def ToString(self) -> str: ...


class SecurityException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
    @typing.overload
    def __init__(self, message: str, type: typing.Type[typing.Any]) -> None: ...
    @typing.overload
    def __init__(self, message: str, type: typing.Type[typing.Any], state: str) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def Demanded(self) -> typing.Any: ...
    @Demanded.setter
    def Demanded(self, value: typing.Any) -> typing.Any: ...
    @property
    def DenySetInstance(self) -> typing.Any: ...
    @DenySetInstance.setter
    def DenySetInstance(self, value: typing.Any) -> typing.Any: ...
    @property
    def FailedAssemblyInfo(self) -> AssemblyName: ...
    @FailedAssemblyInfo.setter
    def FailedAssemblyInfo(self, value: AssemblyName) -> AssemblyName: ...
    @property
    def GrantedSet(self) -> str: ...
    @GrantedSet.setter
    def GrantedSet(self, value: str) -> str: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Method(self) -> MethodInfo: ...
    @Method.setter
    def Method(self, value: MethodInfo) -> MethodInfo: ...
    @property
    def PermissionState(self) -> str: ...
    @PermissionState.setter
    def PermissionState(self, value: str) -> str: ...
    @property
    def PermissionType(self) -> typing.Type[typing.Any]: ...
    @PermissionType.setter
    def PermissionType(self, value: typing.Type[typing.Any]) -> typing.Type[typing.Any]: ...
    @property
    def PermitOnlySetInstance(self) -> typing.Any: ...
    @PermitOnlySetInstance.setter
    def PermitOnlySetInstance(self, value: typing.Any) -> typing.Any: ...
    @property
    def RefusedSet(self) -> str: ...
    @RefusedSet.setter
    def RefusedSet(self, value: str) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...
    @property
    def Url(self) -> str: ...
    @Url.setter
    def Url(self, value: str) -> str: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...
    def ToString(self) -> str: ...


class SecurityRulesAttribute(Attribute):
    def __init__(self, ruleSet: SecurityRuleSet) -> None: ...
    @property
    def RuleSet(self) -> SecurityRuleSet: ...
    @property
    def SkipVerificationInFullTrust(self) -> bool: ...
    @SkipVerificationInFullTrust.setter
    def SkipVerificationInFullTrust(self, value: bool) -> bool: ...
    @property
    def TypeId(self) -> typing.Any: ...


class SecurityRuleSet(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : SecurityRuleSet # 0
    Level1 : SecurityRuleSet # 1
    Level2 : SecurityRuleSet # 2


class SecuritySafeCriticalAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class SecurityTransparentAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class SecurityTreatAsSafeAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class SuppressUnmanagedCodeSecurityAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class UnverifiableCodeAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class VerificationException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...

