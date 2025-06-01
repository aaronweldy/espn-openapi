import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.probability_source import ProbabilitySource
    from ..models.reference import Reference


T = TypeVar("T", bound="ProbabilityItem")


@_attrs_define
class ProbabilityItem:
    """
    Attributes:
        ref (str): Reference URL to this probability entry Example: http://sports.core.api.espn.com/v2/sports/football/l
            eagues/nfl/events/401547417/competitions/401547417/probabilities/4015474171?lang=en&region=us.
        competition (Reference):
        play (Reference):
        home_team (Reference):
        away_team (Reference):
        tie_percentage (float): Probability of the game ending in a tie (0 for sports without ties)
        home_win_percentage (float): Probability of the home team winning (0-1) Example: 0.5168.
        away_win_percentage (float): Probability of the away team winning (0-1) Example: 0.4832.
        last_modified (datetime.datetime): When this probability was last updated Example: 2023-09-17T22:24Z.
        sequence_number (str): Sequence number for ordering probabilities Example: 100.
        source (ProbabilitySource):
        seconds_left (Union[Unset, int]): Seconds remaining in the game (optional, may not be present for all sports)
    """

    ref: str
    competition: "Reference"
    play: "Reference"
    home_team: "Reference"
    away_team: "Reference"
    tie_percentage: float
    home_win_percentage: float
    away_win_percentage: float
    last_modified: datetime.datetime
    sequence_number: str
    source: "ProbabilitySource"
    seconds_left: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        competition = self.competition.to_dict()

        play = self.play.to_dict()

        home_team = self.home_team.to_dict()

        away_team = self.away_team.to_dict()

        tie_percentage = self.tie_percentage

        home_win_percentage = self.home_win_percentage

        away_win_percentage = self.away_win_percentage

        last_modified = self.last_modified.isoformat()

        sequence_number = self.sequence_number

        source = self.source.to_dict()

        seconds_left = self.seconds_left

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "competition": competition,
                "play": play,
                "homeTeam": home_team,
                "awayTeam": away_team,
                "tiePercentage": tie_percentage,
                "homeWinPercentage": home_win_percentage,
                "awayWinPercentage": away_win_percentage,
                "lastModified": last_modified,
                "sequenceNumber": sequence_number,
                "source": source,
            }
        )
        if seconds_left is not UNSET:
            field_dict["secondsLeft"] = seconds_left

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.probability_source import ProbabilitySource
        from ..models.reference import Reference

        d = src_dict.copy()
        ref = d.pop("$ref")

        competition = Reference.from_dict(d.pop("competition"))

        play = Reference.from_dict(d.pop("play"))

        home_team = Reference.from_dict(d.pop("homeTeam"))

        away_team = Reference.from_dict(d.pop("awayTeam"))

        tie_percentage = d.pop("tiePercentage")

        home_win_percentage = d.pop("homeWinPercentage")

        away_win_percentage = d.pop("awayWinPercentage")

        last_modified = isoparse(d.pop("lastModified"))

        sequence_number = d.pop("sequenceNumber")

        source = ProbabilitySource.from_dict(d.pop("source"))

        seconds_left = d.pop("secondsLeft", UNSET)

        probability_item = cls(
            ref=ref,
            competition=competition,
            play=play,
            home_team=home_team,
            away_team=away_team,
            tie_percentage=tie_percentage,
            home_win_percentage=home_win_percentage,
            away_win_percentage=away_win_percentage,
            last_modified=last_modified,
            sequence_number=sequence_number,
            source=source,
            seconds_left=seconds_left,
        )

        probability_item.additional_properties = d
        return probability_item

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
