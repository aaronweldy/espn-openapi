from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DraftAthleteAnalysis")


@_attrs_define
class DraftAthleteAnalysis:
    """
    Attributes:
        id (str):
        type (str):
        text (Union[Unset, str]):
        grade (Union[Unset, int]):
    """

    id: str
    type: str
    text: Union[Unset, str] = UNSET
    grade: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type

        text = self.text

        grade = self.grade

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
            }
        )
        if text is not UNSET:
            field_dict["text"] = text
        if grade is not UNSET:
            field_dict["grade"] = grade

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        type = d.pop("type")

        text = d.pop("text", UNSET)

        grade = d.pop("grade", UNSET)

        draft_athlete_analysis = cls(
            id=id,
            type=type,
            text=text,
            grade=grade,
        )

        draft_athlete_analysis.additional_properties = d
        return draft_athlete_analysis

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
