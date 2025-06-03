from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fantasy_player_draft_ranks_by_rank_type import FantasyPlayerDraftRanksByRankType
    from ..models.fantasy_player_stats import FantasyPlayerStats
    from ..models.player_ownership import PlayerOwnership


T = TypeVar("T", bound="FantasyPlayer")


@_attrs_define
class FantasyPlayer:
    """
    Attributes:
        active (Union[Unset, bool]): Whether the player is currently active
        default_position_id (Union[Unset, int]): The player's default position ID
        draft_ranks_by_rank_type (Union[Unset, FantasyPlayerDraftRanksByRankType]): Draft rankings by type (STANDARD,
            PPR, etc.)
        droppable (Union[Unset, bool]): Whether the player can be dropped
        eligible_slots (Union[Unset, List[int]]): Position slots the player is eligible for
        first_name (Union[Unset, str]): Player's first name
        full_name (Union[Unset, str]): Player's full name
        id (Union[Unset, int]): Player's unique ID
        injured (Union[Unset, bool]): Whether the player is injured
        injury_status (Union[Unset, str]): Current injury status (ACTIVE, QUESTIONABLE, OUT, etc.)
        jersey (Union[Unset, str]): Jersey number
        last_name (Union[Unset, str]): Player's last name
        ownership (Union[Unset, PlayerOwnership]):
        pro_team_id (Union[Unset, int]): Professional team ID
        stats (Union[Unset, List['FantasyPlayerStats']]): Player statistics
    """

    active: Union[Unset, bool] = UNSET
    default_position_id: Union[Unset, int] = UNSET
    draft_ranks_by_rank_type: Union[Unset, "FantasyPlayerDraftRanksByRankType"] = UNSET
    droppable: Union[Unset, bool] = UNSET
    eligible_slots: Union[Unset, List[int]] = UNSET
    first_name: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    injured: Union[Unset, bool] = UNSET
    injury_status: Union[Unset, str] = UNSET
    jersey: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    ownership: Union[Unset, "PlayerOwnership"] = UNSET
    pro_team_id: Union[Unset, int] = UNSET
    stats: Union[Unset, List["FantasyPlayerStats"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active = self.active

        default_position_id = self.default_position_id

        draft_ranks_by_rank_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.draft_ranks_by_rank_type, Unset):
            draft_ranks_by_rank_type = self.draft_ranks_by_rank_type.to_dict()

        droppable = self.droppable

        eligible_slots: Union[Unset, List[int]] = UNSET
        if not isinstance(self.eligible_slots, Unset):
            eligible_slots = self.eligible_slots

        first_name = self.first_name

        full_name = self.full_name

        id = self.id

        injured = self.injured

        injury_status = self.injury_status

        jersey = self.jersey

        last_name = self.last_name

        ownership: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ownership, Unset):
            ownership = self.ownership.to_dict()

        pro_team_id = self.pro_team_id

        stats: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = []
            for stats_item_data in self.stats:
                stats_item = stats_item_data.to_dict()
                stats.append(stats_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if default_position_id is not UNSET:
            field_dict["defaultPositionId"] = default_position_id
        if draft_ranks_by_rank_type is not UNSET:
            field_dict["draftRanksByRankType"] = draft_ranks_by_rank_type
        if droppable is not UNSET:
            field_dict["droppable"] = droppable
        if eligible_slots is not UNSET:
            field_dict["eligibleSlots"] = eligible_slots
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if id is not UNSET:
            field_dict["id"] = id
        if injured is not UNSET:
            field_dict["injured"] = injured
        if injury_status is not UNSET:
            field_dict["injuryStatus"] = injury_status
        if jersey is not UNSET:
            field_dict["jersey"] = jersey
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if ownership is not UNSET:
            field_dict["ownership"] = ownership
        if pro_team_id is not UNSET:
            field_dict["proTeamId"] = pro_team_id
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fantasy_player_draft_ranks_by_rank_type import FantasyPlayerDraftRanksByRankType
        from ..models.fantasy_player_stats import FantasyPlayerStats
        from ..models.player_ownership import PlayerOwnership

        d = src_dict.copy()
        active = d.pop("active", UNSET)

        default_position_id = d.pop("defaultPositionId", UNSET)

        _draft_ranks_by_rank_type = d.pop("draftRanksByRankType", UNSET)
        draft_ranks_by_rank_type: Union[Unset, FantasyPlayerDraftRanksByRankType]
        if isinstance(_draft_ranks_by_rank_type, Unset):
            draft_ranks_by_rank_type = UNSET
        else:
            draft_ranks_by_rank_type = FantasyPlayerDraftRanksByRankType.from_dict(_draft_ranks_by_rank_type)

        droppable = d.pop("droppable", UNSET)

        eligible_slots = cast(List[int], d.pop("eligibleSlots", UNSET))

        first_name = d.pop("firstName", UNSET)

        full_name = d.pop("fullName", UNSET)

        id = d.pop("id", UNSET)

        injured = d.pop("injured", UNSET)

        injury_status = d.pop("injuryStatus", UNSET)

        jersey = d.pop("jersey", UNSET)

        last_name = d.pop("lastName", UNSET)

        _ownership = d.pop("ownership", UNSET)
        ownership: Union[Unset, PlayerOwnership]
        if isinstance(_ownership, Unset):
            ownership = UNSET
        else:
            ownership = PlayerOwnership.from_dict(_ownership)

        pro_team_id = d.pop("proTeamId", UNSET)

        stats = []
        _stats = d.pop("stats", UNSET)
        for stats_item_data in _stats or []:
            stats_item = FantasyPlayerStats.from_dict(stats_item_data)

            stats.append(stats_item)

        fantasy_player = cls(
            active=active,
            default_position_id=default_position_id,
            draft_ranks_by_rank_type=draft_ranks_by_rank_type,
            droppable=droppable,
            eligible_slots=eligible_slots,
            first_name=first_name,
            full_name=full_name,
            id=id,
            injured=injured,
            injury_status=injury_status,
            jersey=jersey,
            last_name=last_name,
            ownership=ownership,
            pro_team_id=pro_team_id,
            stats=stats,
        )

        fantasy_player.additional_properties = d
        return fantasy_player

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
