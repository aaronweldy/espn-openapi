from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record import Record


T = TypeVar("T", bound="TeamRecord")


@_attrs_define
class TeamRecord:
    """
    Attributes:
        overall (Record):
        division (Union[Unset, Record]):
        home (Union[Unset, Record]):
        away (Union[Unset, Record]):
    """

    overall: "Record"
    division: Union[Unset, "Record"] = UNSET
    home: Union[Unset, "Record"] = UNSET
    away: Union[Unset, "Record"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        overall = self.overall.to_dict()

        division: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.division, Unset):
            division = self.division.to_dict()

        home: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.home, Unset):
            home = self.home.to_dict()

        away: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.away, Unset):
            away = self.away.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "overall": overall,
            }
        )
        if division is not UNSET:
            field_dict["division"] = division
        if home is not UNSET:
            field_dict["home"] = home
        if away is not UNSET:
            field_dict["away"] = away

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record import Record

        d = src_dict.copy()
        overall = Record.from_dict(d.pop("overall"))

        _division = d.pop("division", UNSET)
        division: Union[Unset, Record]
        if isinstance(_division, Unset):
            division = UNSET
        else:
            division = Record.from_dict(_division)

        _home = d.pop("home", UNSET)
        home: Union[Unset, Record]
        if isinstance(_home, Unset):
            home = UNSET
        else:
            home = Record.from_dict(_home)

        _away = d.pop("away", UNSET)
        away: Union[Unset, Record]
        if isinstance(_away, Unset):
            away = UNSET
        else:
            away = Record.from_dict(_away)

        team_record = cls(
            overall=overall,
            division=division,
            home=home,
            away=away,
        )

        team_record.additional_properties = d
        return team_record

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
