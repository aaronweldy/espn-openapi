from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.athlete_game_log_response_events import AthleteGameLogResponseEvents
    from ..models.game_log_season import GameLogSeason
    from ..models.requested_season import RequestedSeason


T = TypeVar("T", bound="AthleteGameLogResponse")


@_attrs_define
class AthleteGameLogResponse:
    """
    Attributes:
        events (AthleteGameLogResponseEvents): A dictionary of events, keyed by event ID
        requested_season (Union[Unset, RequestedSeason]):
        season (Union[Unset, GameLogSeason]):
    """

    events: "AthleteGameLogResponseEvents"
    requested_season: Union[Unset, "RequestedSeason"] = UNSET
    season: Union[Unset, "GameLogSeason"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        events = self.events.to_dict()

        requested_season: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.requested_season, Unset):
            requested_season = self.requested_season.to_dict()

        season: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "events": events,
            }
        )
        if requested_season is not UNSET:
            field_dict["requested_season"] = requested_season
        if season is not UNSET:
            field_dict["season"] = season

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.athlete_game_log_response_events import AthleteGameLogResponseEvents
        from ..models.game_log_season import GameLogSeason
        from ..models.requested_season import RequestedSeason

        d = src_dict.copy()
        events = AthleteGameLogResponseEvents.from_dict(d.pop("events"))

        _requested_season = d.pop("requested_season", UNSET)
        requested_season: Union[Unset, RequestedSeason]
        if isinstance(_requested_season, Unset):
            requested_season = UNSET
        else:
            requested_season = RequestedSeason.from_dict(_requested_season)

        _season = d.pop("season", UNSET)
        season: Union[Unset, GameLogSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = GameLogSeason.from_dict(_season)

        athlete_game_log_response = cls(
            events=events,
            requested_season=requested_season,
            season=season,
        )

        athlete_game_log_response.additional_properties = d
        return athlete_game_log_response

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
