from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qbr_stat import QBRStat


T = TypeVar("T", bound="QBRCategory")


@_attrs_define
class QBRCategory:
    """
    Attributes:
        name (Union[Unset, str]):  Example: general.
        display_name (Union[Unset, str]):  Example: General.
        short_display_name (Union[Unset, str]):  Example: General.
        abbreviation (Union[Unset, str]):  Example: GEN.
        stats (Union[Unset, List['QBRStat']]):
    """

    name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    short_display_name: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    stats: Union[Unset, List["QBRStat"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        display_name = self.display_name

        short_display_name = self.short_display_name

        abbreviation = self.abbreviation

        stats: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = []
            for stats_item_data in self.stats:
                stats_item = stats_item_data.to_dict()
                stats.append(stats_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if short_display_name is not UNSET:
            field_dict["shortDisplayName"] = short_display_name
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.qbr_stat import QBRStat

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        short_display_name = d.pop("shortDisplayName", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        stats = []
        _stats = d.pop("stats", UNSET)
        for stats_item_data in _stats or []:
            stats_item = QBRStat.from_dict(stats_item_data)

            stats.append(stats_item)

        qbr_category = cls(
            name=name,
            display_name=display_name,
            short_display_name=short_display_name,
            abbreviation=abbreviation,
            stats=stats,
        )

        qbr_category.additional_properties = d
        return qbr_category

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
