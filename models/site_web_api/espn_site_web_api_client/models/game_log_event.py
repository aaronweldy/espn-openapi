import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.game_log_event_home_away import GameLogEventHomeAway
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_reference import TeamReference


T = TypeVar("T", bound="GameLogEvent")


@_attrs_define
class GameLogEvent:
    """
    Attributes:
        event_id (str):  Example: 401547417.
        date (datetime.datetime):  Example: 2023-02-12T23:30:00Z.
        opponent (TeamReference):
        stats (List[str]):
        home_away (Union[Unset, GameLogEventHomeAway]):  Example: home.
        result (Union[Unset, str]):  Example: W 38-35.
    """

    event_id: str
    date: datetime.datetime
    opponent: "TeamReference"
    stats: List[str]
    home_away: Union[Unset, GameLogEventHomeAway] = UNSET
    result: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_id = self.event_id

        date = self.date.isoformat()

        opponent = self.opponent.to_dict()

        stats = self.stats

        home_away: Union[Unset, str] = UNSET
        if not isinstance(self.home_away, Unset):
            home_away = self.home_away.value

        result = self.result

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventId": event_id,
                "date": date,
                "opponent": opponent,
                "stats": stats,
            }
        )
        if home_away is not UNSET:
            field_dict["homeAway"] = home_away
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team_reference import TeamReference

        d = src_dict.copy()
        event_id = d.pop("eventId")

        date = isoparse(d.pop("date"))

        opponent = TeamReference.from_dict(d.pop("opponent"))

        stats = cast(List[str], d.pop("stats"))

        _home_away = d.pop("homeAway", UNSET)
        home_away: Union[Unset, GameLogEventHomeAway]
        if isinstance(_home_away, Unset):
            home_away = UNSET
        else:
            home_away = GameLogEventHomeAway(_home_away)

        result = d.pop("result", UNSET)

        game_log_event = cls(
            event_id=event_id,
            date=date,
            opponent=opponent,
            stats=stats,
            home_away=home_away,
            result=result,
        )

        game_log_event.additional_properties = d
        return game_log_event

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
