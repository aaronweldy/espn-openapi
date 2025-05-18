from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.athlete_profile_response_athlete import AthleteProfileResponseAthlete


T = TypeVar("T", bound="AthleteProfileResponse")


@_attrs_define
class AthleteProfileResponse:
    """
    Attributes:
        athlete (AthleteProfileResponseAthlete):
    """

    athlete: "AthleteProfileResponseAthlete"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        athlete = self.athlete.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "athlete": athlete,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.athlete_profile_response_athlete import AthleteProfileResponseAthlete

        d = src_dict.copy()
        athlete = AthleteProfileResponseAthlete.from_dict(d.pop("athlete"))

        athlete_profile_response = cls(
            athlete=athlete,
        )

        athlete_profile_response.additional_properties = d
        return athlete_profile_response

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
