from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fantasy_season_response_settings import FantasySeasonResponseSettings


T = TypeVar("T", bound="FantasySeasonResponse")


@_attrs_define
class FantasySeasonResponse:
    """
    Attributes:
        display (Union[Unset, bool]): Whether to display the data
        settings (Union[Unset, FantasySeasonResponseSettings]):
    """

    display: Union[Unset, bool] = UNSET
    settings: Union[Unset, "FantasySeasonResponseSettings"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display = self.display

        settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display is not UNSET:
            field_dict["display"] = display
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fantasy_season_response_settings import FantasySeasonResponseSettings

        d = src_dict.copy()
        display = d.pop("display", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, FantasySeasonResponseSettings]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = FantasySeasonResponseSettings.from_dict(_settings)

        fantasy_season_response = cls(
            display=display,
            settings=settings,
        )

        fantasy_season_response.additional_properties = d
        return fantasy_season_response

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
