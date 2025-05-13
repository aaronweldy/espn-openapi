import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.athlete_details_response_alternate_ids import AthleteDetailsResponseAlternateIds
    from ..models.athlete_details_response_experience import AthleteDetailsResponseExperience
    from ..models.athlete_status import AthleteStatus
    from ..models.link import Link
    from ..models.position import Position
    from ..models.reference import Reference
    from ..models.team import Team


T = TypeVar("T", bound="AthleteDetailsResponse")


@_attrs_define
class AthleteDetailsResponse:
    """
    Attributes:
        id (str):  Example: 3139477.
        uid (str):  Example: s:20~l:28~a:3139477.
        full_name (str):  Example: Patrick Mahomes.
        guid (Union[Unset, str]):  Example: 37d87523-280a-9d4a-0adb-22cfc6d3619c.
        type (Union[Unset, str]):  Example: football.
        alternate_ids (Union[Unset, AthleteDetailsResponseAlternateIds]):
        first_name (Union[Unset, str]):  Example: Patrick.
        last_name (Union[Unset, str]):  Example: Mahomes.
        display_name (Union[Unset, str]):  Example: Patrick Mahomes.
        short_name (Union[Unset, str]):  Example: P. Mahomes.
        weight (Union[Unset, float]):  Example: 225.0.
        display_weight (Union[Unset, str]):  Example: 225 lbs.
        height (Union[Unset, float]):  Example: 74.0.
        display_height (Union[Unset, str]):  Example: 6' 2".
        age (Union[Unset, int]):  Example: 29.
        date_of_birth (Union[Unset, datetime.datetime]):  Example: 1995-09-17T07:00Z.
        debut_year (Union[Unset, int]):  Example: 2017.
        links (Union[Unset, List['Link']]):
        jersey (Union[Unset, str]):  Example: 15.
        position (Union[Unset, Position]):
        team (Union['Reference', 'Team', Unset]):
        active (Union[Unset, bool]):  Example: True.
        status (Union[Unset, AthleteStatus]):
        experience (Union[Unset, AthleteDetailsResponseExperience]):
    """

    id: str
    uid: str
    full_name: str
    guid: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    alternate_ids: Union[Unset, "AthleteDetailsResponseAlternateIds"] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    weight: Union[Unset, float] = UNSET
    display_weight: Union[Unset, str] = UNSET
    height: Union[Unset, float] = UNSET
    display_height: Union[Unset, str] = UNSET
    age: Union[Unset, int] = UNSET
    date_of_birth: Union[Unset, datetime.datetime] = UNSET
    debut_year: Union[Unset, int] = UNSET
    links: Union[Unset, List["Link"]] = UNSET
    jersey: Union[Unset, str] = UNSET
    position: Union[Unset, "Position"] = UNSET
    team: Union["Reference", "Team", Unset] = UNSET
    active: Union[Unset, bool] = UNSET
    status: Union[Unset, "AthleteStatus"] = UNSET
    experience: Union[Unset, "AthleteDetailsResponseExperience"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.team import Team

        id = self.id

        uid = self.uid

        full_name = self.full_name

        guid = self.guid

        type = self.type

        alternate_ids: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.alternate_ids, Unset):
            alternate_ids = self.alternate_ids.to_dict()

        first_name = self.first_name

        last_name = self.last_name

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

        debut_year = self.debut_year

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        jersey = self.jersey

        position: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        team: Union[Dict[str, Any], Unset]
        if isinstance(self.team, Unset):
            team = UNSET
        elif isinstance(self.team, Team):
            team = self.team.to_dict()
        else:
            team = self.team.to_dict()

        active = self.active

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        experience: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.experience, Unset):
            experience = self.experience.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uid": uid,
                "fullName": full_name,
            }
        )
        if guid is not UNSET:
            field_dict["guid"] = guid
        if type is not UNSET:
            field_dict["type"] = type
        if alternate_ids is not UNSET:
            field_dict["alternateIds"] = alternate_ids
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
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
        if debut_year is not UNSET:
            field_dict["debutYear"] = debut_year
        if links is not UNSET:
            field_dict["links"] = links
        if jersey is not UNSET:
            field_dict["jersey"] = jersey
        if position is not UNSET:
            field_dict["position"] = position
        if team is not UNSET:
            field_dict["team"] = team
        if active is not UNSET:
            field_dict["active"] = active
        if status is not UNSET:
            field_dict["status"] = status
        if experience is not UNSET:
            field_dict["experience"] = experience

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.athlete_details_response_alternate_ids import AthleteDetailsResponseAlternateIds
        from ..models.athlete_details_response_experience import AthleteDetailsResponseExperience
        from ..models.athlete_status import AthleteStatus
        from ..models.link import Link
        from ..models.position import Position
        from ..models.reference import Reference
        from ..models.team import Team

        d = src_dict.copy()
        id = d.pop("id")

        uid = d.pop("uid")

        full_name = d.pop("fullName")

        guid = d.pop("guid", UNSET)

        type = d.pop("type", UNSET)

        _alternate_ids = d.pop("alternateIds", UNSET)
        alternate_ids: Union[Unset, AthleteDetailsResponseAlternateIds]
        if isinstance(_alternate_ids, Unset):
            alternate_ids = UNSET
        else:
            alternate_ids = AthleteDetailsResponseAlternateIds.from_dict(_alternate_ids)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

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

        debut_year = d.pop("debutYear", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        jersey = d.pop("jersey", UNSET)

        _position = d.pop("position", UNSET)
        position: Union[Unset, Position]
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = Position.from_dict(_position)

        def _parse_team(data: object) -> Union["Reference", "Team", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                team_type_0 = Team.from_dict(data)

                return team_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            team_type_1 = Reference.from_dict(data)

            return team_type_1

        team = _parse_team(d.pop("team", UNSET))

        active = d.pop("active", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AthleteStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AthleteStatus.from_dict(_status)

        _experience = d.pop("experience", UNSET)
        experience: Union[Unset, AthleteDetailsResponseExperience]
        if isinstance(_experience, Unset):
            experience = UNSET
        else:
            experience = AthleteDetailsResponseExperience.from_dict(_experience)

        athlete_details_response = cls(
            id=id,
            uid=uid,
            full_name=full_name,
            guid=guid,
            type=type,
            alternate_ids=alternate_ids,
            first_name=first_name,
            last_name=last_name,
            display_name=display_name,
            short_name=short_name,
            weight=weight,
            display_weight=display_weight,
            height=height,
            display_height=display_height,
            age=age,
            date_of_birth=date_of_birth,
            debut_year=debut_year,
            links=links,
            jersey=jersey,
            position=position,
            team=team,
            active=active,
            status=status,
            experience=experience,
        )

        athlete_details_response.additional_properties = d
        return athlete_details_response

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
