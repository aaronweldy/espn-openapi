from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.search_v2_content_item import SearchV2ContentItem


T = TypeVar("T", bound="SearchV2ResultGroup")


@_attrs_define
class SearchV2ResultGroup:
    """
    Attributes:
        type (str):
        total_found (int):
        page (int):
        limit (int):
        display_name (str):
        contents (List['SearchV2ContentItem']):
    """

    type: str
    total_found: int
    page: int
    limit: int
    display_name: str
    contents: List["SearchV2ContentItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        total_found = self.total_found

        page = self.page

        limit = self.limit

        display_name = self.display_name

        contents = []
        for contents_item_data in self.contents:
            contents_item = contents_item_data.to_dict()
            contents.append(contents_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "totalFound": total_found,
                "page": page,
                "limit": limit,
                "displayName": display_name,
                "contents": contents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.search_v2_content_item import SearchV2ContentItem

        d = src_dict.copy()
        type = d.pop("type")

        total_found = d.pop("totalFound")

        page = d.pop("page")

        limit = d.pop("limit")

        display_name = d.pop("displayName")

        contents = []
        _contents = d.pop("contents")
        for contents_item_data in _contents:
            contents_item = SearchV2ContentItem.from_dict(contents_item_data)

            contents.append(contents_item)

        search_v2_result_group = cls(
            type=type,
            total_found=total_found,
            page=page,
            limit=limit,
            display_name=display_name,
            contents=contents,
        )

        search_v2_result_group.additional_properties = d
        return search_v2_result_group

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
