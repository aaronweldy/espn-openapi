from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scoreboard_content import ScoreboardContent
    from ..models.scoreboard_news import ScoreboardNews


T = TypeVar("T", bound="NflScoreboardResponse")


@_attrs_define
class NflScoreboardResponse:
    """
    Attributes:
        news (Union[Unset, ScoreboardNews]):
        pinned_count (Union[Unset, int]):
        now_feed_md5_hash (Union[Unset, str]):
        type (Union[Unset, str]):
        content (Union[Unset, ScoreboardContent]):
    """

    news: Union[Unset, "ScoreboardNews"] = UNSET
    pinned_count: Union[Unset, int] = UNSET
    now_feed_md5_hash: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    content: Union[Unset, "ScoreboardContent"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        news: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.news, Unset):
            news = self.news.to_dict()

        pinned_count = self.pinned_count

        now_feed_md5_hash = self.now_feed_md5_hash

        type = self.type

        content: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if news is not UNSET:
            field_dict["news"] = news
        if pinned_count is not UNSET:
            field_dict["pinnedCount"] = pinned_count
        if now_feed_md5_hash is not UNSET:
            field_dict["nowFeedMD5Hash"] = now_feed_md5_hash
        if type is not UNSET:
            field_dict["type"] = type
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scoreboard_content import ScoreboardContent
        from ..models.scoreboard_news import ScoreboardNews

        d = src_dict.copy()
        _news = d.pop("news", UNSET)
        news: Union[Unset, ScoreboardNews]
        if isinstance(_news, Unset):
            news = UNSET
        else:
            news = ScoreboardNews.from_dict(_news)

        pinned_count = d.pop("pinnedCount", UNSET)

        now_feed_md5_hash = d.pop("nowFeedMD5Hash", UNSET)

        type = d.pop("type", UNSET)

        _content = d.pop("content", UNSET)
        content: Union[Unset, ScoreboardContent]
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = ScoreboardContent.from_dict(_content)

        nfl_scoreboard_response = cls(
            news=news,
            pinned_count=pinned_count,
            now_feed_md5_hash=now_feed_md5_hash,
            type=type,
            content=content,
        )

        nfl_scoreboard_response.additional_properties = d
        return nfl_scoreboard_response

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
