from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.web_mobile_links import WebMobileLinks


T = TypeVar("T", bound="AthleteLinks")


@_attrs_define
class AthleteLinks:
    """
    Attributes:
        web (WebMobileLinks):
        mobile (WebMobileLinks):
    """

    web: "WebMobileLinks"
    mobile: "WebMobileLinks"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        web = self.web.to_dict()

        mobile = self.mobile.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "web": web,
                "mobile": mobile,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.web_mobile_links import WebMobileLinks

        d = src_dict.copy()
        web = WebMobileLinks.from_dict(d.pop("web"))

        mobile = WebMobileLinks.from_dict(d.pop("mobile"))

        athlete_links = cls(
            web=web,
            mobile=mobile,
        )

        athlete_links.additional_properties = d
        return athlete_links

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
