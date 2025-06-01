from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.team_leaders_container import TeamLeadersContainer
    from ..models.team_leaders_season import TeamLeadersSeason


T = TypeVar("T", bound="TeamLeadersResponse")


@_attrs_define
class TeamLeadersResponse:
    """Response containing team leaders for various statistical categories

    Attributes:
        current_season (TeamLeadersSeason):
        requested_season (TeamLeadersSeason):
        team_leaders (TeamLeadersContainer):
    """

    current_season: "TeamLeadersSeason"
    requested_season: "TeamLeadersSeason"
    team_leaders: "TeamLeadersContainer"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_season = self.current_season.to_dict()

        requested_season = self.requested_season.to_dict()

        team_leaders = self.team_leaders.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currentSeason": current_season,
                "requestedSeason": requested_season,
                "teamLeaders": team_leaders,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team_leaders_container import TeamLeadersContainer
        from ..models.team_leaders_season import TeamLeadersSeason

        d = src_dict.copy()
        current_season = TeamLeadersSeason.from_dict(d.pop("currentSeason"))

        requested_season = TeamLeadersSeason.from_dict(d.pop("requestedSeason"))

        team_leaders = TeamLeadersContainer.from_dict(d.pop("teamLeaders"))

        team_leaders_response = cls(
            current_season=current_season,
            requested_season=requested_season,
            team_leaders=team_leaders,
        )

        team_leaders_response.additional_properties = d
        return team_leaders_response

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
