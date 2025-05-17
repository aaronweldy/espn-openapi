from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.news_link_item import NewsLinkItem


T = TypeVar("T", bound="NewsArticleLinksApp")


@_attrs_define
class NewsArticleLinksApp:
    """
    Attributes:
        sportscenter (Union[Unset, NewsLinkItem]):
    """

    sportscenter: Union[Unset, "NewsLinkItem"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sportscenter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sportscenter, Unset):
            sportscenter = self.sportscenter.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sportscenter is not UNSET:
            field_dict["sportscenter"] = sportscenter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.news_link_item import NewsLinkItem

        d = src_dict.copy()
        _sportscenter = d.pop("sportscenter", UNSET)
        sportscenter: Union[Unset, NewsLinkItem]
        if isinstance(_sportscenter, Unset):
            sportscenter = UNSET
        else:
            sportscenter = NewsLinkItem.from_dict(_sportscenter)

        news_article_links_app = cls(
            sportscenter=sportscenter,
        )

        news_article_links_app.additional_properties = d
        return news_article_links_app

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
