from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.future_item_type import FutureItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.future_provider import FutureProvider


T = TypeVar("T", bound="FutureItem")


@_attrs_define
class FutureItem:
    """
    Attributes:
        id (int): Unique identifier for this future Example: 1200.
        name (str): Name of the future bet Example: Total Regular Season Passing Yards.
        futures (List['FutureProvider']):
        ref (Union[Unset, str]): API reference URL for this future
        display_name (Union[Unset, str]): Display name of the future bet Example: Total Regular Season Passing Yards.
        type (Union[Unset, FutureItemType]): Type of future bet Example: winDivision.
    """

    id: int
    name: str
    futures: List["FutureProvider"]
    ref: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    type: Union[Unset, FutureItemType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        futures = []
        for futures_item_data in self.futures:
            futures_item = futures_item_data.to_dict()
            futures.append(futures_item)

        ref = self.ref

        display_name = self.display_name

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "futures": futures,
            }
        )
        if ref is not UNSET:
            field_dict["$ref"] = ref
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.future_provider import FutureProvider

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        futures = []
        _futures = d.pop("futures")
        for futures_item_data in _futures:
            futures_item = FutureProvider.from_dict(futures_item_data)

            futures.append(futures_item)

        ref = d.pop("$ref", UNSET)

        display_name = d.pop("displayName", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, FutureItemType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = FutureItemType(_type)

        future_item = cls(
            id=id,
            name=name,
            futures=futures,
            ref=ref,
            display_name=display_name,
            type=type,
        )

        future_item.additional_properties = d
        return future_item

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
