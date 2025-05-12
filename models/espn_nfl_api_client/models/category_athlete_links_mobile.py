from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="CategoryAthleteLinksMobile")


@_attrs_define
class CategoryAthleteLinksMobile:
    """
    Attributes:
        athletes (Union[Unset, Link]):
    """

    athletes: Union[Unset, "Link"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        athletes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.athletes, Unset):
            athletes = self.athletes.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if athletes is not UNSET:
            field_dict["athletes"] = athletes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link import Link

        d = src_dict.copy()
        _athletes = d.pop("athletes", UNSET)
        athletes: Union[Unset, Link]
        if isinstance(_athletes, Unset):
            athletes = UNSET
        else:
            athletes = Link.from_dict(_athletes)

        category_athlete_links_mobile = cls(
            athletes=athletes,
        )

        category_athlete_links_mobile.additional_properties = d
        return category_athlete_links_mobile

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
