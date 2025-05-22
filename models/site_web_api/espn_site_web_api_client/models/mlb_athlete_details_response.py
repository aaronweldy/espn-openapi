from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.mlb_athlete_details_athlete import MLBAthleteDetailsAthlete
    from ..models.mlb_athlete_details_response_league import MLBAthleteDetailsResponseLeague
    from ..models.mlb_athlete_details_response_player_switcher import MLBAthleteDetailsResponsePlayerSwitcher
    from ..models.mlb_athlete_details_response_quicklinks_item import MLBAthleteDetailsResponseQuicklinksItem
    from ..models.mlb_athlete_details_response_season import MLBAthleteDetailsResponseSeason
    from ..models.mlb_athlete_details_response_standings import MLBAthleteDetailsResponseStandings
    from ..models.mlb_athlete_details_response_tickets_info import MLBAthleteDetailsResponseTicketsInfo


T = TypeVar("T", bound="MLBAthleteDetailsResponse")


@_attrs_define
class MLBAthleteDetailsResponse:
    """MLB athlete details response from site.web.api.espn.com

    Attributes:
        athlete (MLBAthleteDetailsAthlete): MLB athlete details (athlete object) from site.web.api.espn.com
        season (MLBAthleteDetailsResponseSeason):
        league (MLBAthleteDetailsResponseLeague):
        player_switcher (MLBAthleteDetailsResponsePlayerSwitcher):
        quicklinks (List['MLBAthleteDetailsResponseQuicklinksItem']):
        links (List['Link']):
        tickets_info (MLBAthleteDetailsResponseTicketsInfo):
        standings (MLBAthleteDetailsResponseStandings):
    """

    athlete: "MLBAthleteDetailsAthlete"
    season: "MLBAthleteDetailsResponseSeason"
    league: "MLBAthleteDetailsResponseLeague"
    player_switcher: "MLBAthleteDetailsResponsePlayerSwitcher"
    quicklinks: List["MLBAthleteDetailsResponseQuicklinksItem"]
    links: List["Link"]
    tickets_info: "MLBAthleteDetailsResponseTicketsInfo"
    standings: "MLBAthleteDetailsResponseStandings"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        athlete = self.athlete.to_dict()

        season = self.season.to_dict()

        league = self.league.to_dict()

        player_switcher = self.player_switcher.to_dict()

        quicklinks = []
        for quicklinks_item_data in self.quicklinks:
            quicklinks_item = quicklinks_item_data.to_dict()
            quicklinks.append(quicklinks_item)

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        tickets_info = self.tickets_info.to_dict()

        standings = self.standings.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "athlete": athlete,
                "season": season,
                "league": league,
                "playerSwitcher": player_switcher,
                "quicklinks": quicklinks,
                "links": links,
                "ticketsInfo": tickets_info,
                "standings": standings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link import Link
        from ..models.mlb_athlete_details_athlete import MLBAthleteDetailsAthlete
        from ..models.mlb_athlete_details_response_league import MLBAthleteDetailsResponseLeague
        from ..models.mlb_athlete_details_response_player_switcher import MLBAthleteDetailsResponsePlayerSwitcher
        from ..models.mlb_athlete_details_response_quicklinks_item import MLBAthleteDetailsResponseQuicklinksItem
        from ..models.mlb_athlete_details_response_season import MLBAthleteDetailsResponseSeason
        from ..models.mlb_athlete_details_response_standings import MLBAthleteDetailsResponseStandings
        from ..models.mlb_athlete_details_response_tickets_info import MLBAthleteDetailsResponseTicketsInfo

        d = src_dict.copy()
        athlete = MLBAthleteDetailsAthlete.from_dict(d.pop("athlete"))

        season = MLBAthleteDetailsResponseSeason.from_dict(d.pop("season"))

        league = MLBAthleteDetailsResponseLeague.from_dict(d.pop("league"))

        player_switcher = MLBAthleteDetailsResponsePlayerSwitcher.from_dict(d.pop("playerSwitcher"))

        quicklinks = []
        _quicklinks = d.pop("quicklinks")
        for quicklinks_item_data in _quicklinks:
            quicklinks_item = MLBAthleteDetailsResponseQuicklinksItem.from_dict(quicklinks_item_data)

            quicklinks.append(quicklinks_item)

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        tickets_info = MLBAthleteDetailsResponseTicketsInfo.from_dict(d.pop("ticketsInfo"))

        standings = MLBAthleteDetailsResponseStandings.from_dict(d.pop("standings"))

        mlb_athlete_details_response = cls(
            athlete=athlete,
            season=season,
            league=league,
            player_switcher=player_switcher,
            quicklinks=quicklinks,
            links=links,
            tickets_info=tickets_info,
            standings=standings,
        )

        mlb_athlete_details_response.additional_properties = d
        return mlb_athlete_details_response

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
