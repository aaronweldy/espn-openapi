from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_record import TeamRecord
    from ..models.team_roster import TeamRoster
    from ..models.transaction_counter import TransactionCounter


T = TypeVar("T", bound="FantasyTeam")


@_attrs_define
class FantasyTeam:
    """
    Attributes:
        id (int): Team ID Example: 1.
        name (str): Full team name Example: Example Team.
        abbreviation (Union[Unset, str]): Team abbreviation Example: TEAM1.
        location (Union[Unset, str]): Team location (first part of name) Example: Example.
        nickname (Union[Unset, str]): Team nickname (second part of name) Example: Team.
        logo (Union[Unset, str]): Team logo URL Example: https://example.com/logo.png.
        owner_id (Union[Unset, str]): Owner's member ID Example: {123456789-ABCD-EF12-3456-7890ABCDEF12}.
        primary_owner (Union[Unset, str]): Primary owner's member ID Example: {123456789-ABCD-EF12-3456-7890ABCDEF12}.
        draft_day_projected_rank (Union[Unset, int]): Projected rank on draft day Example: 5.
        current_projected_rank (Union[Unset, int]): Current projected rank Example: 3.
        playoff_seed (Union[Unset, int]): Team's playoff seed (0 if not determined)
        points (Union[Unset, float]): Total points scored Example: 108.5.
        points_adjusted (Union[Unset, float]): Points after adjustments Example: 108.5.
        points_against (Union[Unset, float]): Total points scored against Example: 95.2.
        division_id (Union[Unset, int]): Division ID
        record (Union[Unset, TeamRecord]):
        roster (Union[Unset, TeamRoster]):
        transaction_counter (Union[Unset, TransactionCounter]):
    """

    id: int
    name: str
    abbreviation: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    nickname: Union[Unset, str] = UNSET
    logo: Union[Unset, str] = UNSET
    owner_id: Union[Unset, str] = UNSET
    primary_owner: Union[Unset, str] = UNSET
    draft_day_projected_rank: Union[Unset, int] = UNSET
    current_projected_rank: Union[Unset, int] = UNSET
    playoff_seed: Union[Unset, int] = UNSET
    points: Union[Unset, float] = UNSET
    points_adjusted: Union[Unset, float] = UNSET
    points_against: Union[Unset, float] = UNSET
    division_id: Union[Unset, int] = UNSET
    record: Union[Unset, "TeamRecord"] = UNSET
    roster: Union[Unset, "TeamRoster"] = UNSET
    transaction_counter: Union[Unset, "TransactionCounter"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        abbreviation = self.abbreviation

        location = self.location

        nickname = self.nickname

        logo = self.logo

        owner_id = self.owner_id

        primary_owner = self.primary_owner

        draft_day_projected_rank = self.draft_day_projected_rank

        current_projected_rank = self.current_projected_rank

        playoff_seed = self.playoff_seed

        points = self.points

        points_adjusted = self.points_adjusted

        points_against = self.points_against

        division_id = self.division_id

        record: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record, Unset):
            record = self.record.to_dict()

        roster: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.roster, Unset):
            roster = self.roster.to_dict()

        transaction_counter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.transaction_counter, Unset):
            transaction_counter = self.transaction_counter.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if location is not UNSET:
            field_dict["location"] = location
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if logo is not UNSET:
            field_dict["logo"] = logo
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if primary_owner is not UNSET:
            field_dict["primaryOwner"] = primary_owner
        if draft_day_projected_rank is not UNSET:
            field_dict["draftDayProjectedRank"] = draft_day_projected_rank
        if current_projected_rank is not UNSET:
            field_dict["currentProjectedRank"] = current_projected_rank
        if playoff_seed is not UNSET:
            field_dict["playoffSeed"] = playoff_seed
        if points is not UNSET:
            field_dict["points"] = points
        if points_adjusted is not UNSET:
            field_dict["pointsAdjusted"] = points_adjusted
        if points_against is not UNSET:
            field_dict["pointsAgainst"] = points_against
        if division_id is not UNSET:
            field_dict["divisionId"] = division_id
        if record is not UNSET:
            field_dict["record"] = record
        if roster is not UNSET:
            field_dict["roster"] = roster
        if transaction_counter is not UNSET:
            field_dict["transactionCounter"] = transaction_counter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team_record import TeamRecord
        from ..models.team_roster import TeamRoster
        from ..models.transaction_counter import TransactionCounter

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        abbreviation = d.pop("abbreviation", UNSET)

        location = d.pop("location", UNSET)

        nickname = d.pop("nickname", UNSET)

        logo = d.pop("logo", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        primary_owner = d.pop("primaryOwner", UNSET)

        draft_day_projected_rank = d.pop("draftDayProjectedRank", UNSET)

        current_projected_rank = d.pop("currentProjectedRank", UNSET)

        playoff_seed = d.pop("playoffSeed", UNSET)

        points = d.pop("points", UNSET)

        points_adjusted = d.pop("pointsAdjusted", UNSET)

        points_against = d.pop("pointsAgainst", UNSET)

        division_id = d.pop("divisionId", UNSET)

        _record = d.pop("record", UNSET)
        record: Union[Unset, TeamRecord]
        if isinstance(_record, Unset):
            record = UNSET
        else:
            record = TeamRecord.from_dict(_record)

        _roster = d.pop("roster", UNSET)
        roster: Union[Unset, TeamRoster]
        if isinstance(_roster, Unset):
            roster = UNSET
        else:
            roster = TeamRoster.from_dict(_roster)

        _transaction_counter = d.pop("transactionCounter", UNSET)
        transaction_counter: Union[Unset, TransactionCounter]
        if isinstance(_transaction_counter, Unset):
            transaction_counter = UNSET
        else:
            transaction_counter = TransactionCounter.from_dict(_transaction_counter)

        fantasy_team = cls(
            id=id,
            name=name,
            abbreviation=abbreviation,
            location=location,
            nickname=nickname,
            logo=logo,
            owner_id=owner_id,
            primary_owner=primary_owner,
            draft_day_projected_rank=draft_day_projected_rank,
            current_projected_rank=current_projected_rank,
            playoff_seed=playoff_seed,
            points=points,
            points_adjusted=points_adjusted,
            points_against=points_against,
            division_id=division_id,
            record=record,
            roster=roster,
            transaction_counter=transaction_counter,
        )

        fantasy_team.additional_properties = d
        return fantasy_team

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
