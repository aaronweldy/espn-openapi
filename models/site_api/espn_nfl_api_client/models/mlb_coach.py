from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MlbCoach")


@_attrs_define
class MlbCoach:
    """Coach information for MLB team roster

    Attributes:
        id (str):
        first_name (str):
        last_name (str):
        experience (int):
    """

    id: str
    first_name: str
    last_name: str
    experience: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        first_name = self.first_name

        last_name = self.last_name

        experience = self.experience

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "firstName": first_name,
                "lastName": last_name,
                "experience": experience,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        experience = d.pop("experience")

        mlb_coach = cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            experience=experience,
        )

        mlb_coach.additional_properties = d
        return mlb_coach

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
