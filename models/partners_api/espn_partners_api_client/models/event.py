import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.competition import Competition


T = TypeVar("T", bound="Event")


@_attrs_define
class Event:
    """
    Attributes:
        id (str): Unique event identifier Example: 401772510.
        date (datetime.datetime): Event date and time Example: 2025-09-05T00:20Z.
        name (str): Full event name Example: Dallas Cowboys at Philadelphia Eagles.
        short_name (str): Short event name Example: DAL @ PHI.
        competitions (List['Competition']):
        time_valid (Union[Unset, bool]): Whether the time is confirmed Example: True.
    """

    id: str
    date: datetime.datetime
    name: str
    short_name: str
    competitions: List["Competition"]
    time_valid: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        date = self.date.isoformat()

        name = self.name

        short_name = self.short_name

        competitions = []
        for competitions_item_data in self.competitions:
            competitions_item = competitions_item_data.to_dict()
            competitions.append(competitions_item)

        time_valid = self.time_valid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "date": date,
                "name": name,
                "shortName": short_name,
                "competitions": competitions,
            }
        )
        if time_valid is not UNSET:
            field_dict["timeValid"] = time_valid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.competition import Competition

        d = src_dict.copy()
        id = d.pop("id")

        date = isoparse(d.pop("date"))

        name = d.pop("name")

        short_name = d.pop("shortName")

        competitions = []
        _competitions = d.pop("competitions")
        for competitions_item_data in _competitions:
            competitions_item = Competition.from_dict(competitions_item_data)

            competitions.append(competitions_item)

        time_valid = d.pop("timeValid", UNSET)

        event = cls(
            id=id,
            date=date,
            name=name,
            short_name=short_name,
            competitions=competitions,
            time_valid=time_valid,
        )

        event.additional_properties = d
        return event

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
