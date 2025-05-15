from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.self_link import SelfLink


T = TypeVar("T", bound="AuthorLinksType0")


@_attrs_define
class AuthorLinksType0:
    """
    Attributes:
        api (Union[Unset, SelfLink]):
    """

    api: Union[Unset, "SelfLink"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.api, Unset):
            api = self.api.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api is not UNSET:
            field_dict["api"] = api

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.self_link import SelfLink

        d = src_dict.copy()
        _api = d.pop("api", UNSET)
        api: Union[Unset, SelfLink]
        if isinstance(_api, Unset):
            api = UNSET
        else:
            api = SelfLink.from_dict(_api)

        author_links_type_0 = cls(
            api=api,
        )

        author_links_type_0.additional_properties = d
        return author_links_type_0

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
