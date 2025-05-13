import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.position_group import PositionGroup
    from ..models.season import Season


T = TypeVar("T", bound="TeamRosterResponse")


@_attrs_define
class TeamRosterResponse:
    """The response for a team roster request

    Attributes:
        timestamp (Union[Unset, datetime.datetime]): The timestamp of when the data was generated
        status (Union[Unset, str]): The status of the response
        season (Union[Unset, Season]):
        athletes (Union[Unset, List['PositionGroup']]): List of roster position groups
    """

    timestamp: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, str] = UNSET
    season: Union[Unset, "Season"] = UNSET
    athletes: Union[Unset, List["PositionGroup"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        status = self.status

        season: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        athletes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.athletes, Unset):
            athletes = []
            for athletes_item_data in self.athletes:
                athletes_item = athletes_item_data.to_dict()
                athletes.append(athletes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if status is not UNSET:
            field_dict["status"] = status
        if season is not UNSET:
            field_dict["season"] = season
        if athletes is not UNSET:
            field_dict["athletes"] = athletes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.position_group import PositionGroup
        from ..models.season import Season

        d = src_dict.copy()
        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        status = d.pop("status", UNSET)

        _season = d.pop("season", UNSET)
        season: Union[Unset, Season]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = Season.from_dict(_season)

        athletes = []
        _athletes = d.pop("athletes", UNSET)
        for athletes_item_data in _athletes or []:
            athletes_item = PositionGroup.from_dict(athletes_item_data)

            athletes.append(athletes_item)

        team_roster_response = cls(
            timestamp=timestamp,
            status=status,
            season=season,
            athletes=athletes,
        )

        team_roster_response.additional_properties = d
        return team_roster_response

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
