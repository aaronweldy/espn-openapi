from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alternate_ids import AlternateIDS
    from ..models.link import Link
    from ..models.logo import Logo
    from ..models.reference import Reference
    from ..models.venue import Venue


T = TypeVar("T", bound="CoreNflSeasonTeamResponse")


@_attrs_define
class CoreNflSeasonTeamResponse:
    """
    Attributes:
        ref (str):
        id (str):
        guid (str):
        uid (str):
        alternate_ids (AlternateIDS):
        slug (str):
        location (str):
        name (str):
        nickname (str):
        abbreviation (str):
        display_name (str):
        short_display_name (str):
        color (str):
        alternate_color (str):
        is_active (bool):
        is_all_star (bool):
        logos (List['Logo']):
        links (List['Link']):
        record (Union[Unset, Reference]):
        odds_records (Union[Unset, Reference]):
        athletes (Union[Unset, Reference]):
        venue (Union[Unset, Venue]):
        groups (Union[Unset, Reference]):
        ranks (Union[Unset, Reference]):
        statistics (Union[Unset, Reference]):
        leaders (Union[Unset, Reference]):
        injuries (Union[Unset, Reference]):
        notes (Union[Unset, Reference]):
        against_the_spread_records (Union[Unset, Reference]):
        franchise (Union[Unset, Reference]):
        projection (Union[Unset, Reference]):
        events (Union[Unset, Reference]):
        transactions (Union[Unset, Reference]):
        coaches (Union[Unset, Reference]):
        attendance (Union[Unset, Reference]):
    """

    ref: str
    id: str
    guid: str
    uid: str
    alternate_ids: "AlternateIDS"
    slug: str
    location: str
    name: str
    nickname: str
    abbreviation: str
    display_name: str
    short_display_name: str
    color: str
    alternate_color: str
    is_active: bool
    is_all_star: bool
    logos: List["Logo"]
    links: List["Link"]
    record: Union[Unset, "Reference"] = UNSET
    odds_records: Union[Unset, "Reference"] = UNSET
    athletes: Union[Unset, "Reference"] = UNSET
    venue: Union[Unset, "Venue"] = UNSET
    groups: Union[Unset, "Reference"] = UNSET
    ranks: Union[Unset, "Reference"] = UNSET
    statistics: Union[Unset, "Reference"] = UNSET
    leaders: Union[Unset, "Reference"] = UNSET
    injuries: Union[Unset, "Reference"] = UNSET
    notes: Union[Unset, "Reference"] = UNSET
    against_the_spread_records: Union[Unset, "Reference"] = UNSET
    franchise: Union[Unset, "Reference"] = UNSET
    projection: Union[Unset, "Reference"] = UNSET
    events: Union[Unset, "Reference"] = UNSET
    transactions: Union[Unset, "Reference"] = UNSET
    coaches: Union[Unset, "Reference"] = UNSET
    attendance: Union[Unset, "Reference"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        id = self.id

        guid = self.guid

        uid = self.uid

        alternate_ids = self.alternate_ids.to_dict()

        slug = self.slug

        location = self.location

        name = self.name

        nickname = self.nickname

        abbreviation = self.abbreviation

        display_name = self.display_name

        short_display_name = self.short_display_name

        color = self.color

        alternate_color = self.alternate_color

        is_active = self.is_active

        is_all_star = self.is_all_star

        logos = []
        for logos_item_data in self.logos:
            logos_item = logos_item_data.to_dict()
            logos.append(logos_item)

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        record: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record, Unset):
            record = self.record.to_dict()

        odds_records: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odds_records, Unset):
            odds_records = self.odds_records.to_dict()

        athletes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.athletes, Unset):
            athletes = self.athletes.to_dict()

        venue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.venue, Unset):
            venue = self.venue.to_dict()

        groups: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups.to_dict()

        ranks: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ranks, Unset):
            ranks = self.ranks.to_dict()

        statistics: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        leaders: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.leaders, Unset):
            leaders = self.leaders.to_dict()

        injuries: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.injuries, Unset):
            injuries = self.injuries.to_dict()

        notes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notes, Unset):
            notes = self.notes.to_dict()

        against_the_spread_records: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.against_the_spread_records, Unset):
            against_the_spread_records = self.against_the_spread_records.to_dict()

        franchise: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.franchise, Unset):
            franchise = self.franchise.to_dict()

        projection: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.projection, Unset):
            projection = self.projection.to_dict()

        events: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events.to_dict()

        transactions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.transactions, Unset):
            transactions = self.transactions.to_dict()

        coaches: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.coaches, Unset):
            coaches = self.coaches.to_dict()

        attendance: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attendance, Unset):
            attendance = self.attendance.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "id": id,
                "guid": guid,
                "uid": uid,
                "alternateIds": alternate_ids,
                "slug": slug,
                "location": location,
                "name": name,
                "nickname": nickname,
                "abbreviation": abbreviation,
                "displayName": display_name,
                "shortDisplayName": short_display_name,
                "color": color,
                "alternateColor": alternate_color,
                "isActive": is_active,
                "isAllStar": is_all_star,
                "logos": logos,
                "links": links,
            }
        )
        if record is not UNSET:
            field_dict["record"] = record
        if odds_records is not UNSET:
            field_dict["oddsRecords"] = odds_records
        if athletes is not UNSET:
            field_dict["athletes"] = athletes
        if venue is not UNSET:
            field_dict["venue"] = venue
        if groups is not UNSET:
            field_dict["groups"] = groups
        if ranks is not UNSET:
            field_dict["ranks"] = ranks
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if leaders is not UNSET:
            field_dict["leaders"] = leaders
        if injuries is not UNSET:
            field_dict["injuries"] = injuries
        if notes is not UNSET:
            field_dict["notes"] = notes
        if against_the_spread_records is not UNSET:
            field_dict["againstTheSpreadRecords"] = against_the_spread_records
        if franchise is not UNSET:
            field_dict["franchise"] = franchise
        if projection is not UNSET:
            field_dict["projection"] = projection
        if events is not UNSET:
            field_dict["events"] = events
        if transactions is not UNSET:
            field_dict["transactions"] = transactions
        if coaches is not UNSET:
            field_dict["coaches"] = coaches
        if attendance is not UNSET:
            field_dict["attendance"] = attendance

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.alternate_ids import AlternateIDS
        from ..models.link import Link
        from ..models.logo import Logo
        from ..models.reference import Reference
        from ..models.venue import Venue

        d = src_dict.copy()
        ref = d.pop("$ref")

        id = d.pop("id")

        guid = d.pop("guid")

        uid = d.pop("uid")

        alternate_ids = AlternateIDS.from_dict(d.pop("alternateIds"))

        slug = d.pop("slug")

        location = d.pop("location")

        name = d.pop("name")

        nickname = d.pop("nickname")

        abbreviation = d.pop("abbreviation")

        display_name = d.pop("displayName")

        short_display_name = d.pop("shortDisplayName")

        color = d.pop("color")

        alternate_color = d.pop("alternateColor")

        is_active = d.pop("isActive")

        is_all_star = d.pop("isAllStar")

        logos = []
        _logos = d.pop("logos")
        for logos_item_data in _logos:
            logos_item = Logo.from_dict(logos_item_data)

            logos.append(logos_item)

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        _record = d.pop("record", UNSET)
        record: Union[Unset, Reference]
        if isinstance(_record, Unset):
            record = UNSET
        else:
            record = Reference.from_dict(_record)

        _odds_records = d.pop("oddsRecords", UNSET)
        odds_records: Union[Unset, Reference]
        if isinstance(_odds_records, Unset):
            odds_records = UNSET
        else:
            odds_records = Reference.from_dict(_odds_records)

        _athletes = d.pop("athletes", UNSET)
        athletes: Union[Unset, Reference]
        if isinstance(_athletes, Unset):
            athletes = UNSET
        else:
            athletes = Reference.from_dict(_athletes)

        _venue = d.pop("venue", UNSET)
        venue: Union[Unset, Venue]
        if isinstance(_venue, Unset):
            venue = UNSET
        else:
            venue = Venue.from_dict(_venue)

        _groups = d.pop("groups", UNSET)
        groups: Union[Unset, Reference]
        if isinstance(_groups, Unset):
            groups = UNSET
        else:
            groups = Reference.from_dict(_groups)

        _ranks = d.pop("ranks", UNSET)
        ranks: Union[Unset, Reference]
        if isinstance(_ranks, Unset):
            ranks = UNSET
        else:
            ranks = Reference.from_dict(_ranks)

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, Reference]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = Reference.from_dict(_statistics)

        _leaders = d.pop("leaders", UNSET)
        leaders: Union[Unset, Reference]
        if isinstance(_leaders, Unset):
            leaders = UNSET
        else:
            leaders = Reference.from_dict(_leaders)

        _injuries = d.pop("injuries", UNSET)
        injuries: Union[Unset, Reference]
        if isinstance(_injuries, Unset):
            injuries = UNSET
        else:
            injuries = Reference.from_dict(_injuries)

        _notes = d.pop("notes", UNSET)
        notes: Union[Unset, Reference]
        if isinstance(_notes, Unset):
            notes = UNSET
        else:
            notes = Reference.from_dict(_notes)

        _against_the_spread_records = d.pop("againstTheSpreadRecords", UNSET)
        against_the_spread_records: Union[Unset, Reference]
        if isinstance(_against_the_spread_records, Unset):
            against_the_spread_records = UNSET
        else:
            against_the_spread_records = Reference.from_dict(_against_the_spread_records)

        _franchise = d.pop("franchise", UNSET)
        franchise: Union[Unset, Reference]
        if isinstance(_franchise, Unset):
            franchise = UNSET
        else:
            franchise = Reference.from_dict(_franchise)

        _projection = d.pop("projection", UNSET)
        projection: Union[Unset, Reference]
        if isinstance(_projection, Unset):
            projection = UNSET
        else:
            projection = Reference.from_dict(_projection)

        _events = d.pop("events", UNSET)
        events: Union[Unset, Reference]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = Reference.from_dict(_events)

        _transactions = d.pop("transactions", UNSET)
        transactions: Union[Unset, Reference]
        if isinstance(_transactions, Unset):
            transactions = UNSET
        else:
            transactions = Reference.from_dict(_transactions)

        _coaches = d.pop("coaches", UNSET)
        coaches: Union[Unset, Reference]
        if isinstance(_coaches, Unset):
            coaches = UNSET
        else:
            coaches = Reference.from_dict(_coaches)

        _attendance = d.pop("attendance", UNSET)
        attendance: Union[Unset, Reference]
        if isinstance(_attendance, Unset):
            attendance = UNSET
        else:
            attendance = Reference.from_dict(_attendance)

        core_nfl_season_team_response = cls(
            ref=ref,
            id=id,
            guid=guid,
            uid=uid,
            alternate_ids=alternate_ids,
            slug=slug,
            location=location,
            name=name,
            nickname=nickname,
            abbreviation=abbreviation,
            display_name=display_name,
            short_display_name=short_display_name,
            color=color,
            alternate_color=alternate_color,
            is_active=is_active,
            is_all_star=is_all_star,
            logos=logos,
            links=links,
            record=record,
            odds_records=odds_records,
            athletes=athletes,
            venue=venue,
            groups=groups,
            ranks=ranks,
            statistics=statistics,
            leaders=leaders,
            injuries=injuries,
            notes=notes,
            against_the_spread_records=against_the_spread_records,
            franchise=franchise,
            projection=projection,
            events=events,
            transactions=transactions,
            coaches=coaches,
            attendance=attendance,
        )

        core_nfl_season_team_response.additional_properties = d
        return core_nfl_season_team_response

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
