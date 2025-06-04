from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_stat import RecordStat


T = TypeVar("T", bound="TeamRecordItem")


@_attrs_define
class TeamRecordItem:
    """Individual team record entry

    Attributes:
        id (str): Record type identifier Example: 0.
        name (str): Internal name of the record type Example: overall.
        type (str): Type of record Example: total.
        summary (str): Summary of the record (e.g., "15-2") Example: 15-2.
        display_value (str): Display value of the record Example: 15-2.
        stats (List['RecordStat']): Detailed statistics for this record type
        ref (Union[Unset, str]): API reference URL for this record
        display_name (Union[Unset, str]): Display name of the record type Example: Home.
        short_display_name (Union[Unset, str]): Short display name Example: HOME.
        description (Union[Unset, str]): Description of the record type Example: Home Record.
        abbreviation (Union[Unset, str]): Abbreviation for the record type Example: Any.
        value (Union[Unset, float]): Numeric value (usually win percentage) Example: 0.8823529411764706.
    """

    id: str
    name: str
    type: str
    summary: str
    display_value: str
    stats: List["RecordStat"]
    ref: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    short_display_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    value: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        type = self.type

        summary = self.summary

        display_value = self.display_value

        stats = []
        for stats_item_data in self.stats:
            stats_item = stats_item_data.to_dict()
            stats.append(stats_item)

        ref = self.ref

        display_name = self.display_name

        short_display_name = self.short_display_name

        description = self.description

        abbreviation = self.abbreviation

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type,
                "summary": summary,
                "displayValue": display_value,
                "stats": stats,
            }
        )
        if ref is not UNSET:
            field_dict["$ref"] = ref
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if short_display_name is not UNSET:
            field_dict["shortDisplayName"] = short_display_name
        if description is not UNSET:
            field_dict["description"] = description
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record_stat import RecordStat

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        type = d.pop("type")

        summary = d.pop("summary")

        display_value = d.pop("displayValue")

        stats = []
        _stats = d.pop("stats")
        for stats_item_data in _stats:
            stats_item = RecordStat.from_dict(stats_item_data)

            stats.append(stats_item)

        ref = d.pop("$ref", UNSET)

        display_name = d.pop("displayName", UNSET)

        short_display_name = d.pop("shortDisplayName", UNSET)

        description = d.pop("description", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        value = d.pop("value", UNSET)

        team_record_item = cls(
            id=id,
            name=name,
            type=type,
            summary=summary,
            display_value=display_value,
            stats=stats,
            ref=ref,
            display_name=display_name,
            short_display_name=short_display_name,
            description=description,
            abbreviation=abbreviation,
            value=value,
        )

        team_record_item.additional_properties = d
        return team_record_item

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
