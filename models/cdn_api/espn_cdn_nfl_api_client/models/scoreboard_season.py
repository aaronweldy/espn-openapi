from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scoreboard_season_type import ScoreboardSeasonType


T = TypeVar("T", bound="ScoreboardSeason")


@_attrs_define
class ScoreboardSeason:
    """
    Attributes:
        year (Union[Unset, int]):
        end_date (Union[Unset, str]):
        display_name (Union[Unset, str]):
        type (Union['ScoreboardSeasonType', Unset, int]):
        start_date (Union[Unset, str]):
    """

    year: Union[Unset, int] = UNSET
    end_date: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    type: Union["ScoreboardSeasonType", Unset, int] = UNSET
    start_date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.scoreboard_season_type import ScoreboardSeasonType

        year = self.year

        end_date = self.end_date

        display_name = self.display_name

        type: Union[Dict[str, Any], Unset, int]
        if isinstance(self.type, Unset):
            type = UNSET
        elif isinstance(self.type, ScoreboardSeasonType):
            type = self.type.to_dict()
        else:
            type = self.type

        start_date = self.start_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if year is not UNSET:
            field_dict["year"] = year
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if type is not UNSET:
            field_dict["type"] = type
        if start_date is not UNSET:
            field_dict["startDate"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scoreboard_season_type import ScoreboardSeasonType

        d = src_dict.copy()
        year = d.pop("year", UNSET)

        end_date = d.pop("endDate", UNSET)

        display_name = d.pop("displayName", UNSET)

        def _parse_type(data: object) -> Union["ScoreboardSeasonType", Unset, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                type_type_0 = ScoreboardSeasonType.from_dict(data)

                return type_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ScoreboardSeasonType", Unset, int], data)

        type = _parse_type(d.pop("type", UNSET))

        start_date = d.pop("startDate", UNSET)

        scoreboard_season = cls(
            year=year,
            end_date=end_date,
            display_name=display_name,
            type=type,
            start_date=start_date,
        )

        scoreboard_season.additional_properties = d
        return scoreboard_season

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
