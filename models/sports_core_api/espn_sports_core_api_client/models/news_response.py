import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.news_headline import NewsHeadline


T = TypeVar("T", bound="NewsResponse")


@_attrs_define
class NewsResponse:
    """
    Attributes:
        headlines (List['NewsHeadline']):
        results_count (int): Total number of results available
        results_limit (int): Maximum number of results returned
        results_offset (int): Offset for pagination
        status (str): Response status Example: success.
        timestamp (datetime.datetime): Timestamp of the response
    """

    headlines: List["NewsHeadline"]
    results_count: int
    results_limit: int
    results_offset: int
    status: str
    timestamp: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        headlines = []
        for headlines_item_data in self.headlines:
            headlines_item = headlines_item_data.to_dict()
            headlines.append(headlines_item)

        results_count = self.results_count

        results_limit = self.results_limit

        results_offset = self.results_offset

        status = self.status

        timestamp = self.timestamp.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "headlines": headlines,
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
        from ..models.news_headline import NewsHeadline

        d = src_dict.copy()
        headlines = []
        _headlines = d.pop("headlines")
        for headlines_item_data in _headlines:
            headlines_item = NewsHeadline.from_dict(headlines_item_data)

            headlines.append(headlines_item)

        results_count = d.pop("resultsCount")

        results_limit = d.pop("resultsLimit")

        results_offset = d.pop("resultsOffset")

        status = d.pop("status")

        timestamp = isoparse(d.pop("timestamp"))

        news_response = cls(
            headlines=headlines,
            results_count=results_count,
            results_limit=results_limit,
            results_offset=results_offset,
            status=status,
            timestamp=timestamp,
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
