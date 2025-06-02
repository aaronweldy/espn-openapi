from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.athlete import Athlete


T = TypeVar("T", bound="AthletesListResponse")


@_attrs_define
class AthletesListResponse:
    """
    Attributes:
        athletes (List['Athlete']):
        count (int): Total number of athletes available Example: 6737.
        page_index (int): Current page index (1-based) Example: 1.
        page_size (int): Number of items per page Example: 100.
        page_count (int): Total number of pages Example: 68.
    """

    athletes: List["Athlete"]
    count: int
    page_index: int
    page_size: int
    page_count: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        athletes = []
        for athletes_item_data in self.athletes:
            athletes_item = athletes_item_data.to_dict()
            athletes.append(athletes_item)

        count = self.count

        page_index = self.page_index

        page_size = self.page_size

        page_count = self.page_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "athletes": athletes,
                "count": count,
                "pageIndex": page_index,
                "pageSize": page_size,
                "pageCount": page_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.athlete import Athlete

        d = src_dict.copy()
        athletes = []
        _athletes = d.pop("athletes")
        for athletes_item_data in _athletes:
            athletes_item = Athlete.from_dict(athletes_item_data)

            athletes.append(athletes_item)

        count = d.pop("count")

        page_index = d.pop("pageIndex")

        page_size = d.pop("pageSize")

        page_count = d.pop("pageCount")

        athletes_list_response = cls(
            athletes=athletes,
            count=count,
            page_index=page_index,
            page_size=page_size,
            page_count=page_count,
        )

        athletes_list_response.additional_properties = d
        return athletes_list_response

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
