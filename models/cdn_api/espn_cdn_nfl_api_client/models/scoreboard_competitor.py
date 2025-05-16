from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scoreboard_competitor_statistics_item import ScoreboardCompetitorStatisticsItem
    from ..models.scoreboard_team_data import ScoreboardTeamData


T = TypeVar("T", bound="ScoreboardCompetitor")


@_attrs_define
class ScoreboardCompetitor:
    """
    Attributes:
        uid (Union[Unset, str]):
        home_away (Union[Unset, str]):
        score (Union[Unset, str]):
        id (Union[Unset, str]):
        team (Union[Unset, ScoreboardTeamData]):
        type (Union[Unset, str]):
        order (Union[Unset, int]):
        statistics (Union[Unset, List['ScoreboardCompetitorStatisticsItem']]):
    """

    uid: Union[Unset, str] = UNSET
    home_away: Union[Unset, str] = UNSET
    score: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    team: Union[Unset, "ScoreboardTeamData"] = UNSET
    type: Union[Unset, str] = UNSET
    order: Union[Unset, int] = UNSET
    statistics: Union[Unset, List["ScoreboardCompetitorStatisticsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uid = self.uid

        home_away = self.home_away

        score = self.score

        id = self.id

        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        type = self.type

        order = self.order

        statistics: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = []
            for statistics_item_data in self.statistics:
                statistics_item = statistics_item_data.to_dict()
                statistics.append(statistics_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uid is not UNSET:
            field_dict["uid"] = uid
        if home_away is not UNSET:
            field_dict["homeAway"] = home_away
        if score is not UNSET:
            field_dict["score"] = score
        if id is not UNSET:
            field_dict["id"] = id
        if team is not UNSET:
            field_dict["team"] = team
        if type is not UNSET:
            field_dict["type"] = type
        if order is not UNSET:
            field_dict["order"] = order
        if statistics is not UNSET:
            field_dict["statistics"] = statistics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scoreboard_competitor_statistics_item import ScoreboardCompetitorStatisticsItem
        from ..models.scoreboard_team_data import ScoreboardTeamData

        d = src_dict.copy()
        uid = d.pop("uid", UNSET)

        home_away = d.pop("homeAway", UNSET)

        score = d.pop("score", UNSET)

        id = d.pop("id", UNSET)

        _team = d.pop("team", UNSET)
        team: Union[Unset, ScoreboardTeamData]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = ScoreboardTeamData.from_dict(_team)

        type = d.pop("type", UNSET)

        order = d.pop("order", UNSET)

        statistics = []
        _statistics = d.pop("statistics", UNSET)
        for statistics_item_data in _statistics or []:
            statistics_item = ScoreboardCompetitorStatisticsItem.from_dict(statistics_item_data)

            statistics.append(statistics_item)

        scoreboard_competitor = cls(
            uid=uid,
            home_away=home_away,
            score=score,
            id=id,
            team=team,
            type=type,
            order=order,
            statistics=statistics,
        )

        scoreboard_competitor.additional_properties = d
        return scoreboard_competitor

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
