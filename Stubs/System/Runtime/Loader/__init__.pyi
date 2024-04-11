import typing
from System.Reflection import AssemblyName, Assembly
from System.Collections.Generic import IEnumerable_1
from System.IO import Stream
from System import IDisposable

class AssemblyDependencyResolver:
    def __init__(self, componentAssemblyPath: str) -> None: ...
    def ResolveAssemblyToPath(self, assemblyName: AssemblyName) -> str: ...
    def ResolveUnmanagedDllToPath(self, unmanagedDllName: str) -> str: ...


class AssemblyLoadContext:
    def __init__(self, name: str, isCollectible: bool = ...) -> None: ...
    @classmethod
    @property
    def All(cls) -> IEnumerable_1[AssemblyLoadContext]: ...
    @property
    def Assemblies(self) -> IEnumerable_1[Assembly]: ...
    @classmethod
    @property
    def CurrentContextualReflectionContext(cls) -> AssemblyLoadContext: ...
    @classmethod
    @property
    def Default(cls) -> AssemblyLoadContext: ...
    @property
    def IsCollectible(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @staticmethod
    def GetAssemblyName(assemblyPath: str) -> AssemblyName: ...
    @staticmethod
    def GetLoadContext(assembly: Assembly) -> AssemblyLoadContext: ...
    def LoadFromAssemblyName(self, assemblyName: AssemblyName) -> Assembly: ...
    def LoadFromAssemblyPath(self, assemblyPath: str) -> Assembly: ...
    def LoadFromNativeImagePath(self, nativeImagePath: str, assemblyPath: str) -> Assembly: ...
    def SetProfileOptimizationRoot(self, directoryPath: str) -> None: ...
    def StartProfileOptimization(self, profile: str) -> None: ...
    def ToString(self) -> str: ...
    def Unload(self) -> None: ...
    # Skipped EnterContextualReflection due to it being static, abstract and generic.

    EnterContextualReflection : EnterContextualReflection_MethodGroup
    class EnterContextualReflection_MethodGroup:
        @typing.overload
        def __call__(self) -> AssemblyLoadContext.ContextualReflectionScope:...
        @typing.overload
        def __call__(self, activating: Assembly) -> AssemblyLoadContext.ContextualReflectionScope:...

    # Skipped LoadFromStream due to it being static, abstract and generic.

    LoadFromStream : LoadFromStream_MethodGroup
    class LoadFromStream_MethodGroup:
        @typing.overload
        def __call__(self, assembly: Stream) -> Assembly:...
        @typing.overload
        def __call__(self, assembly: Stream, assemblySymbols: Stream) -> Assembly:...


    class ContextualReflectionScope(IDisposable):
        def Dispose(self) -> None: ...

