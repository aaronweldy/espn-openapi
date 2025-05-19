import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.mlb_roster_athlete_alternate_ids import MlbRosterAthleteAlternateIds
    from ..models.mlb_roster_athlete_bats import MlbRosterAthleteBats
    from ..models.mlb_roster_athlete_birth_place import MlbRosterAthleteBirthPlace
    from ..models.mlb_roster_athlete_college import MlbRosterAthleteCollege
    from ..models.mlb_roster_athlete_contracts_item import MlbRosterAthleteContractsItem
    from ..models.mlb_roster_athlete_experience import MlbRosterAthleteExperience
    from ..models.mlb_roster_athlete_headshot import MlbRosterAthleteHeadshot
    from ..models.mlb_roster_athlete_injuries_item import MlbRosterAthleteInjuriesItem
    from ..models.mlb_roster_athlete_position import MlbRosterAthletePosition
    from ..models.mlb_roster_athlete_positions_item import MlbRosterAthletePositionsItem
    from ..models.mlb_roster_athlete_status import MlbRosterAthleteStatus
    from ..models.mlb_roster_athlete_teams_item import MlbRosterAthleteTeamsItem
    from ..models.mlb_roster_athlete_throws import MlbRosterAthleteThrows


T = TypeVar("T", bound="MlbRosterAthlete")


@_attrs_define
class MlbRosterAthlete:
    """Athlete information for MLB team roster

    Attributes:
        id (str):
        uid (str):
        guid (str):
        first_name (str):
        last_name (str):
        full_name (str):
        display_name (str):
        short_name (str):
        weight (int):
        display_weight (str):
        height (int):
        display_height (str):
        age (int):
        date_of_birth (datetime.datetime):
        links (List['Link']):
        slug (str):
        headshot (MlbRosterAthleteHeadshot):
        jersey (str):
        position (MlbRosterAthletePosition):
        positions (List['MlbRosterAthletePositionsItem']):
        injuries (List['MlbRosterAthleteInjuriesItem']):
        teams (List['MlbRosterAthleteTeamsItem']):
        contracts (List['MlbRosterAthleteContractsItem']):
        experience (MlbRosterAthleteExperience):
        status (MlbRosterAthleteStatus):
        bats (MlbRosterAthleteBats):
        throws (MlbRosterAthleteThrows):
        alternate_ids (Union[Unset, MlbRosterAthleteAlternateIds]):
        nickname (Union[Unset, str]):
        debut_year (Union[Unset, int]):
        birth_place (Union[Unset, MlbRosterAthleteBirthPlace]):
        college (Union[Unset, MlbRosterAthleteCollege]):
    """

    id: str
    uid: str
    guid: str
    first_name: str
    last_name: str
    full_name: str
    display_name: str
    short_name: str
    weight: int
    display_weight: str
    height: int
    display_height: str
    age: int
    date_of_birth: datetime.datetime
    links: List["Link"]
    slug: str
    headshot: "MlbRosterAthleteHeadshot"
    jersey: str
    position: "MlbRosterAthletePosition"
    positions: List["MlbRosterAthletePositionsItem"]
    injuries: List["MlbRosterAthleteInjuriesItem"]
    teams: List["MlbRosterAthleteTeamsItem"]
    contracts: List["MlbRosterAthleteContractsItem"]
    experience: "MlbRosterAthleteExperience"
    status: "MlbRosterAthleteStatus"
    bats: "MlbRosterAthleteBats"
    throws: "MlbRosterAthleteThrows"
    alternate_ids: Union[Unset, "MlbRosterAthleteAlternateIds"] = UNSET
    nickname: Union[Unset, str] = UNSET
    debut_year: Union[Unset, int] = UNSET
    birth_place: Union[Unset, "MlbRosterAthleteBirthPlace"] = UNSET
    college: Union[Unset, "MlbRosterAthleteCollege"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        uid = self.uid

        guid = self.guid

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

        date_of_birth = self.date_of_birth.isoformat()

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        slug = self.slug

        headshot = self.headshot.to_dict()

        jersey = self.jersey

        position = self.position.to_dict()

        positions = []
        for positions_item_data in self.positions:
            positions_item = positions_item_data.to_dict()
            positions.append(positions_item)

        injuries = []
        for injuries_item_data in self.injuries:
            injuries_item = injuries_item_data.to_dict()
            injuries.append(injuries_item)

        teams = []
        for teams_item_data in self.teams:
            teams_item = teams_item_data.to_dict()
            teams.append(teams_item)

        contracts = []
        for contracts_item_data in self.contracts:
            contracts_item = contracts_item_data.to_dict()
            contracts.append(contracts_item)

        experience = self.experience.to_dict()

        status = self.status.to_dict()

        bats = self.bats.to_dict()

        throws = self.throws.to_dict()

        alternate_ids: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.alternate_ids, Unset):
            alternate_ids = self.alternate_ids.to_dict()

        nickname = self.nickname

        debut_year = self.debut_year

        birth_place: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.birth_place, Unset):
            birth_place = self.birth_place.to_dict()

        college: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.college, Unset):
            college = self.college.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uid": uid,
                "guid": guid,
                "firstName": first_name,
                "lastName": last_name,
                "fullName": full_name,
                "displayName": display_name,
                "shortName": short_name,
                "weight": weight,
                "displayWeight": display_weight,
                "height": height,
                "displayHeight": display_height,
                "age": age,
                "dateOfBirth": date_of_birth,
                "links": links,
                "slug": slug,
                "headshot": headshot,
                "jersey": jersey,
                "position": position,
                "positions": positions,
                "injuries": injuries,
                "teams": teams,
                "contracts": contracts,
                "experience": experience,
                "status": status,
                "bats": bats,
                "throws": throws,
            }
        )
        if alternate_ids is not UNSET:
            field_dict["alternateIds"] = alternate_ids
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if debut_year is not UNSET:
            field_dict["debutYear"] = debut_year
        if birth_place is not UNSET:
            field_dict["birthPlace"] = birth_place
        if college is not UNSET:
            field_dict["college"] = college

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link import Link
        from ..models.mlb_roster_athlete_alternate_ids import MlbRosterAthleteAlternateIds
        from ..models.mlb_roster_athlete_bats import MlbRosterAthleteBats
        from ..models.mlb_roster_athlete_birth_place import MlbRosterAthleteBirthPlace
        from ..models.mlb_roster_athlete_college import MlbRosterAthleteCollege
        from ..models.mlb_roster_athlete_contracts_item import MlbRosterAthleteContractsItem
        from ..models.mlb_roster_athlete_experience import MlbRosterAthleteExperience
        from ..models.mlb_roster_athlete_headshot import MlbRosterAthleteHeadshot
        from ..models.mlb_roster_athlete_injuries_item import MlbRosterAthleteInjuriesItem
        from ..models.mlb_roster_athlete_position import MlbRosterAthletePosition
        from ..models.mlb_roster_athlete_positions_item import MlbRosterAthletePositionsItem
        from ..models.mlb_roster_athlete_status import MlbRosterAthleteStatus
        from ..models.mlb_roster_athlete_teams_item import MlbRosterAthleteTeamsItem
        from ..models.mlb_roster_athlete_throws import MlbRosterAthleteThrows

        d = src_dict.copy()
        id = d.pop("id")

        uid = d.pop("uid")

        guid = d.pop("guid")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        full_name = d.pop("fullName")

        display_name = d.pop("displayName")

        short_name = d.pop("shortName")

        weight = d.pop("weight")

        display_weight = d.pop("displayWeight")

        height = d.pop("height")

        display_height = d.pop("displayHeight")

        age = d.pop("age")

        date_of_birth = isoparse(d.pop("dateOfBirth"))

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        slug = d.pop("slug")

        headshot = MlbRosterAthleteHeadshot.from_dict(d.pop("headshot"))

        jersey = d.pop("jersey")

        position = MlbRosterAthletePosition.from_dict(d.pop("position"))

        positions = []
        _positions = d.pop("positions")
        for positions_item_data in _positions:
            positions_item = MlbRosterAthletePositionsItem.from_dict(positions_item_data)

            positions.append(positions_item)

        injuries = []
        _injuries = d.pop("injuries")
        for injuries_item_data in _injuries:
            injuries_item = MlbRosterAthleteInjuriesItem.from_dict(injuries_item_data)

            injuries.append(injuries_item)

        teams = []
        _teams = d.pop("teams")
        for teams_item_data in _teams:
            teams_item = MlbRosterAthleteTeamsItem.from_dict(teams_item_data)

            teams.append(teams_item)

        contracts = []
        _contracts = d.pop("contracts")
        for contracts_item_data in _contracts:
            contracts_item = MlbRosterAthleteContractsItem.from_dict(contracts_item_data)

            contracts.append(contracts_item)

        experience = MlbRosterAthleteExperience.from_dict(d.pop("experience"))

        status = MlbRosterAthleteStatus.from_dict(d.pop("status"))

        bats = MlbRosterAthleteBats.from_dict(d.pop("bats"))

        throws = MlbRosterAthleteThrows.from_dict(d.pop("throws"))

        _alternate_ids = d.pop("alternateIds", UNSET)
        alternate_ids: Union[Unset, MlbRosterAthleteAlternateIds]
        if isinstance(_alternate_ids, Unset):
            alternate_ids = UNSET
        else:
            alternate_ids = MlbRosterAthleteAlternateIds.from_dict(_alternate_ids)

        nickname = d.pop("nickname", UNSET)

        debut_year = d.pop("debutYear", UNSET)

        _birth_place = d.pop("birthPlace", UNSET)
        birth_place: Union[Unset, MlbRosterAthleteBirthPlace]
        if isinstance(_birth_place, Unset):
            birth_place = UNSET
        else:
            birth_place = MlbRosterAthleteBirthPlace.from_dict(_birth_place)

        _college = d.pop("college", UNSET)
        college: Union[Unset, MlbRosterAthleteCollege]
        if isinstance(_college, Unset):
            college = UNSET
        else:
            college = MlbRosterAthleteCollege.from_dict(_college)

        mlb_roster_athlete = cls(
            id=id,
            uid=uid,
            guid=guid,
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
            links=links,
            slug=slug,
            headshot=headshot,
            jersey=jersey,
            position=position,
            positions=positions,
            injuries=injuries,
            teams=teams,
            contracts=contracts,
            experience=experience,
            status=status,
            bats=bats,
            throws=throws,
            alternate_ids=alternate_ids,
            nickname=nickname,
            debut_year=debut_year,
            birth_place=birth_place,
            college=college,
        )

        mlb_roster_athlete.additional_properties = d
        return mlb_roster_athlete

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
