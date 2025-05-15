import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.drive import Drive
    from ..models.play_clock import PlayClock
    from ..models.play_field_position import PlayFieldPosition
    from ..models.play_participant import PlayParticipant
    from ..models.play_period import PlayPeriod
    from ..models.play_probability_type_1 import PlayProbabilityType1
    from ..models.play_type import PlayType
    from ..models.reference import Reference
    from ..models.team import Team


T = TypeVar("T", bound="Play")


@_attrs_define
class Play:
    """
    Attributes:
        ref (Union[Unset, str]):
        id (Union[Unset, str]):
        sequence_number (Union[Unset, str]):
        type (Union[Unset, PlayType]):
        text (Union[Unset, str]):
        short_text (Union[Unset, str]):
        alternative_text (Union[Unset, str]):
        short_alternative_text (Union[Unset, str]):
        away_score (Union[Unset, int]):
        home_score (Union[Unset, int]):
        period (Union[Unset, PlayPeriod]):
        clock (Union[Unset, PlayClock]):
        scoring_play (Union[Unset, bool]):
        priority (Union[Unset, bool]):
        score_value (Union[Unset, int]):
        modified (Union[Unset, datetime.datetime]):
        team (Union['Reference', 'Team', Unset]):
        participants (Union[Unset, List['PlayParticipant']]):
        probability (Union['PlayProbabilityType1', 'Reference', Unset]):
        wallclock (Union[Unset, datetime.datetime]):
        drive (Union['Drive', 'Reference', Unset]):
        start (Union[Unset, PlayFieldPosition]):
        end (Union[Unset, PlayFieldPosition]):
        stat_yardage (Union[Unset, int]):
    """

    ref: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    sequence_number: Union[Unset, str] = UNSET
    type: Union[Unset, "PlayType"] = UNSET
    text: Union[Unset, str] = UNSET
    short_text: Union[Unset, str] = UNSET
    alternative_text: Union[Unset, str] = UNSET
    short_alternative_text: Union[Unset, str] = UNSET
    away_score: Union[Unset, int] = UNSET
    home_score: Union[Unset, int] = UNSET
    period: Union[Unset, "PlayPeriod"] = UNSET
    clock: Union[Unset, "PlayClock"] = UNSET
    scoring_play: Union[Unset, bool] = UNSET
    priority: Union[Unset, bool] = UNSET
    score_value: Union[Unset, int] = UNSET
    modified: Union[Unset, datetime.datetime] = UNSET
    team: Union["Reference", "Team", Unset] = UNSET
    participants: Union[Unset, List["PlayParticipant"]] = UNSET
    probability: Union["PlayProbabilityType1", "Reference", Unset] = UNSET
    wallclock: Union[Unset, datetime.datetime] = UNSET
    drive: Union["Drive", "Reference", Unset] = UNSET
    start: Union[Unset, "PlayFieldPosition"] = UNSET
    end: Union[Unset, "PlayFieldPosition"] = UNSET
    stat_yardage: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.reference import Reference

        ref = self.ref

        id = self.id

        sequence_number = self.sequence_number

        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        text = self.text

        short_text = self.short_text

        alternative_text = self.alternative_text

        short_alternative_text = self.short_alternative_text

        away_score = self.away_score

        home_score = self.home_score

        period: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.to_dict()

        clock: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.clock, Unset):
            clock = self.clock.to_dict()

        scoring_play = self.scoring_play

        priority = self.priority

        score_value = self.score_value

        modified: Union[Unset, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat()

        team: Union[Dict[str, Any], Unset]
        if isinstance(self.team, Unset):
            team = UNSET
        elif isinstance(self.team, Reference):
            team = self.team.to_dict()
        else:
            team = self.team.to_dict()

        participants: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.participants, Unset):
            participants = []
            for participants_item_data in self.participants:
                participants_item = participants_item_data.to_dict()
                participants.append(participants_item)

        probability: Union[Dict[str, Any], Unset]
        if isinstance(self.probability, Unset):
            probability = UNSET
        elif isinstance(self.probability, Reference):
            probability = self.probability.to_dict()
        else:
            probability = self.probability.to_dict()

        wallclock: Union[Unset, str] = UNSET
        if not isinstance(self.wallclock, Unset):
            wallclock = self.wallclock.isoformat()

        drive: Union[Dict[str, Any], Unset]
        if isinstance(self.drive, Unset):
            drive = UNSET
        elif isinstance(self.drive, Reference):
            drive = self.drive.to_dict()
        else:
            drive = self.drive.to_dict()

        start: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.to_dict()

        end: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.to_dict()

        stat_yardage = self.stat_yardage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ref is not UNSET:
            field_dict["$ref"] = ref
        if id is not UNSET:
            field_dict["id"] = id
        if sequence_number is not UNSET:
            field_dict["sequenceNumber"] = sequence_number
        if type is not UNSET:
            field_dict["type"] = type
        if text is not UNSET:
            field_dict["text"] = text
        if short_text is not UNSET:
            field_dict["shortText"] = short_text
        if alternative_text is not UNSET:
            field_dict["alternativeText"] = alternative_text
        if short_alternative_text is not UNSET:
            field_dict["shortAlternativeText"] = short_alternative_text
        if away_score is not UNSET:
            field_dict["awayScore"] = away_score
        if home_score is not UNSET:
            field_dict["homeScore"] = home_score
        if period is not UNSET:
            field_dict["period"] = period
        if clock is not UNSET:
            field_dict["clock"] = clock
        if scoring_play is not UNSET:
            field_dict["scoringPlay"] = scoring_play
        if priority is not UNSET:
            field_dict["priority"] = priority
        if score_value is not UNSET:
            field_dict["scoreValue"] = score_value
        if modified is not UNSET:
            field_dict["modified"] = modified
        if team is not UNSET:
            field_dict["team"] = team
        if participants is not UNSET:
            field_dict["participants"] = participants
        if probability is not UNSET:
            field_dict["probability"] = probability
        if wallclock is not UNSET:
            field_dict["wallclock"] = wallclock
        if drive is not UNSET:
            field_dict["drive"] = drive
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if stat_yardage is not UNSET:
            field_dict["statYardage"] = stat_yardage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.drive import Drive
        from ..models.play_clock import PlayClock
        from ..models.play_field_position import PlayFieldPosition
        from ..models.play_participant import PlayParticipant
        from ..models.play_period import PlayPeriod
        from ..models.play_probability_type_1 import PlayProbabilityType1
        from ..models.play_type import PlayType
        from ..models.reference import Reference
        from ..models.team import Team

        d = src_dict.copy()
        ref = d.pop("$ref", UNSET)

        id = d.pop("id", UNSET)

        sequence_number = d.pop("sequenceNumber", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, PlayType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = PlayType.from_dict(_type)

        text = d.pop("text", UNSET)

        short_text = d.pop("shortText", UNSET)

        alternative_text = d.pop("alternativeText", UNSET)

        short_alternative_text = d.pop("shortAlternativeText", UNSET)

        away_score = d.pop("awayScore", UNSET)

        home_score = d.pop("homeScore", UNSET)

        _period = d.pop("period", UNSET)
        period: Union[Unset, PlayPeriod]
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = PlayPeriod.from_dict(_period)

        _clock = d.pop("clock", UNSET)
        clock: Union[Unset, PlayClock]
        if isinstance(_clock, Unset):
            clock = UNSET
        else:
            clock = PlayClock.from_dict(_clock)

        scoring_play = d.pop("scoringPlay", UNSET)

        priority = d.pop("priority", UNSET)

        score_value = d.pop("scoreValue", UNSET)

        _modified = d.pop("modified", UNSET)
        modified: Union[Unset, datetime.datetime]
        if isinstance(_modified, Unset):
            modified = UNSET
        else:
            modified = isoparse(_modified)

        def _parse_team(data: object) -> Union["Reference", "Team", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                team_type_0 = Reference.from_dict(data)

                return team_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            team_type_1 = Team.from_dict(data)

            return team_type_1

        team = _parse_team(d.pop("team", UNSET))

        participants = []
        _participants = d.pop("participants", UNSET)
        for participants_item_data in _participants or []:
            participants_item = PlayParticipant.from_dict(participants_item_data)

            participants.append(participants_item)

        def _parse_probability(data: object) -> Union["PlayProbabilityType1", "Reference", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                probability_type_0 = Reference.from_dict(data)

                return probability_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            probability_type_1 = PlayProbabilityType1.from_dict(data)

            return probability_type_1

        probability = _parse_probability(d.pop("probability", UNSET))

        _wallclock = d.pop("wallclock", UNSET)
        wallclock: Union[Unset, datetime.datetime]
        if isinstance(_wallclock, Unset):
            wallclock = UNSET
        else:
            wallclock = isoparse(_wallclock)

        def _parse_drive(data: object) -> Union["Drive", "Reference", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                drive_type_0 = Reference.from_dict(data)

                return drive_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            drive_type_1 = Drive.from_dict(data)

            return drive_type_1

        drive = _parse_drive(d.pop("drive", UNSET))

        _start = d.pop("start", UNSET)
        start: Union[Unset, PlayFieldPosition]
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = PlayFieldPosition.from_dict(_start)

        _end = d.pop("end", UNSET)
        end: Union[Unset, PlayFieldPosition]
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = PlayFieldPosition.from_dict(_end)

        stat_yardage = d.pop("statYardage", UNSET)

        play = cls(
            ref=ref,
            id=id,
            sequence_number=sequence_number,
            type=type,
            text=text,
            short_text=short_text,
            alternative_text=alternative_text,
            short_alternative_text=short_alternative_text,
            away_score=away_score,
            home_score=home_score,
            period=period,
            clock=clock,
            scoring_play=scoring_play,
            priority=priority,
            score_value=score_value,
            modified=modified,
            team=team,
            participants=participants,
            probability=probability,
            wallclock=wallclock,
            drive=drive,
            start=start,
            end=end,
            stat_yardage=stat_yardage,
        )

        play.additional_properties = d
        return play

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
