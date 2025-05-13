from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedule_item_winner import ScheduleItemWinner
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_team import ScheduleTeam


T = TypeVar("T", bound="ScheduleItem")


@_attrs_define
class ScheduleItem:
    """
    Attributes:
        id (int): Schedule item ID Example: 1.
        matchup_period_id (int): Matchup period (week) Example: 1.
        home (ScheduleTeam):
        away (ScheduleTeam):
        winner (Union[Unset, ScheduleItemWinner]): Winner of matchup Example: HOME.
    """

    id: int
    matchup_period_id: int
    home: "ScheduleTeam"
    away: "ScheduleTeam"
    winner: Union[Unset, ScheduleItemWinner] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        matchup_period_id = self.matchup_period_id

        home = self.home.to_dict()

        away = self.away.to_dict()

        winner: Union[Unset, str] = UNSET
        if not isinstance(self.winner, Unset):
            winner = self.winner.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "matchupPeriodId": matchup_period_id,
                "home": home,
                "away": away,
            }
        )
        if winner is not UNSET:
            field_dict["winner"] = winner

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.schedule_team import ScheduleTeam

        d = src_dict.copy()
        id = d.pop("id")

        matchup_period_id = d.pop("matchupPeriodId")

        home = ScheduleTeam.from_dict(d.pop("home"))

        away = ScheduleTeam.from_dict(d.pop("away"))

        _winner = d.pop("winner", UNSET)
        winner: Union[Unset, ScheduleItemWinner]
        if isinstance(_winner, Unset):
            winner = UNSET
        else:
            winner = ScheduleItemWinner(_winner)

        schedule_item = cls(
            id=id,
            matchup_period_id=matchup_period_id,
            home=home,
            away=away,
            winner=winner,
        )

        schedule_item.additional_properties = d
        return schedule_item

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
