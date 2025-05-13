from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conference import Conference


T = TypeVar("T", bound="StandingsResponse")


@_attrs_define
class StandingsResponse:
    """
    Attributes:
        name (str):  Example: National Football League.
        children (List['Conference']):
        uid (Union[Unset, str]):  Example: s:20~l:28~g:9.
        id (Union[Unset, str]):  Example: 9.
        abbreviation (Union[Unset, str]):  Example: NFL.
        short_name (Union[Unset, str]):  Example: NFL.
    """

    name: str
    children: List["Conference"]
    uid: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        children = []
        for children_item_data in self.children:
            children_item = children_item_data.to_dict()
            children.append(children_item)

        uid = self.uid

        id = self.id

        abbreviation = self.abbreviation

        short_name = self.short_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "children": children,
            }
        )
        if uid is not UNSET:
            field_dict["uid"] = uid
        if id is not UNSET:
            field_dict["id"] = id
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if short_name is not UNSET:
            field_dict["shortName"] = short_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.conference import Conference

        d = src_dict.copy()
        name = d.pop("name")

        children = []
        _children = d.pop("children")
        for children_item_data in _children:
            children_item = Conference.from_dict(children_item_data)

            children.append(children_item)

        uid = d.pop("uid", UNSET)

        id = d.pop("id", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        short_name = d.pop("shortName", UNSET)

        standings_response = cls(
            name=name,
            children=children,
            uid=uid,
            id=id,
            abbreviation=abbreviation,
            short_name=short_name,
        )

        standings_response.additional_properties = d
        return standings_response

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
