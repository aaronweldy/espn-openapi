from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reference import Reference


T = TypeVar("T", bound="TeamLeader")


@_attrs_define
class TeamLeader:
    """
    Attributes:
        display_value (str): Display-formatted value for the leader Example: 282.9.
        value (float): Numeric value for the leader statistic Example: 282.9.
        rel (Union[Unset, List[str]]): Relationship types Example: ['athlete'].
        athlete (Union[Unset, Reference]):
        team (Union[Unset, Reference]):
        statistics (Union[Unset, Reference]):
    """

    display_value: str
    value: float
    rel: Union[Unset, List[str]] = UNSET
    athlete: Union[Unset, "Reference"] = UNSET
    team: Union[Unset, "Reference"] = UNSET
    statistics: Union[Unset, "Reference"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_value = self.display_value

        value = self.value

        rel: Union[Unset, List[str]] = UNSET
        if not isinstance(self.rel, Unset):
            rel = self.rel

        athlete: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.athlete, Unset):
            athlete = self.athlete.to_dict()

        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        statistics: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayValue": display_value,
                "value": value,
            }
        )
        if rel is not UNSET:
            field_dict["rel"] = rel
        if athlete is not UNSET:
            field_dict["athlete"] = athlete
        if team is not UNSET:
            field_dict["team"] = team
        if statistics is not UNSET:
            field_dict["statistics"] = statistics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reference import Reference

        d = src_dict.copy()
        display_value = d.pop("displayValue")

        value = d.pop("value")

        rel = cast(List[str], d.pop("rel", UNSET))

        _athlete = d.pop("athlete", UNSET)
        athlete: Union[Unset, Reference]
        if isinstance(_athlete, Unset):
            athlete = UNSET
        else:
            athlete = Reference.from_dict(_athlete)

        _team = d.pop("team", UNSET)
        team: Union[Unset, Reference]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = Reference.from_dict(_team)

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, Reference]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = Reference.from_dict(_statistics)

        team_leader = cls(
            display_value=display_value,
            value=value,
            rel=rel,
            athlete=athlete,
            team=team,
            statistics=statistics,
        )

        team_leader.additional_properties = d
        return team_leader

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
