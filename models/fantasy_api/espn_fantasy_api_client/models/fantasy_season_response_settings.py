from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fantasy_season_response_settings_game_notification_settings import (
        FantasySeasonResponseSettingsGameNotificationSettings,
    )
    from ..models.fantasy_season_response_settings_player_ownership_settings import (
        FantasySeasonResponseSettingsPlayerOwnershipSettings,
    )
    from ..models.fantasy_season_response_settings_stat_id_to_override_position import (
        FantasySeasonResponseSettingsStatIdToOverridePosition,
    )
    from ..models.fantasy_season_response_settings_type_names import FantasySeasonResponseSettingsTypeNames
    from ..models.pro_team import ProTeam


T = TypeVar("T", bound="FantasySeasonResponseSettings")


@_attrs_define
class FantasySeasonResponseSettings:
    """
    Attributes:
        default_draft_position (Union[None, Unset, int]):
        draft_lobby_minimum_league_count (Union[Unset, int]):
        game_notification_settings (Union[Unset, FantasySeasonResponseSettingsGameNotificationSettings]):
        gated (Union[Unset, bool]):
        player_ownership_settings (Union[Unset, FantasySeasonResponseSettingsPlayerOwnershipSettings]):
        pro_teams (Union[Unset, List['ProTeam']]):
        read_only (Union[Unset, bool]):
        stat_id_to_override_position (Union[Unset, FantasySeasonResponseSettingsStatIdToOverridePosition]):
        team_activity_enabled (Union[Unset, bool]):
        type_names (Union[Unset, FantasySeasonResponseSettingsTypeNames]):
    """

    default_draft_position: Union[None, Unset, int] = UNSET
    draft_lobby_minimum_league_count: Union[Unset, int] = UNSET
    game_notification_settings: Union[Unset, "FantasySeasonResponseSettingsGameNotificationSettings"] = UNSET
    gated: Union[Unset, bool] = UNSET
    player_ownership_settings: Union[Unset, "FantasySeasonResponseSettingsPlayerOwnershipSettings"] = UNSET
    pro_teams: Union[Unset, List["ProTeam"]] = UNSET
    read_only: Union[Unset, bool] = UNSET
    stat_id_to_override_position: Union[Unset, "FantasySeasonResponseSettingsStatIdToOverridePosition"] = UNSET
    team_activity_enabled: Union[Unset, bool] = UNSET
    type_names: Union[Unset, "FantasySeasonResponseSettingsTypeNames"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        default_draft_position: Union[None, Unset, int]
        if isinstance(self.default_draft_position, Unset):
            default_draft_position = UNSET
        else:
            default_draft_position = self.default_draft_position

        draft_lobby_minimum_league_count = self.draft_lobby_minimum_league_count

        game_notification_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.game_notification_settings, Unset):
            game_notification_settings = self.game_notification_settings.to_dict()

        gated = self.gated

        player_ownership_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.player_ownership_settings, Unset):
            player_ownership_settings = self.player_ownership_settings.to_dict()

        pro_teams: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pro_teams, Unset):
            pro_teams = []
            for pro_teams_item_data in self.pro_teams:
                pro_teams_item = pro_teams_item_data.to_dict()
                pro_teams.append(pro_teams_item)

        read_only = self.read_only

        stat_id_to_override_position: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stat_id_to_override_position, Unset):
            stat_id_to_override_position = self.stat_id_to_override_position.to_dict()

        team_activity_enabled = self.team_activity_enabled

        type_names: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type_names, Unset):
            type_names = self.type_names.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_draft_position is not UNSET:
            field_dict["defaultDraftPosition"] = default_draft_position
        if draft_lobby_minimum_league_count is not UNSET:
            field_dict["draftLobbyMinimumLeagueCount"] = draft_lobby_minimum_league_count
        if game_notification_settings is not UNSET:
            field_dict["gameNotificationSettings"] = game_notification_settings
        if gated is not UNSET:
            field_dict["gated"] = gated
        if player_ownership_settings is not UNSET:
            field_dict["playerOwnershipSettings"] = player_ownership_settings
        if pro_teams is not UNSET:
            field_dict["proTeams"] = pro_teams
        if read_only is not UNSET:
            field_dict["readOnly"] = read_only
        if stat_id_to_override_position is not UNSET:
            field_dict["statIdToOverridePosition"] = stat_id_to_override_position
        if team_activity_enabled is not UNSET:
            field_dict["teamActivityEnabled"] = team_activity_enabled
        if type_names is not UNSET:
            field_dict["typeNames"] = type_names

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fantasy_season_response_settings_game_notification_settings import (
            FantasySeasonResponseSettingsGameNotificationSettings,
        )
        from ..models.fantasy_season_response_settings_player_ownership_settings import (
            FantasySeasonResponseSettingsPlayerOwnershipSettings,
        )
        from ..models.fantasy_season_response_settings_stat_id_to_override_position import (
            FantasySeasonResponseSettingsStatIdToOverridePosition,
        )
        from ..models.fantasy_season_response_settings_type_names import FantasySeasonResponseSettingsTypeNames
        from ..models.pro_team import ProTeam

        d = src_dict.copy()

        def _parse_default_draft_position(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        default_draft_position = _parse_default_draft_position(d.pop("defaultDraftPosition", UNSET))

        draft_lobby_minimum_league_count = d.pop("draftLobbyMinimumLeagueCount", UNSET)

        _game_notification_settings = d.pop("gameNotificationSettings", UNSET)
        game_notification_settings: Union[Unset, FantasySeasonResponseSettingsGameNotificationSettings]
        if isinstance(_game_notification_settings, Unset):
            game_notification_settings = UNSET
        else:
            game_notification_settings = FantasySeasonResponseSettingsGameNotificationSettings.from_dict(
                _game_notification_settings
            )

        gated = d.pop("gated", UNSET)

        _player_ownership_settings = d.pop("playerOwnershipSettings", UNSET)
        player_ownership_settings: Union[Unset, FantasySeasonResponseSettingsPlayerOwnershipSettings]
        if isinstance(_player_ownership_settings, Unset):
            player_ownership_settings = UNSET
        else:
            player_ownership_settings = FantasySeasonResponseSettingsPlayerOwnershipSettings.from_dict(
                _player_ownership_settings
            )

        pro_teams = []
        _pro_teams = d.pop("proTeams", UNSET)
        for pro_teams_item_data in _pro_teams or []:
            pro_teams_item = ProTeam.from_dict(pro_teams_item_data)

            pro_teams.append(pro_teams_item)

        read_only = d.pop("readOnly", UNSET)

        _stat_id_to_override_position = d.pop("statIdToOverridePosition", UNSET)
        stat_id_to_override_position: Union[Unset, FantasySeasonResponseSettingsStatIdToOverridePosition]
        if isinstance(_stat_id_to_override_position, Unset):
            stat_id_to_override_position = UNSET
        else:
            stat_id_to_override_position = FantasySeasonResponseSettingsStatIdToOverridePosition.from_dict(
                _stat_id_to_override_position
            )

        team_activity_enabled = d.pop("teamActivityEnabled", UNSET)

        _type_names = d.pop("typeNames", UNSET)
        type_names: Union[Unset, FantasySeasonResponseSettingsTypeNames]
        if isinstance(_type_names, Unset):
            type_names = UNSET
        else:
            type_names = FantasySeasonResponseSettingsTypeNames.from_dict(_type_names)

        fantasy_season_response_settings = cls(
            default_draft_position=default_draft_position,
            draft_lobby_minimum_league_count=draft_lobby_minimum_league_count,
            game_notification_settings=game_notification_settings,
            gated=gated,
            player_ownership_settings=player_ownership_settings,
            pro_teams=pro_teams,
            read_only=read_only,
            stat_id_to_override_position=stat_id_to_override_position,
            team_activity_enabled=team_activity_enabled,
            type_names=type_names,
        )

        fantasy_season_response_settings.additional_properties = d
        return fantasy_season_response_settings

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
