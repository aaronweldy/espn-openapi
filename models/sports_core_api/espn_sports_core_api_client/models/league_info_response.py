from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.league_season import LeagueSeason
    from ..models.link import Link
    from ..models.logo import Logo
    from ..models.reference import Reference


T = TypeVar("T", bound="LeagueInfoResponse")


@_attrs_define
class LeagueInfoResponse:
    """
    Attributes:
        id (str):  Example: 28.
        name (str):  Example: National Football League.
        display_name (str):  Example: NFL.
        abbreviation (str):  Example: NFL.
        slug (str):  Example: nfl.
        ref (Union[Unset, str]):  Example:
            http://sports.core.api.espn.com/v2/sports/football/leagues/nfl?lang=en&region=us.
        uid (Union[Unset, str]):  Example: s:20~l:28.
        guid (Union[Unset, str]):  Example: ad4c3bd2-ddb6-3f8c-8abf-744855a08fa4.
        short_name (Union[Unset, str]):  Example: NFL.
        midsize_name (Union[Unset, str]):  Example: NCAA Football.
        is_tournament (Union[Unset, bool]):
        gender (Union[Unset, str]):  Example: MALE.
        season (Union[Unset, LeagueSeason]):
        seasons (Union[Unset, Reference]):
        franchises (Union[Unset, Reference]):
        teams (Union[Unset, Reference]):
        group (Union[Unset, Reference]):
        groups (Union[Unset, Reference]):
        events (Union[Unset, Reference]):
        notes (Union[Unset, Reference]):
        rankings (Union[Unset, Reference]):
        awards (Union[Unset, Reference]):
        calendar (Union[Unset, Reference]):
        transactions (Union[Unset, Reference]):
        draft (Union[Unset, Reference]):
        leaders (Union[Unset, Reference]):
        athletes (Union[Unset, Reference]):
        free_agents (Union[Unset, Reference]):
        talent_picks (Union[Unset, Reference]):
        links (Union[Unset, List['Link']]):
        logos (Union[Unset, List['Logo']]):
    """

    id: str
    name: str
    display_name: str
    abbreviation: str
    slug: str
    ref: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    midsize_name: Union[Unset, str] = UNSET
    is_tournament: Union[Unset, bool] = UNSET
    gender: Union[Unset, str] = UNSET
    season: Union[Unset, "LeagueSeason"] = UNSET
    seasons: Union[Unset, "Reference"] = UNSET
    franchises: Union[Unset, "Reference"] = UNSET
    teams: Union[Unset, "Reference"] = UNSET
    group: Union[Unset, "Reference"] = UNSET
    groups: Union[Unset, "Reference"] = UNSET
    events: Union[Unset, "Reference"] = UNSET
    notes: Union[Unset, "Reference"] = UNSET
    rankings: Union[Unset, "Reference"] = UNSET
    awards: Union[Unset, "Reference"] = UNSET
    calendar: Union[Unset, "Reference"] = UNSET
    transactions: Union[Unset, "Reference"] = UNSET
    draft: Union[Unset, "Reference"] = UNSET
    leaders: Union[Unset, "Reference"] = UNSET
    athletes: Union[Unset, "Reference"] = UNSET
    free_agents: Union[Unset, "Reference"] = UNSET
    talent_picks: Union[Unset, "Reference"] = UNSET
    links: Union[Unset, List["Link"]] = UNSET
    logos: Union[Unset, List["Logo"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        display_name = self.display_name

        abbreviation = self.abbreviation

        slug = self.slug

        ref = self.ref

        uid = self.uid

        guid = self.guid

        short_name = self.short_name

        midsize_name = self.midsize_name

        is_tournament = self.is_tournament

        gender = self.gender

        season: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        seasons: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.seasons, Unset):
            seasons = self.seasons.to_dict()

        franchises: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.franchises, Unset):
            franchises = self.franchises.to_dict()

        teams: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.teams, Unset):
            teams = self.teams.to_dict()

        group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        groups: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups.to_dict()

        events: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events.to_dict()

        notes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notes, Unset):
            notes = self.notes.to_dict()

        rankings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rankings, Unset):
            rankings = self.rankings.to_dict()

        awards: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.awards, Unset):
            awards = self.awards.to_dict()

        calendar: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.calendar, Unset):
            calendar = self.calendar.to_dict()

        transactions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.transactions, Unset):
            transactions = self.transactions.to_dict()

        draft: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.draft, Unset):
            draft = self.draft.to_dict()

        leaders: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.leaders, Unset):
            leaders = self.leaders.to_dict()

        athletes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.athletes, Unset):
            athletes = self.athletes.to_dict()

        free_agents: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.free_agents, Unset):
            free_agents = self.free_agents.to_dict()

        talent_picks: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.talent_picks, Unset):
            talent_picks = self.talent_picks.to_dict()

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        logos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.logos, Unset):
            logos = []
            for logos_item_data in self.logos:
                logos_item = logos_item_data.to_dict()
                logos.append(logos_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "displayName": display_name,
                "abbreviation": abbreviation,
                "slug": slug,
            }
        )
        if ref is not UNSET:
            field_dict["$ref"] = ref
        if uid is not UNSET:
            field_dict["uid"] = uid
        if guid is not UNSET:
            field_dict["guid"] = guid
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if midsize_name is not UNSET:
            field_dict["midsizeName"] = midsize_name
        if is_tournament is not UNSET:
            field_dict["isTournament"] = is_tournament
        if gender is not UNSET:
            field_dict["gender"] = gender
        if season is not UNSET:
            field_dict["season"] = season
        if seasons is not UNSET:
            field_dict["seasons"] = seasons
        if franchises is not UNSET:
            field_dict["franchises"] = franchises
        if teams is not UNSET:
            field_dict["teams"] = teams
        if group is not UNSET:
            field_dict["group"] = group
        if groups is not UNSET:
            field_dict["groups"] = groups
        if events is not UNSET:
            field_dict["events"] = events
        if notes is not UNSET:
            field_dict["notes"] = notes
        if rankings is not UNSET:
            field_dict["rankings"] = rankings
        if awards is not UNSET:
            field_dict["awards"] = awards
        if calendar is not UNSET:
            field_dict["calendar"] = calendar
        if transactions is not UNSET:
            field_dict["transactions"] = transactions
        if draft is not UNSET:
            field_dict["draft"] = draft
        if leaders is not UNSET:
            field_dict["leaders"] = leaders
        if athletes is not UNSET:
            field_dict["athletes"] = athletes
        if free_agents is not UNSET:
            field_dict["freeAgents"] = free_agents
        if talent_picks is not UNSET:
            field_dict["talentPicks"] = talent_picks
        if links is not UNSET:
            field_dict["links"] = links
        if logos is not UNSET:
            field_dict["logos"] = logos

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.league_season import LeagueSeason
        from ..models.link import Link
        from ..models.logo import Logo
        from ..models.reference import Reference

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        display_name = d.pop("displayName")

        abbreviation = d.pop("abbreviation")

        slug = d.pop("slug")

        ref = d.pop("$ref", UNSET)

        uid = d.pop("uid", UNSET)

        guid = d.pop("guid", UNSET)

        short_name = d.pop("shortName", UNSET)

        midsize_name = d.pop("midsizeName", UNSET)

        is_tournament = d.pop("isTournament", UNSET)

        gender = d.pop("gender", UNSET)

        _season = d.pop("season", UNSET)
        season: Union[Unset, LeagueSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = LeagueSeason.from_dict(_season)

        _seasons = d.pop("seasons", UNSET)
        seasons: Union[Unset, Reference]
        if isinstance(_seasons, Unset):
            seasons = UNSET
        else:
            seasons = Reference.from_dict(_seasons)

        _franchises = d.pop("franchises", UNSET)
        franchises: Union[Unset, Reference]
        if isinstance(_franchises, Unset):
            franchises = UNSET
        else:
            franchises = Reference.from_dict(_franchises)

        _teams = d.pop("teams", UNSET)
        teams: Union[Unset, Reference]
        if isinstance(_teams, Unset):
            teams = UNSET
        else:
            teams = Reference.from_dict(_teams)

        _group = d.pop("group", UNSET)
        group: Union[Unset, Reference]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = Reference.from_dict(_group)

        _groups = d.pop("groups", UNSET)
        groups: Union[Unset, Reference]
        if isinstance(_groups, Unset):
            groups = UNSET
        else:
            groups = Reference.from_dict(_groups)

        _events = d.pop("events", UNSET)
        events: Union[Unset, Reference]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = Reference.from_dict(_events)

        _notes = d.pop("notes", UNSET)
        notes: Union[Unset, Reference]
        if isinstance(_notes, Unset):
            notes = UNSET
        else:
            notes = Reference.from_dict(_notes)

        _rankings = d.pop("rankings", UNSET)
        rankings: Union[Unset, Reference]
        if isinstance(_rankings, Unset):
            rankings = UNSET
        else:
            rankings = Reference.from_dict(_rankings)

        _awards = d.pop("awards", UNSET)
        awards: Union[Unset, Reference]
        if isinstance(_awards, Unset):
            awards = UNSET
        else:
            awards = Reference.from_dict(_awards)

        _calendar = d.pop("calendar", UNSET)
        calendar: Union[Unset, Reference]
        if isinstance(_calendar, Unset):
            calendar = UNSET
        else:
            calendar = Reference.from_dict(_calendar)

        _transactions = d.pop("transactions", UNSET)
        transactions: Union[Unset, Reference]
        if isinstance(_transactions, Unset):
            transactions = UNSET
        else:
            transactions = Reference.from_dict(_transactions)

        _draft = d.pop("draft", UNSET)
        draft: Union[Unset, Reference]
        if isinstance(_draft, Unset):
            draft = UNSET
        else:
            draft = Reference.from_dict(_draft)

        _leaders = d.pop("leaders", UNSET)
        leaders: Union[Unset, Reference]
        if isinstance(_leaders, Unset):
            leaders = UNSET
        else:
            leaders = Reference.from_dict(_leaders)

        _athletes = d.pop("athletes", UNSET)
        athletes: Union[Unset, Reference]
        if isinstance(_athletes, Unset):
            athletes = UNSET
        else:
            athletes = Reference.from_dict(_athletes)

        _free_agents = d.pop("freeAgents", UNSET)
        free_agents: Union[Unset, Reference]
        if isinstance(_free_agents, Unset):
            free_agents = UNSET
        else:
            free_agents = Reference.from_dict(_free_agents)

        _talent_picks = d.pop("talentPicks", UNSET)
        talent_picks: Union[Unset, Reference]
        if isinstance(_talent_picks, Unset):
            talent_picks = UNSET
        else:
            talent_picks = Reference.from_dict(_talent_picks)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        logos = []
        _logos = d.pop("logos", UNSET)
        for logos_item_data in _logos or []:
            logos_item = Logo.from_dict(logos_item_data)

            logos.append(logos_item)

        league_info_response = cls(
            id=id,
            name=name,
            display_name=display_name,
            abbreviation=abbreviation,
            slug=slug,
            ref=ref,
            uid=uid,
            guid=guid,
            short_name=short_name,
            midsize_name=midsize_name,
            is_tournament=is_tournament,
            gender=gender,
            season=season,
            seasons=seasons,
            franchises=franchises,
            teams=teams,
            group=group,
            groups=groups,
            events=events,
            notes=notes,
            rankings=rankings,
            awards=awards,
            calendar=calendar,
            transactions=transactions,
            draft=draft,
            leaders=leaders,
            athletes=athletes,
            free_agents=free_agents,
            talent_picks=talent_picks,
            links=links,
            logos=logos,
        )

        league_info_response.additional_properties = d
        return league_info_response

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
