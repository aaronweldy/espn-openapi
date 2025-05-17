from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reference import Reference


T = TypeVar("T", bound="NflTeamDepthchartPosition")


@_attrs_define
class NflTeamDepthchartPosition:
    """
    Attributes:
        ref (str):
        id (str):
        name (str):
        display_name (str):
        abbreviation (str):
        leaf (bool):
        parent (Reference):
    """

    ref: str
    id: str
    name: str
    display_name: str
    abbreviation: str
    leaf: bool
    parent: "Reference"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        id = self.id

        name = self.name

        display_name = self.display_name

        abbreviation = self.abbreviation

        leaf = self.leaf

        parent = self.parent.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "id": id,
                "name": name,
                "displayName": display_name,
                "abbreviation": abbreviation,
                "leaf": leaf,
                "parent": parent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reference import Reference

        d = src_dict.copy()
        ref = d.pop("$ref")

        id = d.pop("id")

        name = d.pop("name")

        display_name = d.pop("displayName")

        abbreviation = d.pop("abbreviation")

        leaf = d.pop("leaf")

        parent = Reference.from_dict(d.pop("parent"))

        nfl_team_depthchart_position = cls(
            ref=ref,
            id=id,
            name=name,
            display_name=display_name,
            abbreviation=abbreviation,
            leaf=leaf,
            parent=parent,
        )

        nfl_team_depthchart_position.additional_properties = d
        return nfl_team_depthchart_position

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
