from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.competitor_home_away import CompetitorHomeAway
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_team import EventTeam
    from ..models.record import Record
    from ..models.score import Score


T = TypeVar("T", bound="Competitor")


@_attrs_define
class Competitor:
    """
    Attributes:
        id (str): Competitor identifier Example: 21.
        type (str): Competitor type Example: team.
        home_away (CompetitorHomeAway): Home or away designation Example: home.
        team (EventTeam):
        order (Union[Unset, int]): Display order
        winner (Union[Unset, bool]): Whether this competitor won (for completed events)
        score (Union[Unset, Score]):
        record (Union[Unset, Record]):
        display_order (Union[Unset, int]): Display order Example: 2.
    """

    id: str
    type: str
    home_away: CompetitorHomeAway
    team: "EventTeam"
    order: Union[Unset, int] = UNSET
    winner: Union[Unset, bool] = UNSET
    score: Union[Unset, "Score"] = UNSET
    record: Union[Unset, "Record"] = UNSET
    display_order: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type

        home_away = self.home_away.value

        team = self.team.to_dict()

        order = self.order

        winner = self.winner

        score: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.score, Unset):
            score = self.score.to_dict()

        record: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record, Unset):
            record = self.record.to_dict()

        display_order = self.display_order

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
                "homeAway": home_away,
                "team": team,
            }
        )
        if order is not UNSET:
            field_dict["order"] = order
        if winner is not UNSET:
            field_dict["winner"] = winner
        if score is not UNSET:
            field_dict["score"] = score
        if record is not UNSET:
            field_dict["record"] = record
        if display_order is not UNSET:
            field_dict["displayOrder"] = display_order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event_team import EventTeam
        from ..models.record import Record
        from ..models.score import Score

        d = src_dict.copy()
        id = d.pop("id")

        type = d.pop("type")

        home_away = CompetitorHomeAway(d.pop("homeAway"))

        team = EventTeam.from_dict(d.pop("team"))

        order = d.pop("order", UNSET)

        winner = d.pop("winner", UNSET)

        _score = d.pop("score", UNSET)
        score: Union[Unset, Score]
        if isinstance(_score, Unset):
            score = UNSET
        else:
            score = Score.from_dict(_score)

        _record = d.pop("record", UNSET)
        record: Union[Unset, Record]
        if isinstance(_record, Unset):
            record = UNSET
        else:
            record = Record.from_dict(_record)

        display_order = d.pop("displayOrder", UNSET)

        competitor = cls(
            id=id,
            type=type,
            home_away=home_away,
            team=team,
            order=order,
            winner=winner,
            score=score,
            record=record,
            display_order=display_order,
        )

        competitor.additional_properties = d
        return competitor

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
