from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.logo import Logo
    from ..models.stats_team_against_the_spread_records import StatsTeamAgainstTheSpreadRecords
    from ..models.stats_team_coaches import StatsTeamCoaches
    from ..models.stats_team_franchise import StatsTeamFranchise
    from ..models.stats_team_groups import StatsTeamGroups
    from ..models.stats_team_ranks import StatsTeamRanks
    from ..models.stats_team_record import StatsTeamRecord
    from ..models.stats_venue import StatsVenue


T = TypeVar("T", bound="StatsTeam")


@_attrs_define
class StatsTeam:
    """
    Attributes:
        id (str): Team ID
        display_name (str): Full team name
        uid (Union[Unset, str]): Unique identifier
        guid (Union[Unset, str]): Global unique identifier
        slug (Union[Unset, str]): URL slug
        location (Union[Unset, str]): Team location
        name (Union[Unset, str]): Team name
        nickname (Union[Unset, str]): Team nickname
        abbreviation (Union[Unset, str]): Team abbreviation
        short_display_name (Union[Unset, str]): Short display name
        color (Union[Unset, str]): Primary team color
        alternate_color (Union[Unset, str]): Alternate team color
        is_active (Union[Unset, bool]): Whether team is active
        is_all_star (Union[Unset, bool]): Whether this is an all-star team
        logos (Union[Unset, List['Logo']]):
        links (Union[Unset, List['Link']]):
        venue (Union[Unset, StatsVenue]):
        record (Union[Unset, StatsTeamRecord]): Team record
        against_the_spread_records (Union[Unset, StatsTeamAgainstTheSpreadRecords]): ATS records
        ranks (Union[Unset, StatsTeamRanks]): Team rankings
        franchise (Union[Unset, StatsTeamFranchise]): Franchise information
        coaches (Union[Unset, StatsTeamCoaches]): Coaching staff
        groups (Union[Unset, StatsTeamGroups]): Groups/divisions
    """

    id: str
    display_name: str
    uid: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    nickname: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    short_display_name: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    alternate_color: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    is_all_star: Union[Unset, bool] = UNSET
    logos: Union[Unset, List["Logo"]] = UNSET
    links: Union[Unset, List["Link"]] = UNSET
    venue: Union[Unset, "StatsVenue"] = UNSET
    record: Union[Unset, "StatsTeamRecord"] = UNSET
    against_the_spread_records: Union[Unset, "StatsTeamAgainstTheSpreadRecords"] = UNSET
    ranks: Union[Unset, "StatsTeamRanks"] = UNSET
    franchise: Union[Unset, "StatsTeamFranchise"] = UNSET
    coaches: Union[Unset, "StatsTeamCoaches"] = UNSET
    groups: Union[Unset, "StatsTeamGroups"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        display_name = self.display_name

        uid = self.uid

        guid = self.guid

        slug = self.slug

        location = self.location

        name = self.name

        nickname = self.nickname

        abbreviation = self.abbreviation

        short_display_name = self.short_display_name

        color = self.color

        alternate_color = self.alternate_color

        is_active = self.is_active

        is_all_star = self.is_all_star

        logos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.logos, Unset):
            logos = []
            for logos_item_data in self.logos:
                logos_item = logos_item_data.to_dict()
                logos.append(logos_item)

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        venue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.venue, Unset):
            venue = self.venue.to_dict()

        record: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record, Unset):
            record = self.record.to_dict()

        against_the_spread_records: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.against_the_spread_records, Unset):
            against_the_spread_records = self.against_the_spread_records.to_dict()

        ranks: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ranks, Unset):
            ranks = self.ranks.to_dict()

        franchise: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.franchise, Unset):
            franchise = self.franchise.to_dict()

        coaches: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.coaches, Unset):
            coaches = self.coaches.to_dict()

        groups: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "displayName": display_name,
            }
        )
        if uid is not UNSET:
            field_dict["uid"] = uid
        if guid is not UNSET:
            field_dict["guid"] = guid
        if slug is not UNSET:
            field_dict["slug"] = slug
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if short_display_name is not UNSET:
            field_dict["shortDisplayName"] = short_display_name
        if color is not UNSET:
            field_dict["color"] = color
        if alternate_color is not UNSET:
            field_dict["alternateColor"] = alternate_color
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if is_all_star is not UNSET:
            field_dict["isAllStar"] = is_all_star
        if logos is not UNSET:
            field_dict["logos"] = logos
        if links is not UNSET:
            field_dict["links"] = links
        if venue is not UNSET:
            field_dict["venue"] = venue
        if record is not UNSET:
            field_dict["record"] = record
        if against_the_spread_records is not UNSET:
            field_dict["againstTheSpreadRecords"] = against_the_spread_records
        if ranks is not UNSET:
            field_dict["ranks"] = ranks
        if franchise is not UNSET:
            field_dict["franchise"] = franchise
        if coaches is not UNSET:
            field_dict["coaches"] = coaches
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link import Link
        from ..models.logo import Logo
        from ..models.stats_team_against_the_spread_records import StatsTeamAgainstTheSpreadRecords
        from ..models.stats_team_coaches import StatsTeamCoaches
        from ..models.stats_team_franchise import StatsTeamFranchise
        from ..models.stats_team_groups import StatsTeamGroups
        from ..models.stats_team_ranks import StatsTeamRanks
        from ..models.stats_team_record import StatsTeamRecord
        from ..models.stats_venue import StatsVenue

        d = src_dict.copy()
        id = d.pop("id")

        display_name = d.pop("displayName")

        uid = d.pop("uid", UNSET)

        guid = d.pop("guid", UNSET)

        slug = d.pop("slug", UNSET)

        location = d.pop("location", UNSET)

        name = d.pop("name", UNSET)

        nickname = d.pop("nickname", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        short_display_name = d.pop("shortDisplayName", UNSET)

        color = d.pop("color", UNSET)

        alternate_color = d.pop("alternateColor", UNSET)

        is_active = d.pop("isActive", UNSET)

        is_all_star = d.pop("isAllStar", UNSET)

        logos = []
        _logos = d.pop("logos", UNSET)
        for logos_item_data in _logos or []:
            logos_item = Logo.from_dict(logos_item_data)

            logos.append(logos_item)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        _venue = d.pop("venue", UNSET)
        venue: Union[Unset, StatsVenue]
        if isinstance(_venue, Unset):
            venue = UNSET
        else:
            venue = StatsVenue.from_dict(_venue)

        _record = d.pop("record", UNSET)
        record: Union[Unset, StatsTeamRecord]
        if isinstance(_record, Unset):
            record = UNSET
        else:
            record = StatsTeamRecord.from_dict(_record)

        _against_the_spread_records = d.pop("againstTheSpreadRecords", UNSET)
        against_the_spread_records: Union[Unset, StatsTeamAgainstTheSpreadRecords]
        if isinstance(_against_the_spread_records, Unset):
            against_the_spread_records = UNSET
        else:
            against_the_spread_records = StatsTeamAgainstTheSpreadRecords.from_dict(_against_the_spread_records)

        _ranks = d.pop("ranks", UNSET)
        ranks: Union[Unset, StatsTeamRanks]
        if isinstance(_ranks, Unset):
            ranks = UNSET
        else:
            ranks = StatsTeamRanks.from_dict(_ranks)

        _franchise = d.pop("franchise", UNSET)
        franchise: Union[Unset, StatsTeamFranchise]
        if isinstance(_franchise, Unset):
            franchise = UNSET
        else:
            franchise = StatsTeamFranchise.from_dict(_franchise)

        _coaches = d.pop("coaches", UNSET)
        coaches: Union[Unset, StatsTeamCoaches]
        if isinstance(_coaches, Unset):
            coaches = UNSET
        else:
            coaches = StatsTeamCoaches.from_dict(_coaches)

        _groups = d.pop("groups", UNSET)
        groups: Union[Unset, StatsTeamGroups]
        if isinstance(_groups, Unset):
            groups = UNSET
        else:
            groups = StatsTeamGroups.from_dict(_groups)

        stats_team = cls(
            id=id,
            display_name=display_name,
            uid=uid,
            guid=guid,
            slug=slug,
            location=location,
            name=name,
            nickname=nickname,
            abbreviation=abbreviation,
            short_display_name=short_display_name,
            color=color,
            alternate_color=alternate_color,
            is_active=is_active,
            is_all_star=is_all_star,
            logos=logos,
            links=links,
            venue=venue,
            record=record,
            against_the_spread_records=against_the_spread_records,
            ranks=ranks,
            franchise=franchise,
            coaches=coaches,
            groups=groups,
        )

        stats_team.additional_properties = d
        return stats_team

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
