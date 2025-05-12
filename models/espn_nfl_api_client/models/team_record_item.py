from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_record_stat import TeamRecordStat


T = TypeVar("T", bound="TeamRecordItem")


@_attrs_define
class TeamRecordItem:
    """
    Attributes:
        type_ (Union[Unset, str]):  Example: total.
        summary (Union[Unset, str]):  Example: 15-2.
        description (Union[Unset, str]):  Example: Home Record.
        stats (Union[Unset, list['TeamRecordStat']]):
    """

    type_: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    stats: Union[Unset, list["TeamRecordStat"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        summary = self.summary

        description = self.description

        stats: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = []
            for stats_item_data in self.stats:
                stats_item = stats_item_data.to_dict()
                stats.append(stats_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if summary is not UNSET:
            field_dict["summary"] = summary
        if description is not UNSET:
            field_dict["description"] = description
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_record_stat import TeamRecordStat

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        summary = d.pop("summary", UNSET)

        description = d.pop("description", UNSET)

        stats = []
        _stats = d.pop("stats", UNSET)
        for stats_item_data in _stats or []:
            stats_item = TeamRecordStat.from_dict(stats_item_data)

            stats.append(stats_item)

        team_record_item = cls(
            type_=type_,
            summary=summary,
            description=description,
            stats=stats,
        )

        team_record_item.additional_properties = d
        return team_record_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
