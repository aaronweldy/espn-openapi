import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.college import College
    from ..models.injury import Injury
    from ..models.link import Link
    from ..models.position import Position
    from ..models.roster_athlete_alternate_ids import RosterAthleteAlternateIds
    from ..models.roster_athlete_birth_place import RosterAthleteBirthPlace
    from ..models.roster_athlete_contracts_item import RosterAthleteContractsItem
    from ..models.roster_athlete_experience import RosterAthleteExperience
    from ..models.roster_athlete_headshot import RosterAthleteHeadshot
    from ..models.roster_athlete_status import RosterAthleteStatus
    from ..models.roster_athlete_teams_item import RosterAthleteTeamsItem


T = TypeVar("T", bound="RosterAthlete")


@_attrs_define
class RosterAthlete:
    """Athlete information for team roster

    Attributes:
        id (Union[Unset, str]): Unique identifier for the athlete
        uid (Union[Unset, str]): Unique identifier in the format s:xx~l:xx~a:xxxxxxx
        guid (Union[Unset, str]): Global unique identifier
        alternate_ids (Union[Unset, RosterAthleteAlternateIds]): Alternative IDs for the athlete
        first_name (Union[Unset, str]): Athlete's first name
        last_name (Union[Unset, str]): Athlete's last name
        full_name (Union[Unset, str]): Athlete's full name
        display_name (Union[Unset, str]): Athlete's display name
        short_name (Union[Unset, str]): Athlete's short name
        weight (Union[Unset, float]): Athlete's weight in pounds
        display_weight (Union[Unset, str]): Athlete's weight as a formatted string
        height (Union[Unset, float]): Athlete's height in inches
        display_height (Union[Unset, str]): Athlete's height as a formatted string
        age (Union[Unset, int]): Athlete's age
        date_of_birth (Union[Unset, datetime.datetime]): Athlete's date of birth
        birth_place (Union[Unset, RosterAthleteBirthPlace]):
        links (Union[Unset, List['Link']]): URLs related to the athlete
        college (Union[Unset, College]): Information about athlete's college
        slug (Union[Unset, str]): URL slug for the athlete
        headshot (Union[Unset, RosterAthleteHeadshot]):
        jersey (Union[Unset, str]): Athlete's jersey number
        position (Union[Unset, Position]):
        injuries (Union[Unset, List['Injury']]): Current injuries for the athlete
        teams (Union[Unset, List['RosterAthleteTeamsItem']]): Teams associated with the athlete
        contracts (Union[Unset, List['RosterAthleteContractsItem']]): Contract information
        experience (Union[Unset, RosterAthleteExperience]):
        status (Union[Unset, RosterAthleteStatus]):
    """

    id: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    alternate_ids: Union[Unset, "RosterAthleteAlternateIds"] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    weight: Union[Unset, float] = UNSET
    display_weight: Union[Unset, str] = UNSET
    height: Union[Unset, float] = UNSET
    display_height: Union[Unset, str] = UNSET
    age: Union[Unset, int] = UNSET
    date_of_birth: Union[Unset, datetime.datetime] = UNSET
    birth_place: Union[Unset, "RosterAthleteBirthPlace"] = UNSET
    links: Union[Unset, List["Link"]] = UNSET
    college: Union[Unset, "College"] = UNSET
    slug: Union[Unset, str] = UNSET
    headshot: Union[Unset, "RosterAthleteHeadshot"] = UNSET
    jersey: Union[Unset, str] = UNSET
    position: Union[Unset, "Position"] = UNSET
    injuries: Union[Unset, List["Injury"]] = UNSET
    teams: Union[Unset, List["RosterAthleteTeamsItem"]] = UNSET
    contracts: Union[Unset, List["RosterAthleteContractsItem"]] = UNSET
    experience: Union[Unset, "RosterAthleteExperience"] = UNSET
    status: Union[Unset, "RosterAthleteStatus"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        uid = self.uid

        guid = self.guid

        alternate_ids: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.alternate_ids, Unset):
            alternate_ids = self.alternate_ids.to_dict()

        first_name = self.first_name

        last_name = self.last_name

        full_name = self.full_name

        display_name = self.display_name

        short_name = self.short_name

        weight = self.weight

        display_weight = self.display_weight

        height = self.height

        display_height = self.display_height

        age = self.age

        date_of_birth: Union[Unset, str] = UNSET
        if not isinstance(self.date_of_birth, Unset):
            date_of_birth = self.date_of_birth.isoformat()

        birth_place: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.birth_place, Unset):
            birth_place = self.birth_place.to_dict()

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        college: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.college, Unset):
            college = self.college.to_dict()

        slug = self.slug

        headshot: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headshot, Unset):
            headshot = self.headshot.to_dict()

        jersey = self.jersey

        position: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        injuries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.injuries, Unset):
            injuries = []
            for injuries_item_data in self.injuries:
                injuries_item = injuries_item_data.to_dict()
                injuries.append(injuries_item)

        teams: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item = teams_item_data.to_dict()
                teams.append(teams_item)

        contracts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.contracts, Unset):
            contracts = []
            for contracts_item_data in self.contracts:
                contracts_item = contracts_item_data.to_dict()
                contracts.append(contracts_item)

        experience: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.experience, Unset):
            experience = self.experience.to_dict()

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uid is not UNSET:
            field_dict["uid"] = uid
        if guid is not UNSET:
            field_dict["guid"] = guid
        if alternate_ids is not UNSET:
            field_dict["alternateIds"] = alternate_ids
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if weight is not UNSET:
            field_dict["weight"] = weight
        if display_weight is not UNSET:
            field_dict["displayWeight"] = display_weight
        if height is not UNSET:
            field_dict["height"] = height
        if display_height is not UNSET:
            field_dict["displayHeight"] = display_height
        if age is not UNSET:
            field_dict["age"] = age
        if date_of_birth is not UNSET:
            field_dict["dateOfBirth"] = date_of_birth
        if birth_place is not UNSET:
            field_dict["birthPlace"] = birth_place
        if links is not UNSET:
            field_dict["links"] = links
        if college is not UNSET:
            field_dict["college"] = college
        if slug is not UNSET:
            field_dict["slug"] = slug
        if headshot is not UNSET:
            field_dict["headshot"] = headshot
        if jersey is not UNSET:
            field_dict["jersey"] = jersey
        if position is not UNSET:
            field_dict["position"] = position
        if injuries is not UNSET:
            field_dict["injuries"] = injuries
        if teams is not UNSET:
            field_dict["teams"] = teams
        if contracts is not UNSET:
            field_dict["contracts"] = contracts
        if experience is not UNSET:
            field_dict["experience"] = experience
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.college import College
        from ..models.injury import Injury
        from ..models.link import Link
        from ..models.position import Position
        from ..models.roster_athlete_alternate_ids import RosterAthleteAlternateIds
        from ..models.roster_athlete_birth_place import RosterAthleteBirthPlace
        from ..models.roster_athlete_contracts_item import RosterAthleteContractsItem
        from ..models.roster_athlete_experience import RosterAthleteExperience
        from ..models.roster_athlete_headshot import RosterAthleteHeadshot
        from ..models.roster_athlete_status import RosterAthleteStatus
        from ..models.roster_athlete_teams_item import RosterAthleteTeamsItem

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        uid = d.pop("uid", UNSET)

        guid = d.pop("guid", UNSET)

        _alternate_ids = d.pop("alternateIds", UNSET)
        alternate_ids: Union[Unset, RosterAthleteAlternateIds]
        if isinstance(_alternate_ids, Unset):
            alternate_ids = UNSET
        else:
            alternate_ids = RosterAthleteAlternateIds.from_dict(_alternate_ids)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        full_name = d.pop("fullName", UNSET)

        display_name = d.pop("displayName", UNSET)

        short_name = d.pop("shortName", UNSET)

        weight = d.pop("weight", UNSET)

        display_weight = d.pop("displayWeight", UNSET)

        height = d.pop("height", UNSET)

        display_height = d.pop("displayHeight", UNSET)

        age = d.pop("age", UNSET)

        _date_of_birth = d.pop("dateOfBirth", UNSET)
        date_of_birth: Union[Unset, datetime.datetime]
        if isinstance(_date_of_birth, Unset):
            date_of_birth = UNSET
        else:
            date_of_birth = isoparse(_date_of_birth)

        _birth_place = d.pop("birthPlace", UNSET)
        birth_place: Union[Unset, RosterAthleteBirthPlace]
        if isinstance(_birth_place, Unset):
            birth_place = UNSET
        else:
            birth_place = RosterAthleteBirthPlace.from_dict(_birth_place)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        _college = d.pop("college", UNSET)
        college: Union[Unset, College]
        if isinstance(_college, Unset):
            college = UNSET
        else:
            college = College.from_dict(_college)

        slug = d.pop("slug", UNSET)

        _headshot = d.pop("headshot", UNSET)
        headshot: Union[Unset, RosterAthleteHeadshot]
        if isinstance(_headshot, Unset):
            headshot = UNSET
        else:
            headshot = RosterAthleteHeadshot.from_dict(_headshot)

        jersey = d.pop("jersey", UNSET)

        _position = d.pop("position", UNSET)
        position: Union[Unset, Position]
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = Position.from_dict(_position)

        injuries = []
        _injuries = d.pop("injuries", UNSET)
        for injuries_item_data in _injuries or []:
            injuries_item = Injury.from_dict(injuries_item_data)

            injuries.append(injuries_item)

        teams = []
        _teams = d.pop("teams", UNSET)
        for teams_item_data in _teams or []:
            teams_item = RosterAthleteTeamsItem.from_dict(teams_item_data)

            teams.append(teams_item)

        contracts = []
        _contracts = d.pop("contracts", UNSET)
        for contracts_item_data in _contracts or []:
            contracts_item = RosterAthleteContractsItem.from_dict(contracts_item_data)

            contracts.append(contracts_item)

        _experience = d.pop("experience", UNSET)
        experience: Union[Unset, RosterAthleteExperience]
        if isinstance(_experience, Unset):
            experience = UNSET
        else:
            experience = RosterAthleteExperience.from_dict(_experience)

        _status = d.pop("status", UNSET)
        status: Union[Unset, RosterAthleteStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RosterAthleteStatus.from_dict(_status)

        roster_athlete = cls(
            id=id,
            uid=uid,
            guid=guid,
            alternate_ids=alternate_ids,
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            display_name=display_name,
            short_name=short_name,
            weight=weight,
            display_weight=display_weight,
            height=height,
            display_height=display_height,
            age=age,
            date_of_birth=date_of_birth,
            birth_place=birth_place,
            links=links,
            college=college,
            slug=slug,
            headshot=headshot,
            jersey=jersey,
            position=position,
            injuries=injuries,
            teams=teams,
            contracts=contracts,
            experience=experience,
            status=status,
        )

        roster_athlete.additional_properties = d
        return roster_athlete

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
