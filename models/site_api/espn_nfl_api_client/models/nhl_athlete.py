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
        first_name (str):
        last_name (str):
        full_name (str):
        display_name (str):
        uid (Union[Unset, str]):
        guid (Union[Unset, str]):
        short_name (Union[Unset, str]):
        weight (Union[Unset, float]):
        display_weight (Union[Unset, str]):
        height (Union[Unset, float]):
        display_height (Union[Unset, str]):
        age (Union[Unset, int]):
        date_of_birth (Union[Unset, datetime.datetime]):
        links (Union[Unset, List['Link']]):
        slug (Union[Unset, str]):
        headshot (Union[Unset, Headshot]):
        jersey (Union[Unset, str]):
        position (Union[Unset, NhlAthletePosition]):
        positions (Union[Unset, List['NhlAthletePositionsItem']]):
        injuries (Union[Unset, List['NhlAthleteInjuriesItem']]):
        teams (Union[Unset, List['NhlAthleteTeamsItem']]):
        contracts (Union[Unset, List['NhlAthleteContractsItem']]):
        experience (Union[Unset, NhlAthleteExperience]):
        status (Union[Unset, NhlAthleteStatus]):
        shoots (Union[Unset, NhlAthleteShoots]):
        catches (Union[Unset, NhlAthleteCatches]):
        college (Union[Unset, NhlAthleteCollege]):
    """

    id: str
    first_name: str
    last_name: str
    full_name: str
    display_name: str
    uid: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    weight: Union[Unset, float] = UNSET
    display_weight: Union[Unset, str] = UNSET
    height: Union[Unset, float] = UNSET
    display_height: Union[Unset, str] = UNSET
    age: Union[Unset, int] = UNSET
    date_of_birth: Union[Unset, datetime.datetime] = UNSET
    links: Union[Unset, List["Link"]] = UNSET
    slug: Union[Unset, str] = UNSET
    headshot: Union[Unset, "Headshot"] = UNSET
    jersey: Union[Unset, str] = UNSET
    position: Union[Unset, "NhlAthletePosition"] = UNSET
    positions: Union[Unset, List["NhlAthletePositionsItem"]] = UNSET
    injuries: Union[Unset, List["NhlAthleteInjuriesItem"]] = UNSET
    teams: Union[Unset, List["NhlAthleteTeamsItem"]] = UNSET
    contracts: Union[Unset, List["NhlAthleteContractsItem"]] = UNSET
    experience: Union[Unset, "NhlAthleteExperience"] = UNSET
    status: Union[Unset, "NhlAthleteStatus"] = UNSET
    shoots: Union[Unset, "NhlAthleteShoots"] = UNSET
    catches: Union[Unset, "NhlAthleteCatches"] = UNSET
    college: Union[Unset, "NhlAthleteCollege"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        first_name = self.first_name

        last_name = self.last_name

        full_name = self.full_name

        display_name = self.display_name

        uid = self.uid

        guid = self.guid

        short_name = self.short_name

        weight = self.weight

        display_weight = self.display_weight

        height = self.height

        display_height = self.display_height

        age = self.age

        date_of_birth: Union[Unset, str] = UNSET
        if not isinstance(self.date_of_birth, Unset):
            date_of_birth = self.date_of_birth.isoformat()

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        slug = self.slug

        headshot: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headshot, Unset):
            headshot = self.headshot.to_dict()

        jersey = self.jersey

        position: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        positions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.positions, Unset):
            positions = []
            for positions_item_data in self.positions:
                positions_item = positions_item_data.to_dict()
                positions.append(positions_item)

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
                "firstName": first_name,
                "lastName": last_name,
                "fullName": full_name,
                "displayName": display_name,
            }
        )
        if uid is not UNSET:
            field_dict["uid"] = uid
        if guid is not UNSET:
            field_dict["guid"] = guid
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
        if links is not UNSET:
            field_dict["links"] = links
        if slug is not UNSET:
            field_dict["slug"] = slug
        if headshot is not UNSET:
            field_dict["headshot"] = headshot
        if jersey is not UNSET:
            field_dict["jersey"] = jersey
        if position is not UNSET:
            field_dict["position"] = position
        if positions is not UNSET:
            field_dict["positions"] = positions
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

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        full_name = d.pop("fullName")

        display_name = d.pop("displayName")

        uid = d.pop("uid", UNSET)

        guid = d.pop("guid", UNSET)

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

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        slug = d.pop("slug", UNSET)

        _headshot = d.pop("headshot", UNSET)
        headshot: Union[Unset, Headshot]
        if isinstance(_headshot, Unset):
            headshot = UNSET
        else:
            headshot = Headshot.from_dict(_headshot)

        jersey = d.pop("jersey", UNSET)

        _position = d.pop("position", UNSET)
        position: Union[Unset, NhlAthletePosition]
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = NhlAthletePosition.from_dict(_position)

        positions = []
        _positions = d.pop("positions", UNSET)
        for positions_item_data in _positions or []:
            positions_item = NhlAthletePositionsItem.from_dict(positions_item_data)

            positions.append(positions_item)

        injuries = []
        _injuries = d.pop("injuries", UNSET)
        for injuries_item_data in _injuries or []:
            injuries_item = NhlAthleteInjuriesItem.from_dict(injuries_item_data)

            injuries.append(injuries_item)

        teams = []
        _teams = d.pop("teams", UNSET)
        for teams_item_data in _teams or []:
            teams_item = NhlAthleteTeamsItem.from_dict(teams_item_data)

            teams.append(teams_item)

        contracts = []
        _contracts = d.pop("contracts", UNSET)
        for contracts_item_data in _contracts or []:
            contracts_item = NhlAthleteContractsItem.from_dict(contracts_item_data)

            contracts.append(contracts_item)

        _experience = d.pop("experience", UNSET)
        experience: Union[Unset, NhlAthleteExperience]
        if isinstance(_experience, Unset):
            experience = UNSET
        else:
            experience = NhlAthleteExperience.from_dict(_experience)

        _status = d.pop("status", UNSET)
        status: Union[Unset, NhlAthleteStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = NhlAthleteStatus.from_dict(_status)

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
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            display_name=display_name,
            uid=uid,
            guid=guid,
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
