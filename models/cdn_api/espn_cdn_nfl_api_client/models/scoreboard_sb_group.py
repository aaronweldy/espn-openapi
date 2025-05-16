from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScoreboardSbGroup")


@_attrs_define
class ScoreboardSbGroup:
    """
    Attributes:
        page_title (Union[Unset, str]):
        alt_title (Union[Unset, str]):
        schedule_start_date (Union[Unset, str]):
        is_college (Union[Unset, bool]):
        league (Union[Unset, str]):
        sport (Union[Unset, str]):
    """

    page_title: Union[Unset, str] = UNSET
    alt_title: Union[Unset, str] = UNSET
    schedule_start_date: Union[Unset, str] = UNSET
    is_college: Union[Unset, bool] = UNSET
    league: Union[Unset, str] = UNSET
    sport: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        page_title = self.page_title

        alt_title = self.alt_title

        schedule_start_date = self.schedule_start_date

        is_college = self.is_college

        league = self.league

        sport = self.sport

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_title is not UNSET:
            field_dict["pageTitle"] = page_title
        if alt_title is not UNSET:
            field_dict["altTitle"] = alt_title
        if schedule_start_date is not UNSET:
            field_dict["scheduleStartDate"] = schedule_start_date
        if is_college is not UNSET:
            field_dict["isCollege"] = is_college
        if league is not UNSET:
            field_dict["league"] = league
        if sport is not UNSET:
            field_dict["sport"] = sport

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        page_title = d.pop("pageTitle", UNSET)

        alt_title = d.pop("altTitle", UNSET)

        schedule_start_date = d.pop("scheduleStartDate", UNSET)

        is_college = d.pop("isCollege", UNSET)

        league = d.pop("league", UNSET)

        sport = d.pop("sport", UNSET)

        scoreboard_sb_group = cls(
            page_title=page_title,
            alt_title=alt_title,
            schedule_start_date=schedule_start_date,
            is_college=is_college,
            league=league,
            sport=sport,
        )

        scoreboard_sb_group.additional_properties = d
        return scoreboard_sb_group

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
