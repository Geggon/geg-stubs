import typing, abc

class IJsonOnDeserialized(typing.Protocol):
    @abc.abstractmethod
    def OnDeserialized(self) -> None: ...

