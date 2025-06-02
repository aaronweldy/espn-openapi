from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_stat import RecordStat


T = TypeVar("T", bound="TeamRecord")


@_attrs_define
class TeamRecord:
    """Individual team record (overall, home, away, etc.)

    Attributes:
        ref (str): Reference URL for the record
        id (str): Record ID Example: 369.
        name (str): Internal name of the record type Example: overall.
        display_name (str): Display name of the record Example: Record Year To Date.
        type (str): Type of record Example: total.
        abbreviation (Union[Unset, str]): Abbreviation for the record Example: Game.
        short_display_name (Union[Unset, str]): Short display name Example: YTD.
        description (Union[Unset, str]): Description of the record type Example: Overall Record.
        summary (Union[Unset, str]): Summary of the record (wins-losses) Example: 2-0.
        display_value (Union[Unset, str]): Display value of the record Example: 2-0.
        value (Union[Unset, float]): Numeric value (usually win percentage) Example: 1.0.
        stats (Union[Unset, List['RecordStat']]): Array of detailed statistics for this record
    """

    ref: str
    id: str
    name: str
    display_name: str
    type: str
    abbreviation: Union[Unset, str] = UNSET
    short_display_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    display_value: Union[Unset, str] = UNSET
    value: Union[Unset, float] = UNSET
    stats: Union[Unset, List["RecordStat"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        id = self.id

        name = self.name

        display_name = self.display_name

        type = self.type

        abbreviation = self.abbreviation

        short_display_name = self.short_display_name

        description = self.description

        summary = self.summary

        display_value = self.display_value

        value = self.value

        stats: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = []
            for stats_item_data in self.stats:
                stats_item = stats_item_data.to_dict()
                stats.append(stats_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "id": id,
                "name": name,
                "displayName": display_name,
                "type": type,
            }
        )
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if short_display_name is not UNSET:
            field_dict["shortDisplayName"] = short_display_name
        if description is not UNSET:
            field_dict["description"] = description
        if summary is not UNSET:
            field_dict["summary"] = summary
        if display_value is not UNSET:
            field_dict["displayValue"] = display_value
        if value is not UNSET:
            field_dict["value"] = value
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record_stat import RecordStat

        d = src_dict.copy()
        ref = d.pop("$ref")

        id = d.pop("id")

        name = d.pop("name")

        display_name = d.pop("displayName")

        type = d.pop("type")

        abbreviation = d.pop("abbreviation", UNSET)

        short_display_name = d.pop("shortDisplayName", UNSET)

        description = d.pop("description", UNSET)

        summary = d.pop("summary", UNSET)

        display_value = d.pop("displayValue", UNSET)

        value = d.pop("value", UNSET)

        stats = []
        _stats = d.pop("stats", UNSET)
        for stats_item_data in _stats or []:
            stats_item = RecordStat.from_dict(stats_item_data)

            stats.append(stats_item)

        team_record = cls(
            ref=ref,
            id=id,
            name=name,
            display_name=display_name,
            type=type,
            abbreviation=abbreviation,
            short_display_name=short_display_name,
            description=description,
            summary=summary,
            display_value=display_value,
            value=value,
            stats=stats,
        )

        team_record.additional_properties = d
        return team_record

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
