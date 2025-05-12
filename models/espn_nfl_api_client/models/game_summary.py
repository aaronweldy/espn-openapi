from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.boxscore import Boxscore
    from ..models.drive import Drive
    from ..models.game_format import GameFormat
    from ..models.game_header import GameHeader
    from ..models.game_info import GameInfo
    from ..models.game_summary_standings import GameSummaryStandings
    from ..models.leader import Leader
    from ..models.play import Play


T = TypeVar("T", bound="GameSummary")


@_attrs_define
class GameSummary:
    """
    Attributes:
        header (Union[Unset, GameHeader]):
        game_info (Union[Unset, GameInfo]):
        boxscore (Union[Unset, Boxscore]):
        format_ (Union[Unset, GameFormat]):
        plays (Union[Unset, list['Play']]):
        drives (Union[Unset, list['Drive'], str]):
        leaders (Union[Unset, list['Leader']]):
        standings (Union[Unset, GameSummaryStandings]): Relevant standings information
    """

    header: Union[Unset, "GameHeader"] = UNSET
    game_info: Union[Unset, "GameInfo"] = UNSET
    boxscore: Union[Unset, "Boxscore"] = UNSET
    format_: Union[Unset, "GameFormat"] = UNSET
    plays: Union[Unset, list["Play"]] = UNSET
    drives: Union[Unset, list["Drive"], str] = UNSET
    leaders: Union[Unset, list["Leader"]] = UNSET
    standings: Union[Unset, "GameSummaryStandings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        header: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.header, Unset):
            header = self.header.to_dict()

        game_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.game_info, Unset):
            game_info = self.game_info.to_dict()

        boxscore: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.boxscore, Unset):
            boxscore = self.boxscore.to_dict()

        format_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.to_dict()

        plays: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.plays, Unset):
            plays = []
            for plays_item_data in self.plays:
                plays_item = plays_item_data.to_dict()
                plays.append(plays_item)

        drives: Union[Unset, list[dict[str, Any]], str]
        if isinstance(self.drives, Unset):
            drives = UNSET
        elif isinstance(self.drives, list):
            drives = []
            for drives_type_0_item_data in self.drives:
                drives_type_0_item = drives_type_0_item_data.to_dict()
                drives.append(drives_type_0_item)

        else:
            drives = self.drives

        leaders: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.leaders, Unset):
            leaders = []
            for leaders_item_data in self.leaders:
                leaders_item = leaders_item_data.to_dict()
                leaders.append(leaders_item)

        standings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.standings, Unset):
            standings = self.standings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if header is not UNSET:
            field_dict["header"] = header
        if game_info is not UNSET:
            field_dict["gameInfo"] = game_info
        if boxscore is not UNSET:
            field_dict["boxscore"] = boxscore
        if format_ is not UNSET:
            field_dict["format"] = format_
        if plays is not UNSET:
            field_dict["plays"] = plays
        if drives is not UNSET:
            field_dict["drives"] = drives
        if leaders is not UNSET:
            field_dict["leaders"] = leaders
        if standings is not UNSET:
            field_dict["standings"] = standings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.boxscore import Boxscore
        from ..models.drive import Drive
        from ..models.game_format import GameFormat
        from ..models.game_header import GameHeader
        from ..models.game_info import GameInfo
        from ..models.game_summary_standings import GameSummaryStandings
        from ..models.leader import Leader
        from ..models.play import Play

        d = dict(src_dict)
        _header = d.pop("header", UNSET)
        header: Union[Unset, GameHeader]
        if isinstance(_header, Unset):
            header = UNSET
        else:
            header = GameHeader.from_dict(_header)

        _game_info = d.pop("gameInfo", UNSET)
        game_info: Union[Unset, GameInfo]
        if isinstance(_game_info, Unset):
            game_info = UNSET
        else:
            game_info = GameInfo.from_dict(_game_info)

        _boxscore = d.pop("boxscore", UNSET)
        boxscore: Union[Unset, Boxscore]
        if isinstance(_boxscore, Unset):
            boxscore = UNSET
        else:
            boxscore = Boxscore.from_dict(_boxscore)

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, GameFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = GameFormat.from_dict(_format_)

        plays = []
        _plays = d.pop("plays", UNSET)
        for plays_item_data in _plays or []:
            plays_item = Play.from_dict(plays_item_data)

            plays.append(plays_item)

        def _parse_drives(data: object) -> Union[Unset, list["Drive"], str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                drives_type_0 = []
                _drives_type_0 = data
                for drives_type_0_item_data in _drives_type_0:
                    drives_type_0_item = Drive.from_dict(drives_type_0_item_data)

                    drives_type_0.append(drives_type_0_item)

                return drives_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Unset, list["Drive"], str], data)

        drives = _parse_drives(d.pop("drives", UNSET))

        leaders = []
        _leaders = d.pop("leaders", UNSET)
        for leaders_item_data in _leaders or []:
            leaders_item = Leader.from_dict(leaders_item_data)

            leaders.append(leaders_item)

        _standings = d.pop("standings", UNSET)
        standings: Union[Unset, GameSummaryStandings]
        if isinstance(_standings, Unset):
            standings = UNSET
        else:
            standings = GameSummaryStandings.from_dict(_standings)

        game_summary = cls(
            header=header,
            game_info=game_info,
            boxscore=boxscore,
            format_=format_,
            plays=plays,
            drives=drives,
            leaders=leaders,
            standings=standings,
        )

        game_summary.additional_properties = d
        return game_summary

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
