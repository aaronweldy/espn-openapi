import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.headshot import Headshot
    from ..models.link import Link
    from ..models.nhl_athlete_catches import NhlAthleteCatches
    from ..models.nhl_athlete_college import NhlAthleteCollege
    from ..models.nhl_athlete_contracts_item import NhlAthleteContractsItem
    from ..models.nhl_athlete_experience import NhlAthleteExperience
    from ..models.nhl_athlete_injuries_item import NhlAthleteInjuriesItem
    from ..models.nhl_athlete_position import NhlAthletePosition
    from ..models.nhl_athlete_positions_item import NhlAthletePositionsItem
    from ..models.nhl_athlete_shoots import NhlAthleteShoots
    from ..models.nhl_athlete_status import NhlAthleteStatus
    from ..models.nhl_athlete_teams_item import NhlAthleteTeamsItem


T = TypeVar("T", bound="NhlAthlete")


@_attrs_define
class NhlAthlete:
    """NHL athlete information for roster

    Attributes:
        id (str):
        uid (str):
        guid (str):
        first_name (str):
        last_name (str):
        full_name (str):
        display_name (str):
        short_name (str):
        weight (float):
        display_weight (str):
        height (float):
        display_height (str):
        age (int):
        date_of_birth (datetime.datetime):
        links (List['Link']):
        slug (str):
        headshot (Headshot):
        jersey (str):
        position (NhlAthletePosition):
        positions (List['NhlAthletePositionsItem']):
        injuries (List['NhlAthleteInjuriesItem']):
        teams (List['NhlAthleteTeamsItem']):
        contracts (List['NhlAthleteContractsItem']):
        experience (NhlAthleteExperience):
        status (NhlAthleteStatus):
        shoots (Union[Unset, NhlAthleteShoots]):
        catches (Union[Unset, NhlAthleteCatches]):
        college (Union[Unset, NhlAthleteCollege]):
    """

    id: str
    uid: str
    guid: str
    first_name: str
    last_name: str
    full_name: str
    display_name: str
    short_name: str
    weight: float
    display_weight: str
    height: float
    display_height: str
    age: int
    date_of_birth: datetime.datetime
    links: List["Link"]
    slug: str
    headshot: "Headshot"
    jersey: str
    position: "NhlAthletePosition"
    positions: List["NhlAthletePositionsItem"]
    injuries: List["NhlAthleteInjuriesItem"]
    teams: List["NhlAthleteTeamsItem"]
    contracts: List["NhlAthleteContractsItem"]
    experience: "NhlAthleteExperience"
    status: "NhlAthleteStatus"
    shoots: Union[Unset, "NhlAthleteShoots"] = UNSET
    catches: Union[Unset, "NhlAthleteCatches"] = UNSET
    college: Union[Unset, "NhlAthleteCollege"] = UNSET
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

        shoots: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shoots, Unset):
            shoots = self.shoots.to_dict()

        catches: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.catches, Unset):
            catches = self.catches.to_dict()

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
            }
        )
        if shoots is not UNSET:
            field_dict["shoots"] = shoots
        if catches is not UNSET:
            field_dict["catches"] = catches
        if college is not UNSET:
            field_dict["college"] = college

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.headshot import Headshot
        from ..models.link import Link
        from ..models.nhl_athlete_catches import NhlAthleteCatches
        from ..models.nhl_athlete_college import NhlAthleteCollege
        from ..models.nhl_athlete_contracts_item import NhlAthleteContractsItem
        from ..models.nhl_athlete_experience import NhlAthleteExperience
        from ..models.nhl_athlete_injuries_item import NhlAthleteInjuriesItem
        from ..models.nhl_athlete_position import NhlAthletePosition
        from ..models.nhl_athlete_positions_item import NhlAthletePositionsItem
        from ..models.nhl_athlete_shoots import NhlAthleteShoots
        from ..models.nhl_athlete_status import NhlAthleteStatus
        from ..models.nhl_athlete_teams_item import NhlAthleteTeamsItem

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

        headshot = Headshot.from_dict(d.pop("headshot"))

        jersey = d.pop("jersey")

        position = NhlAthletePosition.from_dict(d.pop("position"))

        positions = []
        _positions = d.pop("positions")
        for positions_item_data in _positions:
            positions_item = NhlAthletePositionsItem.from_dict(positions_item_data)

            positions.append(positions_item)

        injuries = []
        _injuries = d.pop("injuries")
        for injuries_item_data in _injuries:
            injuries_item = NhlAthleteInjuriesItem.from_dict(injuries_item_data)

            injuries.append(injuries_item)

        teams = []
        _teams = d.pop("teams")
        for teams_item_data in _teams:
            teams_item = NhlAthleteTeamsItem.from_dict(teams_item_data)

            teams.append(teams_item)

        contracts = []
        _contracts = d.pop("contracts")
        for contracts_item_data in _contracts:
            contracts_item = NhlAthleteContractsItem.from_dict(contracts_item_data)

            contracts.append(contracts_item)

        experience = NhlAthleteExperience.from_dict(d.pop("experience"))

        status = NhlAthleteStatus.from_dict(d.pop("status"))

        _shoots = d.pop("shoots", UNSET)
        shoots: Union[Unset, NhlAthleteShoots]
        if isinstance(_shoots, Unset):
            shoots = UNSET
        else:
            shoots = NhlAthleteShoots.from_dict(_shoots)

        _catches = d.pop("catches", UNSET)
        catches: Union[Unset, NhlAthleteCatches]
        if isinstance(_catches, Unset):
            catches = UNSET
        else:
            catches = NhlAthleteCatches.from_dict(_catches)

        _college = d.pop("college", UNSET)
        college: Union[Unset, NhlAthleteCollege]
        if isinstance(_college, Unset):
            college = UNSET
        else:
            college = NhlAthleteCollege.from_dict(_college)

        nhl_athlete = cls(
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
            shoots=shoots,
            catches=catches,
            college=college,
        )

        nhl_athlete.additional_properties = d
        return nhl_athlete

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
