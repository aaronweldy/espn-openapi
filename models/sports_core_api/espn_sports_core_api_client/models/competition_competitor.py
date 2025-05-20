from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.competition_competitor_leaders_type_1 import CompetitionCompetitorLeadersType1
    from ..models.competition_competitor_linescores_type_1 import CompetitionCompetitorLinescoresType1
    from ..models.competition_competitor_record_type_1 import CompetitionCompetitorRecordType1
    from ..models.competition_competitor_roster_type_1 import CompetitionCompetitorRosterType1
    from ..models.competition_competitor_score_type_1 import CompetitionCompetitorScoreType1
    from ..models.competition_competitor_statistics_type_1 import CompetitionCompetitorStatisticsType1
    from ..models.competition_competitor_team_type_1 import CompetitionCompetitorTeamType1
    from ..models.reference import Reference


T = TypeVar("T", bound="CompetitionCompetitor")


@_attrs_define
class CompetitionCompetitor:
    """
    Attributes:
        ref (str):
        id (str):
        uid (str):
        type (str):
        order (int):
        home_away (str):
        winner (bool):
        team (Union['CompetitionCompetitorTeamType1', 'Reference']):
        score (Union['CompetitionCompetitorScoreType1', 'Reference']):
        linescores (Union['CompetitionCompetitorLinescoresType1', 'Reference']):
        roster (Union['CompetitionCompetitorRosterType1', 'Reference']):
        statistics (Union['CompetitionCompetitorStatisticsType1', 'Reference']):
        leaders (Union['CompetitionCompetitorLeadersType1', 'Reference']):
        record (Union['CompetitionCompetitorRecordType1', 'Reference']):
    """

    ref: str
    id: str
    uid: str
    type: str
    order: int
    home_away: str
    winner: bool
    team: Union["CompetitionCompetitorTeamType1", "Reference"]
    score: Union["CompetitionCompetitorScoreType1", "Reference"]
    linescores: Union["CompetitionCompetitorLinescoresType1", "Reference"]
    roster: Union["CompetitionCompetitorRosterType1", "Reference"]
    statistics: Union["CompetitionCompetitorStatisticsType1", "Reference"]
    leaders: Union["CompetitionCompetitorLeadersType1", "Reference"]
    record: Union["CompetitionCompetitorRecordType1", "Reference"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.reference import Reference

        ref = self.ref

        id = self.id

        uid = self.uid

        type = self.type

        order = self.order

        home_away = self.home_away

        winner = self.winner

        team: Dict[str, Any]
        if isinstance(self.team, Reference):
            team = self.team.to_dict()
        else:
            team = self.team.to_dict()

        score: Dict[str, Any]
        if isinstance(self.score, Reference):
            score = self.score.to_dict()
        else:
            score = self.score.to_dict()

        linescores: Dict[str, Any]
        if isinstance(self.linescores, Reference):
            linescores = self.linescores.to_dict()
        else:
            linescores = self.linescores.to_dict()

        roster: Dict[str, Any]
        if isinstance(self.roster, Reference):
            roster = self.roster.to_dict()
        else:
            roster = self.roster.to_dict()

        statistics: Dict[str, Any]
        if isinstance(self.statistics, Reference):
            statistics = self.statistics.to_dict()
        else:
            statistics = self.statistics.to_dict()

        leaders: Dict[str, Any]
        if isinstance(self.leaders, Reference):
            leaders = self.leaders.to_dict()
        else:
            leaders = self.leaders.to_dict()

        record: Dict[str, Any]
        if isinstance(self.record, Reference):
            record = self.record.to_dict()
        else:
            record = self.record.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "id": id,
                "uid": uid,
                "type": type,
                "order": order,
                "homeAway": home_away,
                "winner": winner,
                "team": team,
                "score": score,
                "linescores": linescores,
                "roster": roster,
                "statistics": statistics,
                "leaders": leaders,
                "record": record,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.competition_competitor_leaders_type_1 import CompetitionCompetitorLeadersType1
        from ..models.competition_competitor_linescores_type_1 import CompetitionCompetitorLinescoresType1
        from ..models.competition_competitor_record_type_1 import CompetitionCompetitorRecordType1
        from ..models.competition_competitor_roster_type_1 import CompetitionCompetitorRosterType1
        from ..models.competition_competitor_score_type_1 import CompetitionCompetitorScoreType1
        from ..models.competition_competitor_statistics_type_1 import CompetitionCompetitorStatisticsType1
        from ..models.competition_competitor_team_type_1 import CompetitionCompetitorTeamType1
        from ..models.reference import Reference

        d = src_dict.copy()
        ref = d.pop("$ref")

        id = d.pop("id")

        uid = d.pop("uid")

        type = d.pop("type")

        order = d.pop("order")

        home_away = d.pop("homeAway")

        winner = d.pop("winner")

        def _parse_team(data: object) -> Union["CompetitionCompetitorTeamType1", "Reference"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                team_type_0 = Reference.from_dict(data)

                return team_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            team_type_1 = CompetitionCompetitorTeamType1.from_dict(data)

            return team_type_1

        team = _parse_team(d.pop("team"))

        def _parse_score(data: object) -> Union["CompetitionCompetitorScoreType1", "Reference"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                score_type_0 = Reference.from_dict(data)

                return score_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            score_type_1 = CompetitionCompetitorScoreType1.from_dict(data)

            return score_type_1

        score = _parse_score(d.pop("score"))

        def _parse_linescores(data: object) -> Union["CompetitionCompetitorLinescoresType1", "Reference"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                linescores_type_0 = Reference.from_dict(data)

                return linescores_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            linescores_type_1 = CompetitionCompetitorLinescoresType1.from_dict(data)

            return linescores_type_1

        linescores = _parse_linescores(d.pop("linescores"))

        def _parse_roster(data: object) -> Union["CompetitionCompetitorRosterType1", "Reference"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                roster_type_0 = Reference.from_dict(data)

                return roster_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            roster_type_1 = CompetitionCompetitorRosterType1.from_dict(data)

            return roster_type_1

        roster = _parse_roster(d.pop("roster"))

        def _parse_statistics(data: object) -> Union["CompetitionCompetitorStatisticsType1", "Reference"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                statistics_type_0 = Reference.from_dict(data)

                return statistics_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            statistics_type_1 = CompetitionCompetitorStatisticsType1.from_dict(data)

            return statistics_type_1

        statistics = _parse_statistics(d.pop("statistics"))

        def _parse_leaders(data: object) -> Union["CompetitionCompetitorLeadersType1", "Reference"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                leaders_type_0 = Reference.from_dict(data)

                return leaders_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            leaders_type_1 = CompetitionCompetitorLeadersType1.from_dict(data)

            return leaders_type_1

        leaders = _parse_leaders(d.pop("leaders"))

        def _parse_record(data: object) -> Union["CompetitionCompetitorRecordType1", "Reference"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                record_type_0 = Reference.from_dict(data)

                return record_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            record_type_1 = CompetitionCompetitorRecordType1.from_dict(data)

            return record_type_1

        record = _parse_record(d.pop("record"))

        competition_competitor = cls(
            ref=ref,
            id=id,
            uid=uid,
            type=type,
            order=order,
            home_away=home_away,
            winner=winner,
            team=team,
            score=score,
            linescores=linescores,
            roster=roster,
            statistics=statistics,
            leaders=leaders,
            record=record,
        )

        competition_competitor.additional_properties = d
        return competition_competitor

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
