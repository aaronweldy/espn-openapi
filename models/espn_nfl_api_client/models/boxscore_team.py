from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.statistic import Statistic
    from ..models.team import Team


T = TypeVar("T", bound="BoxscoreTeam")


@_attrs_define
class BoxscoreTeam:
    """
    Attributes:
        team (Union[Unset, Team]):
        statistics (Union[Unset, list['Statistic']]):
    """

    team: Union[Unset, "Team"] = UNSET
    statistics: Union[Unset, list["Statistic"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        statistics: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = []
            for statistics_item_data in self.statistics:
                statistics_item = statistics_item_data.to_dict()
                statistics.append(statistics_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if team is not UNSET:
            field_dict["team"] = team
        if statistics is not UNSET:
            field_dict["statistics"] = statistics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.statistic import Statistic
        from ..models.team import Team

        d = dict(src_dict)
        _team = d.pop("team", UNSET)
        team: Union[Unset, Team]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = Team.from_dict(_team)

        statistics = []
        _statistics = d.pop("statistics", UNSET)
        for statistics_item_data in _statistics or []:
            statistics_item = Statistic.from_dict(statistics_item_data)

            statistics.append(statistics_item)

        boxscore_team = cls(
            team=team,
            statistics=statistics,
        )

        boxscore_team.additional_properties = d
        return boxscore_team

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
