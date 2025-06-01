from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reference import Reference


T = TypeVar("T", bound="CoachDetailsResponseRecordsItem")


@_attrs_define
class CoachDetailsResponseRecordsItem:
    """
    Attributes:
        team (Union[Unset, Reference]):
        record (Union[Unset, Reference]):
    """

    team: Union[Unset, "Reference"] = UNSET
    record: Union[Unset, "Reference"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        record: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record, Unset):
            record = self.record.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if team is not UNSET:
            field_dict["team"] = team
        if record is not UNSET:
            field_dict["record"] = record

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reference import Reference

        d = src_dict.copy()
        _team = d.pop("team", UNSET)
        team: Union[Unset, Reference]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = Reference.from_dict(_team)

        _record = d.pop("record", UNSET)
        record: Union[Unset, Reference]
        if isinstance(_record, Unset):
            record = UNSET
        else:
            record = Reference.from_dict(_record)

        coach_details_response_records_item = cls(
            team=team,
            record=record,
        )

        coach_details_response_records_item.additional_properties = d
        return coach_details_response_records_item

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
