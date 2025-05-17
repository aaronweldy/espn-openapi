from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.competitor_home_away import CompetitorHomeAway
from ..types import UNSET, Unset

if TYPE_CHECKING:
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
        home_away (CompetitorHomeAway):
        team (Team):
        uid (Union[Unset, str]):  Example: s:20~l:28~t:21.
        type (Union[Unset, str]):  Example: team.
        winner (Union[Unset, bool]):
        score (Union[Unset, str]):  Example: 35.
        linescores (Union[Unset, List['Linescore']]):
        statistics (Union[Unset, List['Statistic']]):
        records (Union[Unset, List['Record']]):
    """

    id: str
    order: int
    home_away: CompetitorHomeAway
    team: "Team"
    uid: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    winner: Union[Unset, bool] = UNSET
    score: Union[Unset, str] = UNSET
    linescores: Union[Unset, List["Linescore"]] = UNSET
    statistics: Union[Unset, List["Statistic"]] = UNSET
    records: Union[Unset, List["Record"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        order = self.order

        home_away = self.home_away.value

        team = self.team.to_dict()

        uid = self.uid

        type = self.type

        winner = self.winner

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
                "homeAway": home_away,
                "team": team,
            }
        )
        if uid is not UNSET:
            field_dict["uid"] = uid
        if type is not UNSET:
            field_dict["type"] = type
        if winner is not UNSET:
            field_dict["winner"] = winner
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
        from ..models.linescore import Linescore
        from ..models.record import Record
        from ..models.statistic import Statistic
        from ..models.team import Team

        d = src_dict.copy()
        id = d.pop("id")

        order = d.pop("order")

        home_away = CompetitorHomeAway(d.pop("homeAway"))

        team = Team.from_dict(d.pop("team"))

        uid = d.pop("uid", UNSET)

        type = d.pop("type", UNSET)

        winner = d.pop("winner", UNSET)

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
            home_away=home_away,
            team=team,
            uid=uid,
            type=type,
            winner=winner,
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
