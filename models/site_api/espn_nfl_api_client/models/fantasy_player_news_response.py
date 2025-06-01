import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.fantasy_player_news_item import FantasyPlayerNewsItem


T = TypeVar("T", bound="FantasyPlayerNewsResponse")


@_attrs_define
class FantasyPlayerNewsResponse:
    """Fantasy player news response

    Attributes:
        feed (List['FantasyPlayerNewsItem']): Array of news items
        results_count (int): Total number of results
        results_limit (int): Maximum results per page
        results_offset (int): Offset for pagination
        status (str): Response status
        timestamp (datetime.datetime): Response timestamp
    """

    feed: List["FantasyPlayerNewsItem"]
    results_count: int
    results_limit: int
    results_offset: int
    status: str
    timestamp: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        feed = []
        for feed_item_data in self.feed:
            feed_item = feed_item_data.to_dict()
            feed.append(feed_item)

        results_count = self.results_count

        results_limit = self.results_limit

        results_offset = self.results_offset

        status = self.status

        timestamp = self.timestamp.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feed": feed,
                "resultsCount": results_count,
                "resultsLimit": results_limit,
                "resultsOffset": results_offset,
                "status": status,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fantasy_player_news_item import FantasyPlayerNewsItem

        d = src_dict.copy()
        feed = []
        _feed = d.pop("feed")
        for feed_item_data in _feed:
            feed_item = FantasyPlayerNewsItem.from_dict(feed_item_data)

            feed.append(feed_item)

        results_count = d.pop("resultsCount")

        results_limit = d.pop("resultsLimit")

        results_offset = d.pop("resultsOffset")

        status = d.pop("status")

        timestamp = isoparse(d.pop("timestamp"))

        fantasy_player_news_response = cls(
            feed=feed,
            results_count=results_count,
            results_limit=results_limit,
            results_offset=results_offset,
            status=status,
            timestamp=timestamp,
        )

        fantasy_player_news_response.additional_properties = d
        return fantasy_player_news_response

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
