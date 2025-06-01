from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.leaders_container import LeadersContainer
    from ..models.leaders_league import LeadersLeague
    from ..models.leaders_season import LeadersSeason


T = TypeVar("T", bound="LeadersResponse")


@_attrs_define
class LeadersResponse:
    """Response containing statistical leaders for a sport/league

    Attributes:
        current_season (LeadersSeason):
        requested_season (LeadersSeason):
        leaders (LeadersContainer):
        league (LeadersLeague):
    """

    current_season: "LeadersSeason"
    requested_season: "LeadersSeason"
    leaders: "LeadersContainer"
    league: "LeadersLeague"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_season = self.current_season.to_dict()

        requested_season = self.requested_season.to_dict()

        leaders = self.leaders.to_dict()

        league = self.league.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currentSeason": current_season,
                "requestedSeason": requested_season,
                "leaders": leaders,
                "league": league,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.leaders_container import LeadersContainer
        from ..models.leaders_league import LeadersLeague
        from ..models.leaders_season import LeadersSeason

        d = src_dict.copy()
        current_season = LeadersSeason.from_dict(d.pop("currentSeason"))

        requested_season = LeadersSeason.from_dict(d.pop("requestedSeason"))

        leaders = LeadersContainer.from_dict(d.pop("leaders"))

        league = LeadersLeague.from_dict(d.pop("league"))

        leaders_response = cls(
            current_season=current_season,
            requested_season=requested_season,
            leaders=leaders,
            league=league,
        )

        leaders_response.additional_properties = d
        return leaders_response

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
