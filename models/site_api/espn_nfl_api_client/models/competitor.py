from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.competitor_home_away import CompetitorHomeAway
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.athlete import Athlete
    from ..models.linescore import Linescore
    from ..models.record import Record
    from ..models.statistic import Statistic
    from ..models.team import Team


T = TypeVar("T", bound="Competitor")


@_attrs_define
class Competitor:
    """
    Attributes:
        id (str):  Example: 21.
        order (int):
        uid (Union[Unset, str]):  Example: s:20~l:28~t:21.
        type (Union[Unset, str]):  Example: team.
        home_away (Union[Unset, CompetitorHomeAway]): Home/away designation for team sports (not present in individual
            sports like golf)
        winner (Union[Unset, bool]):
        team (Union[Unset, Team]):
        athlete (Union[Unset, Athlete]):
        score (Union[Unset, str]):  Example: 35.
        linescores (Union[Unset, List['Linescore']]):
        statistics (Union[Unset, List['Statistic']]):
        records (Union[Unset, List['Record']]):
    """

    id: str
    order: int
    uid: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    home_away: Union[Unset, CompetitorHomeAway] = UNSET
    winner: Union[Unset, bool] = UNSET
    team: Union[Unset, "Team"] = UNSET
    athlete: Union[Unset, "Athlete"] = UNSET
    score: Union[Unset, str] = UNSET
    linescores: Union[Unset, List["Linescore"]] = UNSET
    statistics: Union[Unset, List["Statistic"]] = UNSET
    records: Union[Unset, List["Record"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        order = self.order

        uid = self.uid

        type = self.type

        home_away: Union[Unset, str] = UNSET
        if not isinstance(self.home_away, Unset):
            home_away = self.home_away.value

        winner = self.winner

        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        athlete: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.athlete, Unset):
            athlete = self.athlete.to_dict()

        score = self.score

        linescores: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.linescores, Unset):
            linescores = []
            for linescores_item_data in self.linescores:
                linescores_item = linescores_item_data.to_dict()
                linescores.append(linescores_item)

        statistics: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = []
            for statistics_item_data in self.statistics:
                statistics_item = statistics_item_data.to_dict()
                statistics.append(statistics_item)

        records: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.records, Unset):
            records = []
            for records_item_data in self.records:
                records_item = records_item_data.to_dict()
                records.append(records_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "order": order,
            }
        )
        if uid is not UNSET:
            field_dict["uid"] = uid
        if type is not UNSET:
            field_dict["type"] = type
        if home_away is not UNSET:
            field_dict["homeAway"] = home_away
        if winner is not UNSET:
            field_dict["winner"] = winner
        if team is not UNSET:
            field_dict["team"] = team
        if athlete is not UNSET:
            field_dict["athlete"] = athlete
        if score is not UNSET:
            field_dict["score"] = score
        if linescores is not UNSET:
            field_dict["linescores"] = linescores
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if records is not UNSET:
            field_dict["records"] = records

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.athlete import Athlete
        from ..models.linescore import Linescore
        from ..models.record import Record
        from ..models.statistic import Statistic
        from ..models.team import Team

        d = src_dict.copy()
        id = d.pop("id")

        order = d.pop("order")

        uid = d.pop("uid", UNSET)

        type = d.pop("type", UNSET)

        _home_away = d.pop("homeAway", UNSET)
        home_away: Union[Unset, CompetitorHomeAway]
        if isinstance(_home_away, Unset):
            home_away = UNSET
        else:
            home_away = CompetitorHomeAway(_home_away)

        winner = d.pop("winner", UNSET)

        _team = d.pop("team", UNSET)
        team: Union[Unset, Team]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = Team.from_dict(_team)

        _athlete = d.pop("athlete", UNSET)
        athlete: Union[Unset, Athlete]
        if isinstance(_athlete, Unset):
            athlete = UNSET
        else:
            athlete = Athlete.from_dict(_athlete)

        score = d.pop("score", UNSET)

        linescores = []
        _linescores = d.pop("linescores", UNSET)
        for linescores_item_data in _linescores or []:
            linescores_item = Linescore.from_dict(linescores_item_data)

            linescores.append(linescores_item)

        statistics = []
        _statistics = d.pop("statistics", UNSET)
        for statistics_item_data in _statistics or []:
            statistics_item = Statistic.from_dict(statistics_item_data)

            statistics.append(statistics_item)

        records = []
        _records = d.pop("records", UNSET)
        for records_item_data in _records or []:
            records_item = Record.from_dict(records_item_data)

            records.append(records_item)

        competitor = cls(
            id=id,
            order=order,
            uid=uid,
            type=type,
            home_away=home_away,
            winner=winner,
            team=team,
            athlete=athlete,
            score=score,
            linescores=linescores,
            statistics=statistics,
            records=records,
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
