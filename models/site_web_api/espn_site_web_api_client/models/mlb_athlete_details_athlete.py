from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.mlb_athlete_details_athlete_college import MLBAthleteDetailsAthleteCollege
    from ..models.mlb_athlete_details_athlete_headshot import MLBAthleteDetailsAthleteHeadshot
    from ..models.mlb_athlete_details_athlete_position import MLBAthleteDetailsAthletePosition
    from ..models.mlb_athlete_details_athlete_stats_summary import MLBAthleteDetailsAthleteStatsSummary
    from ..models.mlb_athlete_details_athlete_status import MLBAthleteDetailsAthleteStatus
    from ..models.mlb_athlete_details_athlete_team import MLBAthleteDetailsAthleteTeam


T = TypeVar("T", bound="MLBAthleteDetailsAthlete")


@_attrs_define
class MLBAthleteDetailsAthlete:
    """MLB athlete details (athlete object) from site.web.api.espn.com

    Attributes:
        id (str):
        uid (str):
        guid (str):
        type (str):
        first_name (str):
        last_name (str):
        display_name (str):
        full_name (str):
        debut_year (int):
        jersey (str):
        links (List['Link']):
        college (MLBAthleteDetailsAthleteCollege):
        headshot (MLBAthleteDetailsAthleteHeadshot):
        position (MLBAthleteDetailsAthletePosition):
        team (MLBAthleteDetailsAthleteTeam):
        active (bool):
        status (MLBAthleteDetailsAthleteStatus):
        stats_summary (MLBAthleteDetailsAthleteStatsSummary):
        display_birth_place (str):
        display_height (str):
        display_weight (str):
        display_dob (str):
        age (int):
        display_jersey (str):
        display_experience (str):
        display_draft (str):
        display_bats_throws (str):
    """

    id: str
    uid: str
    guid: str
    type: str
    first_name: str
    last_name: str
    display_name: str
    full_name: str
    debut_year: int
    jersey: str
    links: List["Link"]
    college: "MLBAthleteDetailsAthleteCollege"
    headshot: "MLBAthleteDetailsAthleteHeadshot"
    position: "MLBAthleteDetailsAthletePosition"
    team: "MLBAthleteDetailsAthleteTeam"
    active: bool
    status: "MLBAthleteDetailsAthleteStatus"
    stats_summary: "MLBAthleteDetailsAthleteStatsSummary"
    display_birth_place: str
    display_height: str
    display_weight: str
    display_dob: str
    age: int
    display_jersey: str
    display_experience: str
    display_draft: str
    display_bats_throws: str
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

        debut_year = self.debut_year

        jersey = self.jersey

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        college = self.college.to_dict()

        headshot = self.headshot.to_dict()

        position = self.position.to_dict()

        team = self.team.to_dict()

        active = self.active

        status = self.status.to_dict()

        stats_summary = self.stats_summary.to_dict()

        display_birth_place = self.display_birth_place

        display_height = self.display_height

        display_weight = self.display_weight

        display_dob = self.display_dob

        age = self.age

        display_jersey = self.display_jersey

        display_experience = self.display_experience

        display_draft = self.display_draft

        display_bats_throws = self.display_bats_throws

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
                "debutYear": debut_year,
                "jersey": jersey,
                "links": links,
                "college": college,
                "headshot": headshot,
                "position": position,
                "team": team,
                "active": active,
                "status": status,
                "statsSummary": stats_summary,
                "displayBirthPlace": display_birth_place,
                "displayHeight": display_height,
                "displayWeight": display_weight,
                "displayDOB": display_dob,
                "age": age,
                "displayJersey": display_jersey,
                "displayExperience": display_experience,
                "displayDraft": display_draft,
                "displayBatsThrows": display_bats_throws,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link import Link
        from ..models.mlb_athlete_details_athlete_college import MLBAthleteDetailsAthleteCollege
        from ..models.mlb_athlete_details_athlete_headshot import MLBAthleteDetailsAthleteHeadshot
        from ..models.mlb_athlete_details_athlete_position import MLBAthleteDetailsAthletePosition
        from ..models.mlb_athlete_details_athlete_stats_summary import MLBAthleteDetailsAthleteStatsSummary
        from ..models.mlb_athlete_details_athlete_status import MLBAthleteDetailsAthleteStatus
        from ..models.mlb_athlete_details_athlete_team import MLBAthleteDetailsAthleteTeam

        d = src_dict.copy()
        id = d.pop("id")

        uid = d.pop("uid")

        guid = d.pop("guid")

        type = d.pop("type")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        display_name = d.pop("displayName")

        full_name = d.pop("fullName")

        debut_year = d.pop("debutYear")

        jersey = d.pop("jersey")

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        college = MLBAthleteDetailsAthleteCollege.from_dict(d.pop("college"))

        headshot = MLBAthleteDetailsAthleteHeadshot.from_dict(d.pop("headshot"))

        position = MLBAthleteDetailsAthletePosition.from_dict(d.pop("position"))

        team = MLBAthleteDetailsAthleteTeam.from_dict(d.pop("team"))

        active = d.pop("active")

        status = MLBAthleteDetailsAthleteStatus.from_dict(d.pop("status"))

        stats_summary = MLBAthleteDetailsAthleteStatsSummary.from_dict(d.pop("statsSummary"))

        display_birth_place = d.pop("displayBirthPlace")

        display_height = d.pop("displayHeight")

        display_weight = d.pop("displayWeight")

        display_dob = d.pop("displayDOB")

        age = d.pop("age")

        display_jersey = d.pop("displayJersey")

        display_experience = d.pop("displayExperience")

        display_draft = d.pop("displayDraft")

        display_bats_throws = d.pop("displayBatsThrows")

        mlb_athlete_details_athlete = cls(
            id=id,
            uid=uid,
            guid=guid,
            type=type,
            first_name=first_name,
            last_name=last_name,
            display_name=display_name,
            full_name=full_name,
            debut_year=debut_year,
            jersey=jersey,
            links=links,
            college=college,
            headshot=headshot,
            position=position,
            team=team,
            active=active,
            status=status,
            stats_summary=stats_summary,
            display_birth_place=display_birth_place,
            display_height=display_height,
            display_weight=display_weight,
            display_dob=display_dob,
            age=age,
            display_jersey=display_jersey,
            display_experience=display_experience,
            display_draft=display_draft,
            display_bats_throws=display_bats_throws,
        )

        mlb_athlete_details_athlete.additional_properties = d
        return mlb_athlete_details_athlete

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
