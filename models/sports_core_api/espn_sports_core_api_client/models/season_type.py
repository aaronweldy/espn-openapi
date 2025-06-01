import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reference import Reference
    from ..models.season_week import SeasonWeek


T = TypeVar("T", bound="SeasonType")


@_attrs_define
class SeasonType:
    """
    Attributes:
        id (str):
        type (int):
        name (str):
        abbreviation (str):
        ref (Union[Unset, str]):
        year (Union[Unset, int]):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        has_groups (Union[Unset, bool]):
        has_standings (Union[Unset, bool]):
        has_legs (Union[Unset, bool]):
        groups (Union[Unset, Reference]):
        weeks (Union[Unset, Reference]):
        week (Union[Unset, SeasonWeek]):
        corrections (Union[Unset, Reference]):
        leaders (Union[Unset, Reference]):
        slug (Union[Unset, str]):
    """

    id: str
    type: int
    name: str
    abbreviation: str
    ref: Union[Unset, str] = UNSET
    year: Union[Unset, int] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    has_groups: Union[Unset, bool] = UNSET
    has_standings: Union[Unset, bool] = UNSET
    has_legs: Union[Unset, bool] = UNSET
    groups: Union[Unset, "Reference"] = UNSET
    weeks: Union[Unset, "Reference"] = UNSET
    week: Union[Unset, "SeasonWeek"] = UNSET
    corrections: Union[Unset, "Reference"] = UNSET
    leaders: Union[Unset, "Reference"] = UNSET
    slug: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type

        name = self.name

        abbreviation = self.abbreviation

        ref = self.ref

        year = self.year

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        has_groups = self.has_groups

        has_standings = self.has_standings

        has_legs = self.has_legs

        groups: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups.to_dict()

        weeks: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.weeks, Unset):
            weeks = self.weeks.to_dict()

        week: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.week, Unset):
            week = self.week.to_dict()

        corrections: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.corrections, Unset):
            corrections = self.corrections.to_dict()

        leaders: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.leaders, Unset):
            leaders = self.leaders.to_dict()

        slug = self.slug

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
                "name": name,
                "abbreviation": abbreviation,
            }
        )
        if ref is not UNSET:
            field_dict["$ref"] = ref
        if year is not UNSET:
            field_dict["year"] = year
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if has_groups is not UNSET:
            field_dict["hasGroups"] = has_groups
        if has_standings is not UNSET:
            field_dict["hasStandings"] = has_standings
        if has_legs is not UNSET:
            field_dict["hasLegs"] = has_legs
        if groups is not UNSET:
            field_dict["groups"] = groups
        if weeks is not UNSET:
            field_dict["weeks"] = weeks
        if week is not UNSET:
            field_dict["week"] = week
        if corrections is not UNSET:
            field_dict["corrections"] = corrections
        if leaders is not UNSET:
            field_dict["leaders"] = leaders
        if slug is not UNSET:
            field_dict["slug"] = slug

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reference import Reference
        from ..models.season_week import SeasonWeek

        d = src_dict.copy()
        id = d.pop("id")

        type = d.pop("type")

        name = d.pop("name")

        abbreviation = d.pop("abbreviation")

        ref = d.pop("$ref", UNSET)

        year = d.pop("year", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        has_groups = d.pop("hasGroups", UNSET)

        has_standings = d.pop("hasStandings", UNSET)

        has_legs = d.pop("hasLegs", UNSET)

        _groups = d.pop("groups", UNSET)
        groups: Union[Unset, Reference]
        if isinstance(_groups, Unset):
            groups = UNSET
        else:
            groups = Reference.from_dict(_groups)

        _weeks = d.pop("weeks", UNSET)
        weeks: Union[Unset, Reference]
        if isinstance(_weeks, Unset):
            weeks = UNSET
        else:
            weeks = Reference.from_dict(_weeks)

        _week = d.pop("week", UNSET)
        week: Union[Unset, SeasonWeek]
        if isinstance(_week, Unset):
            week = UNSET
        else:
            week = SeasonWeek.from_dict(_week)

        _corrections = d.pop("corrections", UNSET)
        corrections: Union[Unset, Reference]
        if isinstance(_corrections, Unset):
            corrections = UNSET
        else:
            corrections = Reference.from_dict(_corrections)

        _leaders = d.pop("leaders", UNSET)
        leaders: Union[Unset, Reference]
        if isinstance(_leaders, Unset):
            leaders = UNSET
        else:
            leaders = Reference.from_dict(_leaders)

        slug = d.pop("slug", UNSET)

        season_type = cls(
            id=id,
            type=type,
            name=name,
            abbreviation=abbreviation,
            ref=ref,
            year=year,
            start_date=start_date,
            end_date=end_date,
            has_groups=has_groups,
            has_standings=has_standings,
            has_legs=has_legs,
            groups=groups,
            weeks=weeks,
            week=week,
            corrections=corrections,
            leaders=leaders,
            slug=slug,
        )

        season_type.additional_properties = d
        return season_type

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
