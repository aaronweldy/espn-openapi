from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fantasy_athlete import FantasyAthlete
    from ..models.fantasy_probable_statistics_item import FantasyProbableStatisticsItem
    from ..models.fantasy_probable_status import FantasyProbableStatus


T = TypeVar("T", bound="FantasyProbable")


@_attrs_define
class FantasyProbable:
    """
    Attributes:
        name (Union[Unset, str]):
        display_name (Union[Unset, str]):
        abbreviation (Union[Unset, str]):
        player_id (Union[Unset, int]):
        athlete (Union[Unset, FantasyAthlete]):
        status (Union[Unset, FantasyProbableStatus]):
        statistics (Union[Unset, List['FantasyProbableStatisticsItem']]):
    """

    name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    player_id: Union[Unset, int] = UNSET
    athlete: Union[Unset, "FantasyAthlete"] = UNSET
    status: Union[Unset, "FantasyProbableStatus"] = UNSET
    statistics: Union[Unset, List["FantasyProbableStatisticsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        display_name = self.display_name

        abbreviation = self.abbreviation

        player_id = self.player_id

        athlete: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.athlete, Unset):
            athlete = self.athlete.to_dict()

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        statistics: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = []
            for statistics_item_data in self.statistics:
                statistics_item = statistics_item_data.to_dict()
                statistics.append(statistics_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if player_id is not UNSET:
            field_dict["playerId"] = player_id
        if athlete is not UNSET:
            field_dict["athlete"] = athlete
        if status is not UNSET:
            field_dict["status"] = status
        if statistics is not UNSET:
            field_dict["statistics"] = statistics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fantasy_athlete import FantasyAthlete
        from ..models.fantasy_probable_statistics_item import FantasyProbableStatisticsItem
        from ..models.fantasy_probable_status import FantasyProbableStatus

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        player_id = d.pop("playerId", UNSET)

        _athlete = d.pop("athlete", UNSET)
        athlete: Union[Unset, FantasyAthlete]
        if isinstance(_athlete, Unset):
            athlete = UNSET
        else:
            athlete = FantasyAthlete.from_dict(_athlete)

        _status = d.pop("status", UNSET)
        status: Union[Unset, FantasyProbableStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = FantasyProbableStatus.from_dict(_status)

        statistics = []
        _statistics = d.pop("statistics", UNSET)
        for statistics_item_data in _statistics or []:
            statistics_item = FantasyProbableStatisticsItem.from_dict(statistics_item_data)

            statistics.append(statistics_item)

        fantasy_probable = cls(
            name=name,
            display_name=display_name,
            abbreviation=abbreviation,
            player_id=player_id,
            athlete=athlete,
            status=status,
            statistics=statistics,
        )

        fantasy_probable.additional_properties = d
        return fantasy_probable

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
