from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.proposition_options_item import PropositionOptionsItem


T = TypeVar("T", bound="Proposition")


@_attrs_define
class Proposition:
    """
    Attributes:
        id (Union[Unset, str]):
        type (Union[Unset, str]):
        text (Union[Unset, str]):
        short_text (Union[Unset, str]):
        locked (Union[Unset, bool]):
        scoring_period_id (Union[Unset, int]):
        options (Union[Unset, List['PropositionOptionsItem']]):
    """

    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    short_text: Union[Unset, str] = UNSET
    locked: Union[Unset, bool] = UNSET
    scoring_period_id: Union[Unset, int] = UNSET
    options: Union[Unset, List["PropositionOptionsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type

        text = self.text

        short_text = self.short_text

        locked = self.locked

        scoring_period_id = self.scoring_period_id

        options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type
        if text is not UNSET:
            field_dict["text"] = text
        if short_text is not UNSET:
            field_dict["shortText"] = short_text
        if locked is not UNSET:
            field_dict["locked"] = locked
        if scoring_period_id is not UNSET:
            field_dict["scoringPeriodId"] = scoring_period_id
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.proposition_options_item import PropositionOptionsItem

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        type = d.pop("type", UNSET)

        text = d.pop("text", UNSET)

        short_text = d.pop("shortText", UNSET)

        locked = d.pop("locked", UNSET)

        scoring_period_id = d.pop("scoringPeriodId", UNSET)

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = PropositionOptionsItem.from_dict(options_item_data)

            options.append(options_item)

        proposition = cls(
            id=id,
            type=type,
            text=text,
            short_text=short_text,
            locked=locked,
            scoring_period_id=scoring_period_id,
            options=options,
        )

        proposition.additional_properties = d
        return proposition

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
