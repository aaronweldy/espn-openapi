from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContributorIds")


@_attrs_define
class ContributorIds:
    """
    Attributes:
        now (Union[Unset, str]):
        cms (Union[Unset, str]):
        slug (Union[Unset, str]):
        guid (Union[Unset, str]):
    """

    now: Union[Unset, str] = UNSET
    cms: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        now = self.now

        cms = self.cms

        slug = self.slug

        guid = self.guid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if now is not UNSET:
            field_dict["now"] = now
        if cms is not UNSET:
            field_dict["cms"] = cms
        if slug is not UNSET:
            field_dict["slug"] = slug
        if guid is not UNSET:
            field_dict["guid"] = guid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        now = d.pop("now", UNSET)

        cms = d.pop("cms", UNSET)

        slug = d.pop("slug", UNSET)

        guid = d.pop("guid", UNSET)

        contributor_ids = cls(
            now=now,
            cms=cms,
            slug=slug,
            guid=guid,
        )

        contributor_ids.additional_properties = d
        return contributor_ids

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
