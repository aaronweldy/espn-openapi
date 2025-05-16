from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scoreboard_calendar import ScoreboardCalendar
    from ..models.scoreboard_content_date_params import ScoreboardContentDateParams
    from ..models.scoreboard_content_defaults import ScoreboardContentDefaults
    from ..models.scoreboard_sb_data import ScoreboardSbData
    from ..models.scoreboard_sb_group import ScoreboardSbGroup


T = TypeVar("T", bound="ScoreboardContent")


@_attrs_define
class ScoreboardContent:
    """
    Attributes:
        league (Union[Unset, str]):
        sb_group (Union[Unset, ScoreboardSbGroup]):
        sb_data (Union[Unset, ScoreboardSbData]):
        calendar (Union[Unset, List['ScoreboardCalendar']]):
        canonical (Union[Unset, str]):
        date_params (Union[Unset, ScoreboardContentDateParams]):
        defaults (Union[Unset, ScoreboardContentDefaults]):
        description (Union[Unset, str]):
        is_week_oriented (Union[Unset, bool]):
        og_type (Union[Unset, str]):
        title (Union[Unset, str]):
    """

    league: Union[Unset, str] = UNSET
    sb_group: Union[Unset, "ScoreboardSbGroup"] = UNSET
    sb_data: Union[Unset, "ScoreboardSbData"] = UNSET
    calendar: Union[Unset, List["ScoreboardCalendar"]] = UNSET
    canonical: Union[Unset, str] = UNSET
    date_params: Union[Unset, "ScoreboardContentDateParams"] = UNSET
    defaults: Union[Unset, "ScoreboardContentDefaults"] = UNSET
    description: Union[Unset, str] = UNSET
    is_week_oriented: Union[Unset, bool] = UNSET
    og_type: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        league = self.league

        sb_group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sb_group, Unset):
            sb_group = self.sb_group.to_dict()

        sb_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sb_data, Unset):
            sb_data = self.sb_data.to_dict()

        calendar: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.calendar, Unset):
            calendar = []
            for calendar_item_data in self.calendar:
                calendar_item = calendar_item_data.to_dict()
                calendar.append(calendar_item)

        canonical = self.canonical

        date_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.date_params, Unset):
            date_params = self.date_params.to_dict()

        defaults: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.defaults, Unset):
            defaults = self.defaults.to_dict()

        description = self.description

        is_week_oriented = self.is_week_oriented

        og_type = self.og_type

        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if league is not UNSET:
            field_dict["league"] = league
        if sb_group is not UNSET:
            field_dict["sbGroup"] = sb_group
        if sb_data is not UNSET:
            field_dict["sbData"] = sb_data
        if calendar is not UNSET:
            field_dict["calendar"] = calendar
        if canonical is not UNSET:
            field_dict["canonical"] = canonical
        if date_params is not UNSET:
            field_dict["dateParams"] = date_params
        if defaults is not UNSET:
            field_dict["defaults"] = defaults
        if description is not UNSET:
            field_dict["description"] = description
        if is_week_oriented is not UNSET:
            field_dict["isWeekOriented"] = is_week_oriented
        if og_type is not UNSET:
            field_dict["og_type"] = og_type
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scoreboard_calendar import ScoreboardCalendar
        from ..models.scoreboard_content_date_params import ScoreboardContentDateParams
        from ..models.scoreboard_content_defaults import ScoreboardContentDefaults
        from ..models.scoreboard_sb_data import ScoreboardSbData
        from ..models.scoreboard_sb_group import ScoreboardSbGroup

        d = src_dict.copy()
        league = d.pop("league", UNSET)

        _sb_group = d.pop("sbGroup", UNSET)
        sb_group: Union[Unset, ScoreboardSbGroup]
        if isinstance(_sb_group, Unset):
            sb_group = UNSET
        else:
            sb_group = ScoreboardSbGroup.from_dict(_sb_group)

        _sb_data = d.pop("sbData", UNSET)
        sb_data: Union[Unset, ScoreboardSbData]
        if isinstance(_sb_data, Unset):
            sb_data = UNSET
        else:
            sb_data = ScoreboardSbData.from_dict(_sb_data)

        calendar = []
        _calendar = d.pop("calendar", UNSET)
        for calendar_item_data in _calendar or []:
            calendar_item = ScoreboardCalendar.from_dict(calendar_item_data)

            calendar.append(calendar_item)

        canonical = d.pop("canonical", UNSET)

        _date_params = d.pop("dateParams", UNSET)
        date_params: Union[Unset, ScoreboardContentDateParams]
        if isinstance(_date_params, Unset):
            date_params = UNSET
        else:
            date_params = ScoreboardContentDateParams.from_dict(_date_params)

        _defaults = d.pop("defaults", UNSET)
        defaults: Union[Unset, ScoreboardContentDefaults]
        if isinstance(_defaults, Unset):
            defaults = UNSET
        else:
            defaults = ScoreboardContentDefaults.from_dict(_defaults)

        description = d.pop("description", UNSET)

        is_week_oriented = d.pop("isWeekOriented", UNSET)

        og_type = d.pop("og_type", UNSET)

        title = d.pop("title", UNSET)

        scoreboard_content = cls(
            league=league,
            sb_group=sb_group,
            sb_data=sb_data,
            calendar=calendar,
            canonical=canonical,
            date_params=date_params,
            defaults=defaults,
            description=description,
            is_week_oriented=is_week_oriented,
            og_type=og_type,
            title=title,
        )

        scoreboard_content.additional_properties = d
        return scoreboard_content

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
