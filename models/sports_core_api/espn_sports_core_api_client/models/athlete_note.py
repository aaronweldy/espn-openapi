import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="AthleteNote")


@_attrs_define
class AthleteNote:
    """Individual note for an athlete

    Attributes:
        id (str): Unique identifier for the note Example: 597206.
        type (str): Type of note (e.g., news) Example: news.
        date (datetime.datetime): Date and time of the note Example: 2025-03-12T15:55Z.
        headline (str): Brief summary of the note Example: Mahomes agreed Wednesday with the Chiefs on a restructure of
            his contract, Adam Teicher of ESPN.com reports..
        text (str): Full text of the note Example: Mahomes and star defensive tackle Chris Jones both agreed to
            restructure their contracts Wednesday....
        source (str): Source of the note Example: RotoWire.
    """

    id: str
    type: str
    date: datetime.datetime
    headline: str
    text: str
    source: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type

        date = self.date.isoformat()

        headline = self.headline

        text = self.text

        source = self.source

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
                "date": date,
                "headline": headline,
                "text": text,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        type = d.pop("type")

        date = isoparse(d.pop("date"))

        headline = d.pop("headline")

        text = d.pop("text")

        source = d.pop("source")

        athlete_note = cls(
            id=id,
            type=type,
            date=date,
            headline=headline,
            text=text,
            source=source,
        )

        athlete_note.additional_properties = d
        return athlete_note

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
