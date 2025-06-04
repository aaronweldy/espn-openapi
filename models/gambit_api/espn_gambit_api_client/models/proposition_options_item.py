from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PropositionOptionsItem")


@_attrs_define
class PropositionOptionsItem:
    """
    Attributes:
        id (Union[Unset, str]):
        text (Union[Unset, str]):
        winner (Union[None, Unset, bool]):
    """

    id: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    winner: Union[None, Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        text = self.text

        winner: Union[None, Unset, bool]
        if isinstance(self.winner, Unset):
            winner = UNSET
        else:
            winner = self.winner

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if text is not UNSET:
            field_dict["text"] = text
        if winner is not UNSET:
            field_dict["winner"] = winner

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        text = d.pop("text", UNSET)

        def _parse_winner(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        winner = _parse_winner(d.pop("winner", UNSET))

        proposition_options_item = cls(
            id=id,
            text=text,
            winner=winner,
        )

        proposition_options_item.additional_properties = d
        return proposition_options_item

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
