from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reference import Reference


T = TypeVar("T", bound="Position")


@_attrs_define
class Position:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 9.
        name (Union[Unset, str]):  Example: Quarterback.
        display_name (Union[Unset, str]):  Example: Quarterback.
        abbreviation (Union[Unset, str]):  Example: QB.
        leaf (Union[None, Unset, bool]):  Example: True.
        parent (Union['Position', 'Reference', None, Unset]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    leaf: Union[None, Unset, bool] = UNSET
    parent: Union["Position", "Reference", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.reference import Reference

        id = self.id

        name = self.name

        display_name = self.display_name

        abbreviation = self.abbreviation

        leaf: Union[None, Unset, bool]
        if isinstance(self.leaf, Unset):
            leaf = UNSET
        else:
            leaf = self.leaf

        parent: Union[Dict[str, Any], None, Unset]
        if isinstance(self.parent, Unset):
            parent = UNSET
        elif isinstance(self.parent, Position):
            parent = self.parent.to_dict()
        elif isinstance(self.parent, Reference):
            parent = self.parent.to_dict()
        else:
            parent = self.parent

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if leaf is not UNSET:
            field_dict["leaf"] = leaf
        if parent is not UNSET:
            field_dict["parent"] = parent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reference import Reference

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        def _parse_leaf(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        leaf = _parse_leaf(d.pop("leaf", UNSET))

        def _parse_parent(data: object) -> Union["Position", "Reference", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parent_type_0 = Position.from_dict(data)

                return parent_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parent_type_1 = Reference.from_dict(data)

                return parent_type_1
            except:  # noqa: E722
                pass
            return cast(Union["Position", "Reference", None, Unset], data)

        parent = _parse_parent(d.pop("parent", UNSET))

        position = cls(
            id=id,
            name=name,
            display_name=display_name,
            abbreviation=abbreviation,
            leaf=leaf,
            parent=parent,
        )

        position.additional_properties = d
        return position

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
