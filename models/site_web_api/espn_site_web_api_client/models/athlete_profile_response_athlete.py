from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.athlete_profile_response_athlete_college import AthleteProfileResponseAthleteCollege
    from ..models.headshot import Headshot
    from ..models.position import Position
    from ..models.status import Status
    from ..models.team import Team


T = TypeVar("T", bound="AthleteProfileResponseAthlete")


@_attrs_define
class AthleteProfileResponseAthlete:
    """
    Attributes:
        id (str):
        uid (str):
        guid (str):
        type (str):
        first_name (str):
        last_name (str):
        display_name (str):
        full_name (str):
        jersey (str):
        position (Position):
        age (int):
        display_height (str):
        display_weight (str):
        college (AthleteProfileResponseAthleteCollege):
        team (Team):
        headshot (Headshot):
        status (Status):
    """

    id: str
    uid: str
    guid: str
    type: str
    first_name: str
    last_name: str
    display_name: str
    full_name: str
    jersey: str
    position: "Position"
    age: int
    display_height: str
    display_weight: str
    college: "AthleteProfileResponseAthleteCollege"
    team: "Team"
    headshot: "Headshot"
    status: "Status"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        uid = self.uid

        guid = self.guid

        type = self.type

        first_name = self.first_name

        last_name = self.last_name

        display_name = self.display_name

        full_name = self.full_name

        jersey = self.jersey

        position = self.position.to_dict()

        age = self.age

        display_height = self.display_height

        display_weight = self.display_weight

        college = self.college.to_dict()

        team = self.team.to_dict()

        headshot = self.headshot.to_dict()

        status = self.status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uid": uid,
                "guid": guid,
                "type": type,
                "firstName": first_name,
                "lastName": last_name,
                "displayName": display_name,
                "fullName": full_name,
                "jersey": jersey,
                "position": position,
                "age": age,
                "displayHeight": display_height,
                "displayWeight": display_weight,
                "college": college,
                "team": team,
                "headshot": headshot,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.athlete_profile_response_athlete_college import AthleteProfileResponseAthleteCollege
        from ..models.headshot import Headshot
        from ..models.position import Position
        from ..models.status import Status
        from ..models.team import Team

        d = src_dict.copy()
        id = d.pop("id")

        uid = d.pop("uid")

        guid = d.pop("guid")

        type = d.pop("type")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        display_name = d.pop("displayName")

        full_name = d.pop("fullName")

        jersey = d.pop("jersey")

        position = Position.from_dict(d.pop("position"))

        age = d.pop("age")

        display_height = d.pop("displayHeight")

        display_weight = d.pop("displayWeight")

        college = AthleteProfileResponseAthleteCollege.from_dict(d.pop("college"))

        team = Team.from_dict(d.pop("team"))

        headshot = Headshot.from_dict(d.pop("headshot"))

        status = Status.from_dict(d.pop("status"))

        athlete_profile_response_athlete = cls(
            id=id,
            uid=uid,
            guid=guid,
            type=type,
            first_name=first_name,
            last_name=last_name,
            display_name=display_name,
            full_name=full_name,
            jersey=jersey,
            position=position,
            age=age,
            display_height=display_height,
            display_weight=display_weight,
            college=college,
            team=team,
            headshot=headshot,
            status=status,
        )

        athlete_profile_response_athlete.additional_properties = d
        return athlete_profile_response_athlete

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
