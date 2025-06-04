from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contributor_info import ContributorInfo
    from ..models.feed_item import FeedItem


T = TypeVar("T", bound="FlexItem")


@_attrs_define
class FlexItem:
    """
    Attributes:
        type (str): Item type (e.g., contributor-page)
        contributor (Union[Unset, ContributorInfo]):
        count (Union[Unset, int]): Total number of feed items
        page_size (Union[Unset, int]): Number of items per page
        cursor (Union[Unset, str]): Pagination cursor
        feed (Union[Unset, List['FeedItem']]): Array of content feed items
    """

    type: str
    contributor: Union[Unset, "ContributorInfo"] = UNSET
    count: Union[Unset, int] = UNSET
    page_size: Union[Unset, int] = UNSET
    cursor: Union[Unset, str] = UNSET
    feed: Union[Unset, List["FeedItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        contributor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contributor, Unset):
            contributor = self.contributor.to_dict()

        count = self.count

        page_size = self.page_size

        cursor = self.cursor

        feed: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.feed, Unset):
            feed = []
            for feed_item_data in self.feed:
                feed_item = feed_item_data.to_dict()
                feed.append(feed_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if contributor is not UNSET:
            field_dict["contributor"] = contributor
        if count is not UNSET:
            field_dict["count"] = count
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if feed is not UNSET:
            field_dict["feed"] = feed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contributor_info import ContributorInfo
        from ..models.feed_item import FeedItem

        d = src_dict.copy()
        type = d.pop("type")

        _contributor = d.pop("contributor", UNSET)
        contributor: Union[Unset, ContributorInfo]
        if isinstance(_contributor, Unset):
            contributor = UNSET
        else:
            contributor = ContributorInfo.from_dict(_contributor)

        count = d.pop("count", UNSET)

        page_size = d.pop("pageSize", UNSET)

        cursor = d.pop("cursor", UNSET)

        feed = []
        _feed = d.pop("feed", UNSET)
        for feed_item_data in _feed or []:
            feed_item = FeedItem.from_dict(feed_item_data)

            feed.append(feed_item)

        flex_item = cls(
            type=type,
            contributor=contributor,
            count=count,
            page_size=page_size,
            cursor=cursor,
            feed=feed,
        )

        flex_item.additional_properties = d
        return flex_item

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
