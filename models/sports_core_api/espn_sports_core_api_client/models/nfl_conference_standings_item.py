from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="NflConferenceStandingsItem")


@_attrs_define
class NflConferenceStandingsItem:
    """Item in NFL Conference Standings response.

    Attributes:
        ref (str):
        id (str):
        name (str):
        display_name (str):
        links (List['Link']):
    """

    ref: str
    id: str
    name: str
    display_name: str
    links: List["Link"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        id = self.id

        name = self.name

        display_name = self.display_name

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "id": id,
                "name": name,
                "displayName": display_name,
                "links": links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link import Link

        d = src_dict.copy()
        ref = d.pop("$ref")

        id = d.pop("id")

        name = d.pop("name")

        display_name = d.pop("displayName")

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        nfl_conference_standings_item = cls(
            ref=ref,
            id=id,
            name=name,
            display_name=display_name,
            links=links,
        )

        nfl_conference_standings_item.additional_properties = d
        return nfl_conference_standings_item

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
