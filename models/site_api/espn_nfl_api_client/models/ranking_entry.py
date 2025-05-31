import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ranked_team import RankedTeam


T = TypeVar("T", bound="RankingEntry")


@_attrs_define
class RankingEntry:
    """Individual team ranking entry

    Attributes:
        current (Union[Unset, int]): Current rank
        previous (Union[Unset, int]): Previous rank
        points (Union[Unset, int]): Total points received
        first_place_votes (Union[Unset, int]): Number of first place votes
        trend (Union[Unset, str]): Trend indicator (up, down, or "-")
        team (Union[Unset, RankedTeam]): Team information in rankings
        date (Union[Unset, datetime.datetime]): Date of the ranking
        last_updated (Union[Unset, datetime.datetime]): When the ranking was last updated
        record_summary (Union[Unset, str]): Team's record summary (e.g., "14-2")
    """

    current: Union[Unset, int] = UNSET
    previous: Union[Unset, int] = UNSET
    points: Union[Unset, int] = UNSET
    first_place_votes: Union[Unset, int] = UNSET
    trend: Union[Unset, str] = UNSET
    team: Union[Unset, "RankedTeam"] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    record_summary: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current = self.current

        previous = self.previous

        points = self.points

        first_place_votes = self.first_place_votes

        trend = self.trend

        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        record_summary = self.record_summary

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current is not UNSET:
            field_dict["current"] = current
        if previous is not UNSET:
            field_dict["previous"] = previous
        if points is not UNSET:
            field_dict["points"] = points
        if first_place_votes is not UNSET:
            field_dict["firstPlaceVotes"] = first_place_votes
        if trend is not UNSET:
            field_dict["trend"] = trend
        if team is not UNSET:
            field_dict["team"] = team
        if date is not UNSET:
            field_dict["date"] = date
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if record_summary is not UNSET:
            field_dict["recordSummary"] = record_summary

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ranked_team import RankedTeam

        d = src_dict.copy()
        current = d.pop("current", UNSET)

        previous = d.pop("previous", UNSET)

        points = d.pop("points", UNSET)

        first_place_votes = d.pop("firstPlaceVotes", UNSET)

        trend = d.pop("trend", UNSET)

        _team = d.pop("team", UNSET)
        team: Union[Unset, RankedTeam]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = RankedTeam.from_dict(_team)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        record_summary = d.pop("recordSummary", UNSET)

        ranking_entry = cls(
            current=current,
            previous=previous,
            points=points,
            first_place_votes=first_place_votes,
            trend=trend,
            team=team,
            date=date,
            last_updated=last_updated,
            record_summary=record_summary,
        )

        ranking_entry.additional_properties = d
        return ranking_entry

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
