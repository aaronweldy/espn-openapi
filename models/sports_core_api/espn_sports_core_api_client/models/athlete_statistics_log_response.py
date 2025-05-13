from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.athlete_reference import AthleteReference
    from ..models.statistics_log_entry import StatisticsLogEntry


T = TypeVar("T", bound="AthleteStatisticsLogResponse")


@_attrs_define
class AthleteStatisticsLogResponse:
    """
    Attributes:
        entries (List['StatisticsLogEntry']):
        ref (Union[Unset, str]):  Example:
            http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/athletes/3139477/statisticslog?lang=en&region=us.
        athlete (Union[Unset, AthleteReference]):
    """

    entries: List["StatisticsLogEntry"]
    ref: Union[Unset, str] = UNSET
    athlete: Union[Unset, "AthleteReference"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        ref = self.ref

        athlete: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.athlete, Unset):
            athlete = self.athlete.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entries": entries,
            }
        )
        if ref is not UNSET:
            field_dict["$ref"] = ref
        if athlete is not UNSET:
            field_dict["athlete"] = athlete

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.athlete_reference import AthleteReference
        from ..models.statistics_log_entry import StatisticsLogEntry

        d = src_dict.copy()
        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:
            entries_item = StatisticsLogEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        ref = d.pop("$ref", UNSET)

        _athlete = d.pop("athlete", UNSET)
        athlete: Union[Unset, AthleteReference]
        if isinstance(_athlete, Unset):
            athlete = UNSET
        else:
            athlete = AthleteReference.from_dict(_athlete)

        athlete_statistics_log_response = cls(
            entries=entries,
            ref=ref,
            athlete=athlete,
        )

        athlete_statistics_log_response.additional_properties = d
        return athlete_statistics_log_response

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
