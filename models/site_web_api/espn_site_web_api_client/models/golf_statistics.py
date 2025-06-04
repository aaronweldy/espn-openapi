from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.golf_stat_split import GolfStatSplit


T = TypeVar("T", bound="GolfStatistics")


@_attrs_define
class GolfStatistics:
    """
    Attributes:
        display_name (str): Display name for the statistics set (e.g., "2024 Season Overview")
        labels (List[str]): Short labels for statistics (e.g., "EVENTS", "CUTS")
        names (List[str]): Full names for statistics (e.g., "Tournaments Played")
        display_names (List[str]): Display names for statistics (e.g., "Tournaments played")
        splits (List['GolfStatSplit']): Statistical splits
    """

    display_name: str
    labels: List[str]
    names: List[str]
    display_names: List[str]
    splits: List["GolfStatSplit"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name

        labels = self.labels

        names = self.names

        display_names = self.display_names

        splits = []
        for splits_item_data in self.splits:
            splits_item = splits_item_data.to_dict()
            splits.append(splits_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayName": display_name,
                "labels": labels,
                "names": names,
                "displayNames": display_names,
                "splits": splits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.golf_stat_split import GolfStatSplit

        d = src_dict.copy()
        display_name = d.pop("displayName")

        labels = cast(List[str], d.pop("labels"))

        names = cast(List[str], d.pop("names"))

        display_names = cast(List[str], d.pop("displayNames"))

        splits = []
        _splits = d.pop("splits")
        for splits_item_data in _splits:
            splits_item = GolfStatSplit.from_dict(splits_item_data)

            splits.append(splits_item)

        golf_statistics = cls(
            display_name=display_name,
            labels=labels,
            names=names,
            display_names=display_names,
            splits=splits,
        )

        golf_statistics.additional_properties = d
        return golf_statistics

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
