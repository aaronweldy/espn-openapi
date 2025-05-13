from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.player_stats import PlayerStats


T = TypeVar("T", bound="Player")


@_attrs_define
class Player:
    """
    Attributes:
        id (int): Player ID Example: 3139477.
        full_name (str): Player's full name Example: Patrick Mahomes.
        default_position_id (int): Default position ID Example: 1.
        pro_team_id (int): Pro team ID Example: 12.
        eligible_slots (List[int]): Slots player is eligible for Example: [0, 20, 21].
        first_name (Union[Unset, str]): Player's first name Example: Patrick.
        last_name (Union[Unset, str]): Player's last name Example: Mahomes.
        active (Union[Unset, bool]): Whether player is active Example: True.
        injury_status (Union[Unset, str]): Player injury status Example: ACTIVE.
        stats (Union[Unset, List['PlayerStats']]): Player statistics
    """

    id: int
    full_name: str
    default_position_id: int
    pro_team_id: int
    eligible_slots: List[int]
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    active: Union[Unset, bool] = UNSET
    injury_status: Union[Unset, str] = UNSET
    stats: Union[Unset, List["PlayerStats"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        full_name = self.full_name

        default_position_id = self.default_position_id

        pro_team_id = self.pro_team_id

        eligible_slots = self.eligible_slots

        first_name = self.first_name

        last_name = self.last_name

        active = self.active

        injury_status = self.injury_status

        stats: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = []
            for stats_item_data in self.stats:
                stats_item = stats_item_data.to_dict()
                stats.append(stats_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "fullName": full_name,
                "defaultPositionId": default_position_id,
                "proTeamId": pro_team_id,
                "eligibleSlots": eligible_slots,
            }
        )
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if active is not UNSET:
            field_dict["active"] = active
        if injury_status is not UNSET:
            field_dict["injuryStatus"] = injury_status
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.player_stats import PlayerStats

        d = src_dict.copy()
        id = d.pop("id")

        full_name = d.pop("fullName")

        default_position_id = d.pop("defaultPositionId")

        pro_team_id = d.pop("proTeamId")

        eligible_slots = cast(List[int], d.pop("eligibleSlots"))

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        active = d.pop("active", UNSET)

        injury_status = d.pop("injuryStatus", UNSET)

        stats = []
        _stats = d.pop("stats", UNSET)
        for stats_item_data in _stats or []:
            stats_item = PlayerStats.from_dict(stats_item_data)

            stats.append(stats_item)

        player = cls(
            id=id,
            full_name=full_name,
            default_position_id=default_position_id,
            pro_team_id=pro_team_id,
            eligible_slots=eligible_slots,
            first_name=first_name,
            last_name=last_name,
            active=active,
            injury_status=injury_status,
            stats=stats,
        )

        player.additional_properties = d
        return player

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
