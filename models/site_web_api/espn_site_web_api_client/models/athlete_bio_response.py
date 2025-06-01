from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.award_entry import AwardEntry
    from ..models.team_history_entry import TeamHistoryEntry


T = TypeVar("T", bound="AthleteBioResponse")


@_attrs_define
class AthleteBioResponse:
    """Athlete biographical information response

    Attributes:
        team_history (Union[Unset, List['TeamHistoryEntry']]): History of teams the athlete has played for
        awards (Union[Unset, List['AwardEntry']]): Awards and achievements (optional, not all athletes have awards)
    """

    team_history: Union[Unset, List["TeamHistoryEntry"]] = UNSET
    awards: Union[Unset, List["AwardEntry"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team_history: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.team_history, Unset):
            team_history = []
            for team_history_item_data in self.team_history:
                team_history_item = team_history_item_data.to_dict()
                team_history.append(team_history_item)

        awards: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.awards, Unset):
            awards = []
            for awards_item_data in self.awards:
                awards_item = awards_item_data.to_dict()
                awards.append(awards_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if team_history is not UNSET:
            field_dict["teamHistory"] = team_history
        if awards is not UNSET:
            field_dict["awards"] = awards

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.award_entry import AwardEntry
        from ..models.team_history_entry import TeamHistoryEntry

        d = src_dict.copy()
        team_history = []
        _team_history = d.pop("teamHistory", UNSET)
        for team_history_item_data in _team_history or []:
            team_history_item = TeamHistoryEntry.from_dict(team_history_item_data)

            team_history.append(team_history_item)

        awards = []
        _awards = d.pop("awards", UNSET)
        for awards_item_data in _awards or []:
            awards_item = AwardEntry.from_dict(awards_item_data)

            awards.append(awards_item)

        athlete_bio_response = cls(
            team_history=team_history,
            awards=awards,
        )

        athlete_bio_response.additional_properties = d
        return athlete_bio_response

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
