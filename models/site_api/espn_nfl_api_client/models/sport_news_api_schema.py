from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.news_article import NewsArticle
    from ..models.news_link import NewsLink


T = TypeVar("T", bound="SportNewsAPISchema")


@_attrs_define
class SportNewsAPISchema:
    """
    Attributes:
        header (str): Header title for the news feed Example: NFL News.
        articles (List['NewsArticle']):
        link (NewsLink):
    """

    header: str
    articles: List["NewsArticle"]
    link: "NewsLink"
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
        from ..models.news_article import NewsArticle
        from ..models.news_link import NewsLink

        d = src_dict.copy()
        header = d.pop("header")

        articles = []
        _articles = d.pop("articles")
        for articles_item_data in _articles:
            articles_item = NewsArticle.from_dict(articles_item_data)

            articles.append(articles_item)

        link = NewsLink.from_dict(d.pop("link"))

        sport_news_api_schema = cls(
            header=header,
            articles=articles,
            link=link,
        )

        sport_news_api_schema.additional_properties = d
        return sport_news_api_schema

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
