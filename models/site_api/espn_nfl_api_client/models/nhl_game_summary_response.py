from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nhl_game_summary_response_boxscore import NhlGameSummaryResponseBoxscore
    from ..models.nhl_game_summary_response_game_info import NhlGameSummaryResponseGameInfo
    from ..models.nhl_game_summary_response_header import NhlGameSummaryResponseHeader
    from ..models.nhl_game_summary_response_plays_item import NhlGameSummaryResponsePlaysItem
    from ..models.nhl_game_summary_response_standings import NhlGameSummaryResponseStandings
    from ..models.nhl_game_summary_response_win_probability_item import NhlGameSummaryResponseWinProbabilityItem


T = TypeVar("T", bound="NhlGameSummaryResponse")


@_attrs_define
class NhlGameSummaryResponse:
    """NHL game summary response with comprehensive game data

    Attributes:
        boxscore (NhlGameSummaryResponseBoxscore): Game boxscore data
        game_info (NhlGameSummaryResponseGameInfo): Game information including venue and officials
        header (NhlGameSummaryResponseHeader): Game header information
        plays (Union[Unset, List['NhlGameSummaryResponsePlaysItem']]): Game plays data
        win_probability (Union[Unset, List['NhlGameSummaryResponseWinProbabilityItem']]): Win probability data
        standings (Union[Unset, NhlGameSummaryResponseStandings]): Standings information
    """

    boxscore: "NhlGameSummaryResponseBoxscore"
    game_info: "NhlGameSummaryResponseGameInfo"
    header: "NhlGameSummaryResponseHeader"
    plays: Union[Unset, List["NhlGameSummaryResponsePlaysItem"]] = UNSET
    win_probability: Union[Unset, List["NhlGameSummaryResponseWinProbabilityItem"]] = UNSET
    standings: Union[Unset, "NhlGameSummaryResponseStandings"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        boxscore = self.boxscore.to_dict()

        game_info = self.game_info.to_dict()

        header = self.header.to_dict()

        plays: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.plays, Unset):
            plays = []
            for plays_item_data in self.plays:
                plays_item = plays_item_data.to_dict()
                plays.append(plays_item)

        win_probability: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.win_probability, Unset):
            win_probability = []
            for win_probability_item_data in self.win_probability:
                win_probability_item = win_probability_item_data.to_dict()
                win_probability.append(win_probability_item)

        standings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.standings, Unset):
            standings = self.standings.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "boxscore": boxscore,
                "gameInfo": game_info,
                "header": header,
            }
        )
        if plays is not UNSET:
            field_dict["plays"] = plays
        if win_probability is not UNSET:
            field_dict["winProbability"] = win_probability
        if standings is not UNSET:
            field_dict["standings"] = standings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nhl_game_summary_response_boxscore import NhlGameSummaryResponseBoxscore
        from ..models.nhl_game_summary_response_game_info import NhlGameSummaryResponseGameInfo
        from ..models.nhl_game_summary_response_header import NhlGameSummaryResponseHeader
        from ..models.nhl_game_summary_response_plays_item import NhlGameSummaryResponsePlaysItem
        from ..models.nhl_game_summary_response_standings import NhlGameSummaryResponseStandings
        from ..models.nhl_game_summary_response_win_probability_item import NhlGameSummaryResponseWinProbabilityItem

        d = src_dict.copy()
        boxscore = NhlGameSummaryResponseBoxscore.from_dict(d.pop("boxscore"))

        game_info = NhlGameSummaryResponseGameInfo.from_dict(d.pop("gameInfo"))

        header = NhlGameSummaryResponseHeader.from_dict(d.pop("header"))

        plays = []
        _plays = d.pop("plays", UNSET)
        for plays_item_data in _plays or []:
            plays_item = NhlGameSummaryResponsePlaysItem.from_dict(plays_item_data)

            plays.append(plays_item)

        win_probability = []
        _win_probability = d.pop("winProbability", UNSET)
        for win_probability_item_data in _win_probability or []:
            win_probability_item = NhlGameSummaryResponseWinProbabilityItem.from_dict(win_probability_item_data)

            win_probability.append(win_probability_item)

        _standings = d.pop("standings", UNSET)
        standings: Union[Unset, NhlGameSummaryResponseStandings]
        if isinstance(_standings, Unset):
            standings = UNSET
        else:
            standings = NhlGameSummaryResponseStandings.from_dict(_standings)

        nhl_game_summary_response = cls(
            boxscore=boxscore,
            game_info=game_info,
            header=header,
            plays=plays,
            win_probability=win_probability,
            standings=standings,
        )

        nhl_game_summary_response.additional_properties = d
        return nhl_game_summary_response

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
