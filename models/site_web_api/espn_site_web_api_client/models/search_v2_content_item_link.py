from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchV2ContentItemLink")


@_attrs_define
class SearchV2ContentItemLink:
    """
    Attributes:
        app (Union[None, Unset, str]):
        web (Union[None, Unset, str]):
    """

    app: Union[None, Unset, str] = UNSET
    web: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        app: Union[None, Unset, str]
        if isinstance(self.app, Unset):
            app = UNSET
        else:
            app = self.app

        web: Union[None, Unset, str]
        if isinstance(self.web, Unset):
            web = UNSET
        else:
            web = self.web

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app is not UNSET:
            field_dict["app"] = app
        if web is not UNSET:
            field_dict["web"] = web

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_app(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        app = _parse_app(d.pop("app", UNSET))

        def _parse_web(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        web = _parse_web(d.pop("web", UNSET))

        search_v2_content_item_link = cls(
            app=app,
            web=web,
        )

        search_v2_content_item_link.additional_properties = d
        return search_v2_content_item_link

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
