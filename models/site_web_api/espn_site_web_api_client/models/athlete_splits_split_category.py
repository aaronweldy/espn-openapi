from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.athlete_splits_split import AthleteSplitsSplit


T = TypeVar("T", bound="AthleteSplitsSplitCategory")


@_attrs_define
class AthleteSplitsSplitCategory:
    """Split category in NFL Athlete Splits response.

    Attributes:
        name (str):
        display_name (str):
        splits (Union[List['AthleteSplitsSplit'], None, Unset]):
    """

    name: str
    display_name: str
    splits: Union[List["AthleteSplitsSplit"], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        display_name = self.display_name

        splits: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.splits, Unset):
            splits = UNSET
        elif isinstance(self.splits, list):
            splits = []
            for splits_type_0_item_data in self.splits:
                splits_type_0_item = splits_type_0_item_data.to_dict()
                splits.append(splits_type_0_item)

        else:
            splits = self.splits

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "displayName": display_name,
            }
        )
        if splits is not UNSET:
            field_dict["splits"] = splits

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.athlete_splits_split import AthleteSplitsSplit

        d = src_dict.copy()
        name = d.pop("name")

        display_name = d.pop("displayName")

        def _parse_splits(data: object) -> Union[List["AthleteSplitsSplit"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                splits_type_0 = []
                _splits_type_0 = data
                for splits_type_0_item_data in _splits_type_0:
                    splits_type_0_item = AthleteSplitsSplit.from_dict(splits_type_0_item_data)

                    splits_type_0.append(splits_type_0_item)

                return splits_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["AthleteSplitsSplit"], None, Unset], data)

        splits = _parse_splits(d.pop("splits", UNSET))

        athlete_splits_split_category = cls(
            name=name,
            display_name=display_name,
            splits=splits,
        )

        athlete_splits_split_category.additional_properties = d
        return athlete_splits_split_category

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
