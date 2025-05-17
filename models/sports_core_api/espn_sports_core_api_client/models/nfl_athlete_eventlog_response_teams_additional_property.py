from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reference import Reference


T = TypeVar("T", bound="NflAthleteEventlogResponseTeamsAdditionalProperty")


@_attrs_define
class NflAthleteEventlogResponseTeamsAdditionalProperty:
    """
    Attributes:
        team (Reference):
        id (str):
    """

    team: "Reference"
    id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team = self.team.to_dict()

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team": team,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reference import Reference

        d = src_dict.copy()
        team = Reference.from_dict(d.pop("team"))

        id = d.pop("id")

        nfl_athlete_eventlog_response_teams_additional_property = cls(
            team=team,
            id=id,
        )

        nfl_athlete_eventlog_response_teams_additional_property.additional_properties = d
        return nfl_athlete_eventlog_response_teams_additional_property

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
