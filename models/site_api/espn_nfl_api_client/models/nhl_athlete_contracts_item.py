from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nhl_athlete_contracts_item_season import NhlAthleteContractsItemSeason


T = TypeVar("T", bound="NhlAthleteContractsItem")


@_attrs_define
class NhlAthleteContractsItem:
    """
    Attributes:
        salary (Union[Unset, int]):
        season (Union[Unset, NhlAthleteContractsItemSeason]):
    """

    salary: Union[Unset, int] = UNSET
    season: Union[Unset, "NhlAthleteContractsItemSeason"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        salary = self.salary

        season: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if salary is not UNSET:
            field_dict["salary"] = salary
        if season is not UNSET:
            field_dict["season"] = season

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nhl_athlete_contracts_item_season import NhlAthleteContractsItemSeason

        d = src_dict.copy()
        salary = d.pop("salary", UNSET)

        _season = d.pop("season", UNSET)
        season: Union[Unset, NhlAthleteContractsItemSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = NhlAthleteContractsItemSeason.from_dict(_season)

        nhl_athlete_contracts_item = cls(
            salary=salary,
            season=season,
        )

        nhl_athlete_contracts_item.additional_properties = d
        return nhl_athlete_contracts_item

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
