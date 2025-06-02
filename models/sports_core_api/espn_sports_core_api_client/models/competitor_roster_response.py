from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reference import Reference
    from ..models.roster_entry import RosterEntry


T = TypeVar("T", bound="CompetitorRosterResponse")


@_attrs_define
class CompetitorRosterResponse:
    """
    Attributes:
        ref (str): Reference URL for this roster
        entries (List['RosterEntry']): List of roster entries (players)
        competition (Union[Unset, Reference]):
        team (Union[Unset, Reference]):
    """

    ref: str
    entries: List["RosterEntry"]
    competition: Union[Unset, "Reference"] = UNSET
    team: Union[Unset, "Reference"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        competition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.competition, Unset):
            competition = self.competition.to_dict()

        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "entries": entries,
            }
        )
        if competition is not UNSET:
            field_dict["competition"] = competition
        if team is not UNSET:
            field_dict["team"] = team

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reference import Reference
        from ..models.roster_entry import RosterEntry

        d = src_dict.copy()
        ref = d.pop("$ref")

        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:
            entries_item = RosterEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        _competition = d.pop("competition", UNSET)
        competition: Union[Unset, Reference]
        if isinstance(_competition, Unset):
            competition = UNSET
        else:
            competition = Reference.from_dict(_competition)

        _team = d.pop("team", UNSET)
        team: Union[Unset, Reference]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = Reference.from_dict(_team)

        competitor_roster_response = cls(
            ref=ref,
            entries=entries,
            competition=competition,
            team=team,
        )

        competitor_roster_response.additional_properties = d
        return competitor_roster_response

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
