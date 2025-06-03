from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayerOwnership")


@_attrs_define
class PlayerOwnership:
    """
    Attributes:
        activity_level (Union[None, Unset, str]): Player activity level
        auction_value_average (Union[Unset, float]): Average auction value
        auction_value_average_change (Union[Unset, float]): Change in average auction value
        average_draft_position (Union[Unset, float]): Average draft position
        average_draft_position_percent_change (Union[Unset, float]): Percent change in average draft position
        date (Union[None, Unset, str]): Date of ownership data
        league_type (Union[Unset, int]): Type of league
        percent_change (Union[Unset, float]): Percent change in ownership
        percent_owned (Union[Unset, float]): Percentage of leagues where player is owned
        percent_started (Union[Unset, float]): Percentage of leagues where player is started
    """

    activity_level: Union[None, Unset, str] = UNSET
    auction_value_average: Union[Unset, float] = UNSET
    auction_value_average_change: Union[Unset, float] = UNSET
    average_draft_position: Union[Unset, float] = UNSET
    average_draft_position_percent_change: Union[Unset, float] = UNSET
    date: Union[None, Unset, str] = UNSET
    league_type: Union[Unset, int] = UNSET
    percent_change: Union[Unset, float] = UNSET
    percent_owned: Union[Unset, float] = UNSET
    percent_started: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        activity_level: Union[None, Unset, str]
        if isinstance(self.activity_level, Unset):
            activity_level = UNSET
        else:
            activity_level = self.activity_level

        auction_value_average = self.auction_value_average

        auction_value_average_change = self.auction_value_average_change

        average_draft_position = self.average_draft_position

        average_draft_position_percent_change = self.average_draft_position_percent_change

        date: Union[None, Unset, str]
        if isinstance(self.date, Unset):
            date = UNSET
        else:
            date = self.date

        league_type = self.league_type

        percent_change = self.percent_change

        percent_owned = self.percent_owned

        percent_started = self.percent_started

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity_level is not UNSET:
            field_dict["activityLevel"] = activity_level
        if auction_value_average is not UNSET:
            field_dict["auctionValueAverage"] = auction_value_average
        if auction_value_average_change is not UNSET:
            field_dict["auctionValueAverageChange"] = auction_value_average_change
        if average_draft_position is not UNSET:
            field_dict["averageDraftPosition"] = average_draft_position
        if average_draft_position_percent_change is not UNSET:
            field_dict["averageDraftPositionPercentChange"] = average_draft_position_percent_change
        if date is not UNSET:
            field_dict["date"] = date
        if league_type is not UNSET:
            field_dict["leagueType"] = league_type
        if percent_change is not UNSET:
            field_dict["percentChange"] = percent_change
        if percent_owned is not UNSET:
            field_dict["percentOwned"] = percent_owned
        if percent_started is not UNSET:
            field_dict["percentStarted"] = percent_started

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_activity_level(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        activity_level = _parse_activity_level(d.pop("activityLevel", UNSET))

        auction_value_average = d.pop("auctionValueAverage", UNSET)

        auction_value_average_change = d.pop("auctionValueAverageChange", UNSET)

        average_draft_position = d.pop("averageDraftPosition", UNSET)

        average_draft_position_percent_change = d.pop("averageDraftPositionPercentChange", UNSET)

        def _parse_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        date = _parse_date(d.pop("date", UNSET))

        league_type = d.pop("leagueType", UNSET)

        percent_change = d.pop("percentChange", UNSET)

        percent_owned = d.pop("percentOwned", UNSET)

        percent_started = d.pop("percentStarted", UNSET)

        player_ownership = cls(
            activity_level=activity_level,
            auction_value_average=auction_value_average,
            auction_value_average_change=auction_value_average_change,
            average_draft_position=average_draft_position,
            average_draft_position_percent_change=average_draft_position_percent_change,
            date=date,
            league_type=league_type,
            percent_change=percent_change,
            percent_owned=percent_owned,
            percent_started=percent_started,
        )

        player_ownership.additional_properties = d
        return player_ownership

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
