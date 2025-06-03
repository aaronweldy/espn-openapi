from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FantasySeasonResponseSettingsGameNotificationSettings")


@_attrs_define
class FantasySeasonResponseSettingsGameNotificationSettings:
    """
    Attributes:
        availability_notifications_enabled (Union[Unset, bool]):
        draft_notifications_enabled (Union[Unset, bool]):
        injury_notifications_enabled (Union[Unset, bool]):
        lineup_notifications_enabled (Union[Unset, bool]):
        position_eligibility_notifications_enabled (Union[Unset, bool]):
        roster_news_notifications_enabled (Union[Unset, bool]):
        start_bench_notifications_enabled (Union[Unset, bool]):
        trade_notifications_enabled (Union[Unset, bool]):
    """

    availability_notifications_enabled: Union[Unset, bool] = UNSET
    draft_notifications_enabled: Union[Unset, bool] = UNSET
    injury_notifications_enabled: Union[Unset, bool] = UNSET
    lineup_notifications_enabled: Union[Unset, bool] = UNSET
    position_eligibility_notifications_enabled: Union[Unset, bool] = UNSET
    roster_news_notifications_enabled: Union[Unset, bool] = UNSET
    start_bench_notifications_enabled: Union[Unset, bool] = UNSET
    trade_notifications_enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        availability_notifications_enabled = self.availability_notifications_enabled

        draft_notifications_enabled = self.draft_notifications_enabled

        injury_notifications_enabled = self.injury_notifications_enabled

        lineup_notifications_enabled = self.lineup_notifications_enabled

        position_eligibility_notifications_enabled = self.position_eligibility_notifications_enabled

        roster_news_notifications_enabled = self.roster_news_notifications_enabled

        start_bench_notifications_enabled = self.start_bench_notifications_enabled

        trade_notifications_enabled = self.trade_notifications_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if availability_notifications_enabled is not UNSET:
            field_dict["availabilityNotificationsEnabled"] = availability_notifications_enabled
        if draft_notifications_enabled is not UNSET:
            field_dict["draftNotificationsEnabled"] = draft_notifications_enabled
        if injury_notifications_enabled is not UNSET:
            field_dict["injuryNotificationsEnabled"] = injury_notifications_enabled
        if lineup_notifications_enabled is not UNSET:
            field_dict["lineupNotificationsEnabled"] = lineup_notifications_enabled
        if position_eligibility_notifications_enabled is not UNSET:
            field_dict["positionEligibilityNotificationsEnabled"] = position_eligibility_notifications_enabled
        if roster_news_notifications_enabled is not UNSET:
            field_dict["rosterNewsNotificationsEnabled"] = roster_news_notifications_enabled
        if start_bench_notifications_enabled is not UNSET:
            field_dict["startBenchNotificationsEnabled"] = start_bench_notifications_enabled
        if trade_notifications_enabled is not UNSET:
            field_dict["tradeNotificationsEnabled"] = trade_notifications_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        availability_notifications_enabled = d.pop("availabilityNotificationsEnabled", UNSET)

        draft_notifications_enabled = d.pop("draftNotificationsEnabled", UNSET)

        injury_notifications_enabled = d.pop("injuryNotificationsEnabled", UNSET)

        lineup_notifications_enabled = d.pop("lineupNotificationsEnabled", UNSET)

        position_eligibility_notifications_enabled = d.pop("positionEligibilityNotificationsEnabled", UNSET)

        roster_news_notifications_enabled = d.pop("rosterNewsNotificationsEnabled", UNSET)

        start_bench_notifications_enabled = d.pop("startBenchNotificationsEnabled", UNSET)

        trade_notifications_enabled = d.pop("tradeNotificationsEnabled", UNSET)

        fantasy_season_response_settings_game_notification_settings = cls(
            availability_notifications_enabled=availability_notifications_enabled,
            draft_notifications_enabled=draft_notifications_enabled,
            injury_notifications_enabled=injury_notifications_enabled,
            lineup_notifications_enabled=lineup_notifications_enabled,
            position_eligibility_notifications_enabled=position_eligibility_notifications_enabled,
            roster_news_notifications_enabled=roster_news_notifications_enabled,
            start_bench_notifications_enabled=start_bench_notifications_enabled,
            trade_notifications_enabled=trade_notifications_enabled,
        )

        fantasy_season_response_settings_game_notification_settings.additional_properties = d
        return fantasy_season_response_settings_game_notification_settings

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
