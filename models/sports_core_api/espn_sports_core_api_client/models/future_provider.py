from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.betting_provider import BettingProvider
    from ..models.future_book import FutureBook


T = TypeVar("T", bound="FutureProvider")


@_attrs_define
class FutureProvider:
    """
    Attributes:
        provider (BettingProvider):
        books (List['FutureBook']):
    """

    provider: "BettingProvider"
    books: List["FutureBook"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        provider = self.provider.to_dict()

        books = []
        for books_item_data in self.books:
            books_item = books_item_data.to_dict()
            books.append(books_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "books": books,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.betting_provider import BettingProvider
        from ..models.future_book import FutureBook

        d = src_dict.copy()
        provider = BettingProvider.from_dict(d.pop("provider"))

        books = []
        _books = d.pop("books")
        for books_item_data in _books:
            books_item = FutureBook.from_dict(books_item_data)

            books.append(books_item)

        future_provider = cls(
            provider=provider,
            books=books,
        )

        future_provider.additional_properties = d
        return future_provider

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
