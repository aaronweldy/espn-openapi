from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
        record (Reference):
        odds_records (Reference):
        athletes (Reference):
        venue (Venue):
        groups (Reference):
        ranks (Reference):
        statistics (Reference):
        leaders (Reference):
        links (List['Link']):
        injuries (Reference):
        notes (Reference):
        against_the_spread_records (Reference):
        franchise (Reference):
        projection (Reference):
        events (Reference):
        transactions (Reference):
        coaches (Reference):
        attendance (Reference):
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
    record: "Reference"
    odds_records: "Reference"
    athletes: "Reference"
    venue: "Venue"
    groups: "Reference"
    ranks: "Reference"
    statistics: "Reference"
    leaders: "Reference"
    links: List["Link"]
    injuries: "Reference"
    notes: "Reference"
    against_the_spread_records: "Reference"
    franchise: "Reference"
    projection: "Reference"
    events: "Reference"
    transactions: "Reference"
    coaches: "Reference"
    attendance: "Reference"
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

        record = self.record.to_dict()

        odds_records = self.odds_records.to_dict()

        athletes = self.athletes.to_dict()

        venue = self.venue.to_dict()

        groups = self.groups.to_dict()

        ranks = self.ranks.to_dict()

        statistics = self.statistics.to_dict()

        leaders = self.leaders.to_dict()

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        injuries = self.injuries.to_dict()

        notes = self.notes.to_dict()

        against_the_spread_records = self.against_the_spread_records.to_dict()

        franchise = self.franchise.to_dict()

        projection = self.projection.to_dict()

        events = self.events.to_dict()

        transactions = self.transactions.to_dict()

        coaches = self.coaches.to_dict()

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
                "record": record,
                "oddsRecords": odds_records,
                "athletes": athletes,
                "venue": venue,
                "groups": groups,
                "ranks": ranks,
                "statistics": statistics,
                "leaders": leaders,
                "links": links,
                "injuries": injuries,
                "notes": notes,
                "againstTheSpreadRecords": against_the_spread_records,
                "franchise": franchise,
                "projection": projection,
                "events": events,
                "transactions": transactions,
                "coaches": coaches,
                "attendance": attendance,
            }
        )

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

        record = Reference.from_dict(d.pop("record"))

        odds_records = Reference.from_dict(d.pop("oddsRecords"))

        athletes = Reference.from_dict(d.pop("athletes"))

        venue = Venue.from_dict(d.pop("venue"))

        groups = Reference.from_dict(d.pop("groups"))

        ranks = Reference.from_dict(d.pop("ranks"))

        statistics = Reference.from_dict(d.pop("statistics"))

        leaders = Reference.from_dict(d.pop("leaders"))

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        injuries = Reference.from_dict(d.pop("injuries"))

        notes = Reference.from_dict(d.pop("notes"))

        against_the_spread_records = Reference.from_dict(d.pop("againstTheSpreadRecords"))

        franchise = Reference.from_dict(d.pop("franchise"))

        projection = Reference.from_dict(d.pop("projection"))

        events = Reference.from_dict(d.pop("events"))

        transactions = Reference.from_dict(d.pop("transactions"))

        coaches = Reference.from_dict(d.pop("coaches"))

        attendance = Reference.from_dict(d.pop("attendance"))

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
            record=record,
            odds_records=odds_records,
            athletes=athletes,
            venue=venue,
            groups=groups,
            ranks=ranks,
            statistics=statistics,
            leaders=leaders,
            links=links,
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
