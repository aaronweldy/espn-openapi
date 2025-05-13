from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reference import Reference
    from ..models.statistics_reference import StatisticsReference
    from ..models.team import Team


T = TypeVar("T", bound="StatisticsTypeEntry")


@_attrs_define
class StatisticsTypeEntry:
    """
    Attributes:
        type (str):  Example: total.
        statistics (StatisticsReference):
        team (Union['Reference', 'Team', None, Unset]):
    """

    type: str
    statistics: "StatisticsReference"
    team: Union["Reference", "Team", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.reference import Reference
        from ..models.team import Team

        type = self.type

        statistics = self.statistics.to_dict()

        team: Union[Dict[str, Any], None, Unset]
        if isinstance(self.team, Unset):
            team = UNSET
        elif isinstance(self.team, Team):
            team = self.team.to_dict()
        elif isinstance(self.team, Reference):
            team = self.team.to_dict()
        else:
            team = self.team

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "statistics": statistics,
            }
        )
        if team is not UNSET:
            field_dict["team"] = team

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reference import Reference
        from ..models.statistics_reference import StatisticsReference
        from ..models.team import Team

        d = src_dict.copy()
        type = d.pop("type")

        statistics = StatisticsReference.from_dict(d.pop("statistics"))

        def _parse_team(data: object) -> Union["Reference", "Team", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                team_type_0 = Team.from_dict(data)

                return team_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                team_type_1 = Reference.from_dict(data)

                return team_type_1
            except:  # noqa: E722
                pass
            return cast(Union["Reference", "Team", None, Unset], data)

        team = _parse_team(d.pop("team", UNSET))

        statistics_type_entry = cls(
            type=type,
            statistics=statistics,
            team=team,
        )

        statistics_type_entry.additional_properties = d
        return statistics_type_entry

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
