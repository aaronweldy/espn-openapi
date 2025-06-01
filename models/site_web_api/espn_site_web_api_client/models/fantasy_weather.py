from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fantasy_weather_link import FantasyWeatherLink


T = TypeVar("T", bound="FantasyWeather")


@_attrs_define
class FantasyWeather:
    """
    Attributes:
        display_value (Union[Unset, str]):
        high_temperature (Union[Unset, int]):
        condition_id (Union[Unset, str]):
        link (Union[Unset, FantasyWeatherLink]):
    """

    display_value: Union[Unset, str] = UNSET
    high_temperature: Union[Unset, int] = UNSET
    condition_id: Union[Unset, str] = UNSET
    link: Union[Unset, "FantasyWeatherLink"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_value = self.display_value

        high_temperature = self.high_temperature

        condition_id = self.condition_id

        link: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.link, Unset):
            link = self.link.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_value is not UNSET:
            field_dict["displayValue"] = display_value
        if high_temperature is not UNSET:
            field_dict["highTemperature"] = high_temperature
        if condition_id is not UNSET:
            field_dict["conditionId"] = condition_id
        if link is not UNSET:
            field_dict["link"] = link

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fantasy_weather_link import FantasyWeatherLink

        d = src_dict.copy()
        display_value = d.pop("displayValue", UNSET)

        high_temperature = d.pop("highTemperature", UNSET)

        condition_id = d.pop("conditionId", UNSET)

        _link = d.pop("link", UNSET)
        link: Union[Unset, FantasyWeatherLink]
        if isinstance(_link, Unset):
            link = UNSET
        else:
            link = FantasyWeatherLink.from_dict(_link)

        fantasy_weather = cls(
            display_value=display_value,
            high_temperature=high_temperature,
            condition_id=condition_id,
            link=link,
        )

        fantasy_weather.additional_properties = d
        return fantasy_weather

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
