from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.article import Article
    from ..models.link import Link


T = TypeVar("T", bound="NewsResponse")


@_attrs_define
class NewsResponse:
    """
    Attributes:
        header (str): Header title for the news feed Example: NFL News.
        articles (List['Article']):
        link (Link):
    """

    header: str
    articles: List["Article"]
    link: "Link"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        header = self.header

        articles = []
        for articles_item_data in self.articles:
            articles_item = articles_item_data.to_dict()
            articles.append(articles_item)

        link = self.link.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "header": header,
                "articles": articles,
                "link": link,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.article import Article
        from ..models.link import Link

        d = src_dict.copy()
        header = d.pop("header")

        articles = []
        _articles = d.pop("articles")
        for articles_item_data in _articles:
            articles_item = Article.from_dict(articles_item_data)

            articles.append(articles_item)

        link = Link.from_dict(d.pop("link"))

        news_response = cls(
            header=header,
            articles=articles,
            link=link,
        )

        news_response.additional_properties = d
        return news_response

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
