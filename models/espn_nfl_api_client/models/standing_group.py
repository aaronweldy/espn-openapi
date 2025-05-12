from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.standing_entry import StandingEntry


T = TypeVar("T", bound="StandingGroup")


@_attrs_define
class StandingGroup:
    """
    Attributes:
        season (int):  Example: 2024.
        season_type (int):  Example: 2.
        entries (List['StandingEntry']):
        id (Union[Unset, str]):  Example: 0.
        name (Union[Unset, str]):  Example: overall.
        display_name (Union[Unset, str]):  Example: Standings.
        links (Union[Unset, List['Link']]):
        season_display_name (Union[Unset, str]):  Example: 2024.
    """

    season: int
    season_type: int
    entries: List["StandingEntry"]
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    links: Union[Unset, List["Link"]] = UNSET
    season_display_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        season = self.season

        season_type = self.season_type

        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        id = self.id

        name = self.name

        display_name = self.display_name

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        season_display_name = self.season_display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "season": season,
                "seasonType": season_type,
                "entries": entries,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if links is not UNSET:
            field_dict["links"] = links
        if season_display_name is not UNSET:
            field_dict["seasonDisplayName"] = season_display_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link import Link
        from ..models.standing_entry import StandingEntry

        d = src_dict.copy()
        season = d.pop("season")

        season_type = d.pop("seasonType")

        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:
            entries_item = StandingEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        season_display_name = d.pop("seasonDisplayName", UNSET)

        standing_group = cls(
            season=season,
            season_type=season_type,
            entries=entries,
            id=id,
            name=name,
            display_name=display_name,
            links=links,
            season_display_name=season_display_name,
        )

        standing_group.additional_properties = d
        return standing_group

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
