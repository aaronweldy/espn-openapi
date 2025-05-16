from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nfl_standings_entry import NflStandingsEntry


T = TypeVar("T", bound="NflStandingsGroupStandings")


@_attrs_define
class NflStandingsGroupStandings:
    """
    Attributes:
        entries (Union[Unset, List['NflStandingsEntry']]):
        display_name (Union[Unset, str]):
        name (Union[Unset, str]):
        id (Union[Unset, str]):
    """

    entries: Union[Unset, List["NflStandingsEntry"]] = UNSET
    display_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        display_name = self.display_name

        name = self.name

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entries is not UNSET:
            field_dict["entries"] = entries
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nfl_standings_entry import NflStandingsEntry

        d = src_dict.copy()
        entries = []
        _entries = d.pop("entries", UNSET)
        for entries_item_data in _entries or []:
            entries_item = NflStandingsEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        display_name = d.pop("displayName", UNSET)

        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        nfl_standings_group_standings = cls(
            entries=entries,
            display_name=display_name,
            name=name,
            id=id,
        )

        nfl_standings_group_standings.additional_properties = d
        return nfl_standings_group_standings

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
