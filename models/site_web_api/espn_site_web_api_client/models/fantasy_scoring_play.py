from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fantasy_scoring_play_clock import FantasyScoringPlayClock
    from ..models.fantasy_scoring_play_participants_item import FantasyScoringPlayParticipantsItem
    from ..models.fantasy_scoring_play_period import FantasyScoringPlayPeriod
    from ..models.fantasy_scoring_play_scoring_type import FantasyScoringPlayScoringType
    from ..models.fantasy_scoring_play_team import FantasyScoringPlayTeam
    from ..models.fantasy_scoring_play_type import FantasyScoringPlayType


T = TypeVar("T", bound="FantasyScoringPlay")


@_attrs_define
class FantasyScoringPlay:
    """
    Attributes:
        id (Union[Unset, str]):
        type (Union[Unset, FantasyScoringPlayType]):
        text (Union[Unset, str]):
        away_score (Union[Unset, int]):
        home_score (Union[Unset, int]):
        period (Union[Unset, FantasyScoringPlayPeriod]):
        scoring_type (Union[Unset, FantasyScoringPlayScoringType]):
        clock (Union[Unset, FantasyScoringPlayClock]):
        team (Union[Unset, FantasyScoringPlayTeam]):
        participants (Union[Unset, List['FantasyScoringPlayParticipantsItem']]):
    """

    id: Union[Unset, str] = UNSET
    type: Union[Unset, "FantasyScoringPlayType"] = UNSET
    text: Union[Unset, str] = UNSET
    away_score: Union[Unset, int] = UNSET
    home_score: Union[Unset, int] = UNSET
    period: Union[Unset, "FantasyScoringPlayPeriod"] = UNSET
    scoring_type: Union[Unset, "FantasyScoringPlayScoringType"] = UNSET
    clock: Union[Unset, "FantasyScoringPlayClock"] = UNSET
    team: Union[Unset, "FantasyScoringPlayTeam"] = UNSET
    participants: Union[Unset, List["FantasyScoringPlayParticipantsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        text = self.text

        away_score = self.away_score

        home_score = self.home_score

        period: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.to_dict()

        scoring_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.scoring_type, Unset):
            scoring_type = self.scoring_type.to_dict()

        clock: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.clock, Unset):
            clock = self.clock.to_dict()

        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        participants: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.participants, Unset):
            participants = []
            for participants_item_data in self.participants:
                participants_item = participants_item_data.to_dict()
                participants.append(participants_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type
        if text is not UNSET:
            field_dict["text"] = text
        if away_score is not UNSET:
            field_dict["awayScore"] = away_score
        if home_score is not UNSET:
            field_dict["homeScore"] = home_score
        if period is not UNSET:
            field_dict["period"] = period
        if scoring_type is not UNSET:
            field_dict["scoringType"] = scoring_type
        if clock is not UNSET:
            field_dict["clock"] = clock
        if team is not UNSET:
            field_dict["team"] = team
        if participants is not UNSET:
            field_dict["participants"] = participants

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fantasy_scoring_play_clock import FantasyScoringPlayClock
        from ..models.fantasy_scoring_play_participants_item import FantasyScoringPlayParticipantsItem
        from ..models.fantasy_scoring_play_period import FantasyScoringPlayPeriod
        from ..models.fantasy_scoring_play_scoring_type import FantasyScoringPlayScoringType
        from ..models.fantasy_scoring_play_team import FantasyScoringPlayTeam
        from ..models.fantasy_scoring_play_type import FantasyScoringPlayType

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, FantasyScoringPlayType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = FantasyScoringPlayType.from_dict(_type)

        text = d.pop("text", UNSET)

        away_score = d.pop("awayScore", UNSET)

        home_score = d.pop("homeScore", UNSET)

        _period = d.pop("period", UNSET)
        period: Union[Unset, FantasyScoringPlayPeriod]
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = FantasyScoringPlayPeriod.from_dict(_period)

        _scoring_type = d.pop("scoringType", UNSET)
        scoring_type: Union[Unset, FantasyScoringPlayScoringType]
        if isinstance(_scoring_type, Unset):
            scoring_type = UNSET
        else:
            scoring_type = FantasyScoringPlayScoringType.from_dict(_scoring_type)

        _clock = d.pop("clock", UNSET)
        clock: Union[Unset, FantasyScoringPlayClock]
        if isinstance(_clock, Unset):
            clock = UNSET
        else:
            clock = FantasyScoringPlayClock.from_dict(_clock)

        _team = d.pop("team", UNSET)
        team: Union[Unset, FantasyScoringPlayTeam]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = FantasyScoringPlayTeam.from_dict(_team)

        participants = []
        _participants = d.pop("participants", UNSET)
        for participants_item_data in _participants or []:
            participants_item = FantasyScoringPlayParticipantsItem.from_dict(participants_item_data)

            participants.append(participants_item)

        fantasy_scoring_play = cls(
            id=id,
            type=type,
            text=text,
            away_score=away_score,
            home_score=home_score,
            period=period,
            scoring_type=scoring_type,
            clock=clock,
            team=team,
            participants=participants,
        )

        fantasy_scoring_play.additional_properties = d
        return fantasy_scoring_play

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
