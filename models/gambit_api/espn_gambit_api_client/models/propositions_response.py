from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.proposition import Proposition


T = TypeVar("T", bound="PropositionsResponse")


@_attrs_define
class PropositionsResponse:
    """
    Attributes:
        challenge_id (Union[Unset, str]):
        propositions (Union[Unset, List['Proposition']]):
    """

    challenge_id: Union[Unset, str] = UNSET
    propositions: Union[Unset, List["Proposition"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        challenge_id = self.challenge_id

        propositions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.propositions, Unset):
            propositions = []
            for propositions_item_data in self.propositions:
                propositions_item = propositions_item_data.to_dict()
                propositions.append(propositions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if challenge_id is not UNSET:
            field_dict["challengeId"] = challenge_id
        if propositions is not UNSET:
            field_dict["propositions"] = propositions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.proposition import Proposition

        d = src_dict.copy()
        challenge_id = d.pop("challengeId", UNSET)

        propositions = []
        _propositions = d.pop("propositions", UNSET)
        for propositions_item_data in _propositions or []:
            propositions_item = Proposition.from_dict(propositions_item_data)

            propositions.append(propositions_item)

        propositions_response = cls(
            challenge_id=challenge_id,
            propositions=propositions,
        )

        propositions_response.additional_properties = d
        return propositions_response

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
