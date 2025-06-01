from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mlb_statistic_name import MlbStatisticName
from ..models.nba_statistic_name import NbaStatisticName
from ..models.nfl_statistic_name import NflStatisticName
from ..models.nhl_statistic_name import NhlStatisticName
from ..models.soccer_statistic_name import SoccerStatisticName
from ..types import UNSET, Unset

T = TypeVar("T", bound="Statistic")


@_attrs_define
class Statistic:
    """
    Attributes:
        name (Union[MlbStatisticName, NbaStatisticName, NflStatisticName, NhlStatisticName, SoccerStatisticName,
            Unset]):
        display_name (Union[Unset, str]):  Example: First Downs.
        short_display_name (Union[Unset, str]):
        display_value (Union[Unset, str]):  Example: 27.
        value (Union[Unset, float]):  Example: 27.
    """

    name: Union[MlbStatisticName, NbaStatisticName, NflStatisticName, NhlStatisticName, SoccerStatisticName, Unset] = (
        UNSET
    )
    display_name: Union[Unset, str] = UNSET
    short_display_name: Union[Unset, str] = UNSET
    display_value: Union[Unset, str] = UNSET
    value: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name: Union[Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        elif isinstance(self.name, NflStatisticName):
            name = self.name.value
        elif isinstance(self.name, MlbStatisticName):
            name = self.name.value
        elif isinstance(self.name, NhlStatisticName):
            name = self.name.value
        elif isinstance(self.name, NbaStatisticName):
            name = self.name.value
        else:
            name = self.name.value

        display_name = self.display_name

        short_display_name = self.short_display_name

        display_value = self.display_value

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if short_display_name is not UNSET:
            field_dict["shortDisplayName"] = short_display_name
        if display_value is not UNSET:
            field_dict["displayValue"] = display_value
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_name(
            data: object,
        ) -> Union[MlbStatisticName, NbaStatisticName, NflStatisticName, NhlStatisticName, SoccerStatisticName, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                name_type_0 = NflStatisticName(data)

                return name_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                name_type_1 = MlbStatisticName(data)

                return name_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                name_type_2 = NhlStatisticName(data)

                return name_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                name_type_3 = NbaStatisticName(data)

                return name_type_3
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            name_type_4 = SoccerStatisticName(data)

            return name_type_4

        name = _parse_name(d.pop("name", UNSET))

        display_name = d.pop("displayName", UNSET)

        short_display_name = d.pop("shortDisplayName", UNSET)

        display_value = d.pop("displayValue", UNSET)

        value = d.pop("value", UNSET)

        statistic = cls(
            name=name,
            display_name=display_name,
            short_display_name=short_display_name,
            display_value=display_value,
            value=value,
        )

        statistic.additional_properties = d
        return statistic

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
