import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reference import Reference
    from ..models.season_type import SeasonType
    from ..models.season_types_list import SeasonTypesList


T = TypeVar("T", bound="LeagueSeason")


@_attrs_define
class LeagueSeason:
    """
    Attributes:
        year (int):  Example: 2024.
        start_date (datetime.datetime):
        end_date (datetime.datetime):
        display_name (str):  Example: 2024.
        ref (Union[Unset, str]):
        type (Union[Unset, SeasonType]):
        types (Union[Unset, SeasonTypesList]):
        rankings (Union[Unset, Reference]):
        athletes (Union[Unset, Reference]):
        futures (Union[Unset, Reference]):
        leaders (Union[Unset, Reference]):
        coaches (Union[Unset, Reference]):
        awards (Union[Unset, Reference]):
        power_indexes (Union[Unset, Reference]):
        power_index_leaders (Union[Unset, Reference]):
    """

    year: int
    start_date: datetime.datetime
    end_date: datetime.datetime
    display_name: str
    ref: Union[Unset, str] = UNSET
    type: Union[Unset, "SeasonType"] = UNSET
    types: Union[Unset, "SeasonTypesList"] = UNSET
    rankings: Union[Unset, "Reference"] = UNSET
    athletes: Union[Unset, "Reference"] = UNSET
    futures: Union[Unset, "Reference"] = UNSET
    leaders: Union[Unset, "Reference"] = UNSET
    coaches: Union[Unset, "Reference"] = UNSET
    awards: Union[Unset, "Reference"] = UNSET
    power_indexes: Union[Unset, "Reference"] = UNSET
    power_index_leaders: Union[Unset, "Reference"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        year = self.year

        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        display_name = self.display_name

        ref = self.ref

        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        types: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.types, Unset):
            types = self.types.to_dict()

        rankings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rankings, Unset):
            rankings = self.rankings.to_dict()

        athletes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.athletes, Unset):
            athletes = self.athletes.to_dict()

        futures: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.futures, Unset):
            futures = self.futures.to_dict()

        leaders: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.leaders, Unset):
            leaders = self.leaders.to_dict()

        coaches: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.coaches, Unset):
            coaches = self.coaches.to_dict()

        awards: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.awards, Unset):
            awards = self.awards.to_dict()

        power_indexes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.power_indexes, Unset):
            power_indexes = self.power_indexes.to_dict()

        power_index_leaders: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.power_index_leaders, Unset):
            power_index_leaders = self.power_index_leaders.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "year": year,
                "startDate": start_date,
                "endDate": end_date,
                "displayName": display_name,
            }
        )
        if ref is not UNSET:
            field_dict["$ref"] = ref
        if type is not UNSET:
            field_dict["type"] = type
        if types is not UNSET:
            field_dict["types"] = types
        if rankings is not UNSET:
            field_dict["rankings"] = rankings
        if athletes is not UNSET:
            field_dict["athletes"] = athletes
        if futures is not UNSET:
            field_dict["futures"] = futures
        if leaders is not UNSET:
            field_dict["leaders"] = leaders
        if coaches is not UNSET:
            field_dict["coaches"] = coaches
        if awards is not UNSET:
            field_dict["awards"] = awards
        if power_indexes is not UNSET:
            field_dict["powerIndexes"] = power_indexes
        if power_index_leaders is not UNSET:
            field_dict["powerIndexLeaders"] = power_index_leaders

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reference import Reference
        from ..models.season_type import SeasonType
        from ..models.season_types_list import SeasonTypesList

        d = src_dict.copy()
        year = d.pop("year")

        start_date = isoparse(d.pop("startDate"))

        end_date = isoparse(d.pop("endDate"))

        display_name = d.pop("displayName")

        ref = d.pop("$ref", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, SeasonType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = SeasonType.from_dict(_type)

        _types = d.pop("types", UNSET)
        types: Union[Unset, SeasonTypesList]
        if isinstance(_types, Unset):
            types = UNSET
        else:
            types = SeasonTypesList.from_dict(_types)

        _rankings = d.pop("rankings", UNSET)
        rankings: Union[Unset, Reference]
        if isinstance(_rankings, Unset):
            rankings = UNSET
        else:
            rankings = Reference.from_dict(_rankings)

        _athletes = d.pop("athletes", UNSET)
        athletes: Union[Unset, Reference]
        if isinstance(_athletes, Unset):
            athletes = UNSET
        else:
            athletes = Reference.from_dict(_athletes)

        _futures = d.pop("futures", UNSET)
        futures: Union[Unset, Reference]
        if isinstance(_futures, Unset):
            futures = UNSET
        else:
            futures = Reference.from_dict(_futures)

        _leaders = d.pop("leaders", UNSET)
        leaders: Union[Unset, Reference]
        if isinstance(_leaders, Unset):
            leaders = UNSET
        else:
            leaders = Reference.from_dict(_leaders)

        _coaches = d.pop("coaches", UNSET)
        coaches: Union[Unset, Reference]
        if isinstance(_coaches, Unset):
            coaches = UNSET
        else:
            coaches = Reference.from_dict(_coaches)

        _awards = d.pop("awards", UNSET)
        awards: Union[Unset, Reference]
        if isinstance(_awards, Unset):
            awards = UNSET
        else:
            awards = Reference.from_dict(_awards)

        _power_indexes = d.pop("powerIndexes", UNSET)
        power_indexes: Union[Unset, Reference]
        if isinstance(_power_indexes, Unset):
            power_indexes = UNSET
        else:
            power_indexes = Reference.from_dict(_power_indexes)

        _power_index_leaders = d.pop("powerIndexLeaders", UNSET)
        power_index_leaders: Union[Unset, Reference]
        if isinstance(_power_index_leaders, Unset):
            power_index_leaders = UNSET
        else:
            power_index_leaders = Reference.from_dict(_power_index_leaders)

        league_season = cls(
            year=year,
            start_date=start_date,
            end_date=end_date,
            display_name=display_name,
            ref=ref,
            type=type,
            types=types,
            rankings=rankings,
            athletes=athletes,
            futures=futures,
            leaders=leaders,
            coaches=coaches,
            awards=awards,
            power_indexes=power_indexes,
            power_index_leaders=power_index_leaders,
        )

        league_season.additional_properties = d
        return league_season

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
