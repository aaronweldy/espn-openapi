from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.official import Official
    from ..models.venue import Venue
    from ..models.weather import Weather


T = TypeVar("T", bound="GameInfo")


@_attrs_define
class GameInfo:
    """
    Attributes:
        venue (Union[Unset, Venue]):
        officials (Union[Unset, list['Official']]):
        attendance (Union[Unset, int]):
        weather (Union[Unset, Weather]):
    """

    venue: Union[Unset, "Venue"] = UNSET
    officials: Union[Unset, list["Official"]] = UNSET
    attendance: Union[Unset, int] = UNSET
    weather: Union[Unset, "Weather"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        venue: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.venue, Unset):
            venue = self.venue.to_dict()

        officials: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.officials, Unset):
            officials = []
            for officials_item_data in self.officials:
                officials_item = officials_item_data.to_dict()
                officials.append(officials_item)

        attendance = self.attendance

        weather: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.weather, Unset):
            weather = self.weather.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if venue is not UNSET:
            field_dict["venue"] = venue
        if officials is not UNSET:
            field_dict["officials"] = officials
        if attendance is not UNSET:
            field_dict["attendance"] = attendance
        if weather is not UNSET:
            field_dict["weather"] = weather

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.official import Official
        from ..models.venue import Venue
        from ..models.weather import Weather

        d = dict(src_dict)
        _venue = d.pop("venue", UNSET)
        venue: Union[Unset, Venue]
        if isinstance(_venue, Unset):
            venue = UNSET
        else:
            venue = Venue.from_dict(_venue)

        officials = []
        _officials = d.pop("officials", UNSET)
        for officials_item_data in _officials or []:
            officials_item = Official.from_dict(officials_item_data)

            officials.append(officials_item)

        attendance = d.pop("attendance", UNSET)

        _weather = d.pop("weather", UNSET)
        weather: Union[Unset, Weather]
        if isinstance(_weather, Unset):
            weather = UNSET
        else:
            weather = Weather.from_dict(_weather)

        game_info = cls(
            venue=venue,
            officials=officials,
            attendance=attendance,
            weather=weather,
        )

        game_info.additional_properties = d
        return game_info

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
