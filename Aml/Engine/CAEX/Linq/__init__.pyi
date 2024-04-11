import typing, abc
from System.Collections.Generic import IEnumerable_1
from Aml.Engine.CAEX import ExternalInterfaceType, ExternalInterfaceSequence, InterfaceFamilyType, RoleRequirementsType, CAEXSequence_1, RoleFamilyType, SupportedRoleClassType

class CAEXSequenceExtension(abc.ABC):
    @staticmethod
    def OfInterfaceClass(sequence: ExternalInterfaceSequence, interfaceClass: InterfaceFamilyType) -> IEnumerable_1[ExternalInterfaceType]: ...
    # Skipped OfRoleClass due to it being static, abstract and generic.

    OfRoleClass : OfRoleClass_MethodGroup
    class OfRoleClass_MethodGroup:
        @typing.overload
        def __call__(self, sequence: CAEXSequence_1[RoleRequirementsType], roleClass: RoleFamilyType) -> IEnumerable_1[RoleRequirementsType]:...
        @typing.overload
        def __call__(self, sequence: CAEXSequence_1[SupportedRoleClassType], roleClass: RoleFamilyType) -> IEnumerable_1[SupportedRoleClassType]:...


