import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AthleteNote")


@_attrs_define
class AthleteNote:
    """Individual note for an athlete

    Attributes:
        id (str): Unique identifier for the note Example: 597206.
        type (str): Type of note (e.g., news) Example: news.
        date (datetime.datetime): Date and time of the note Example: 2025-03-12T15:55Z.
        headline (Union[Unset, str]): Brief summary of the note (may be omitted by API).
        text (Union[Unset, str]): Full text of the note (may be omitted by API).
        source (str): Source of the note Example: RotoWire.
    """

    id: str
    type: str
    date: datetime.datetime
    source: str
    headline: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type = self.type

        date = self.date.isoformat()

        headline: Union[Unset, str]
        if isinstance(self.headline, Unset):
            headline = UNSET
        else:
            headline = self.headline

        text: Union[Unset, str]
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
                "date": date,
                "source": source,
            }
        )
        if headline is not UNSET:
            field_dict["headline"] = headline
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        type = d.pop("type")

        date = isoparse(d.pop("date"))

        headline = d.pop("headline", UNSET)

        text = d.pop("text", UNSET)

        source = d.pop("source")

        athlete_note = cls(
            id=id,
            type=type,
            date=date,
            source=source,
            headline=headline,
            text=text,
        )

        athlete_note.additional_properties = d
        return athlete_note

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
