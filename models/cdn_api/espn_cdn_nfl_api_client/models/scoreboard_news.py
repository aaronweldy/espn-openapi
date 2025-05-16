from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scoreboard_article import ScoreboardArticle
    from ..models.scoreboard_link import ScoreboardLink


T = TypeVar("T", bound="ScoreboardNews")


@_attrs_define
class ScoreboardNews:
    """
    Attributes:
        link (Union[Unset, ScoreboardLink]):
        header (Union[Unset, str]):
        articles (Union[Unset, List['ScoreboardArticle']]):
    """

    link: Union[Unset, "ScoreboardLink"] = UNSET
    header: Union[Unset, str] = UNSET
    articles: Union[Unset, List["ScoreboardArticle"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        link: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.link, Unset):
            link = self.link.to_dict()

        header = self.header

        articles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.articles, Unset):
            articles = []
            for articles_item_data in self.articles:
                articles_item = articles_item_data.to_dict()
                articles.append(articles_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if link is not UNSET:
            field_dict["link"] = link
        if header is not UNSET:
            field_dict["header"] = header
        if articles is not UNSET:
            field_dict["articles"] = articles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scoreboard_article import ScoreboardArticle
        from ..models.scoreboard_link import ScoreboardLink

        d = src_dict.copy()
        _link = d.pop("link", UNSET)
        link: Union[Unset, ScoreboardLink]
        if isinstance(_link, Unset):
            link = UNSET
        else:
            link = ScoreboardLink.from_dict(_link)

        header = d.pop("header", UNSET)

        articles = []
        _articles = d.pop("articles", UNSET)
        for articles_item_data in _articles or []:
            articles_item = ScoreboardArticle.from_dict(articles_item_data)

            articles.append(articles_item)

        scoreboard_news = cls(
            link=link,
            header=header,
            articles=articles,
        )

        scoreboard_news.additional_properties = d
        return scoreboard_news

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
