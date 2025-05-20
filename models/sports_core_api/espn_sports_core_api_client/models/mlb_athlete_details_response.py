from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.mlb_athlete_details_response_alternate_ids import MlbAthleteDetailsResponseAlternateIds
    from ..models.mlb_athlete_details_response_awards import MlbAthleteDetailsResponseAwards
    from ..models.mlb_athlete_details_response_bats import MlbAthleteDetailsResponseBats
    from ..models.mlb_athlete_details_response_birth_place import MlbAthleteDetailsResponseBirthPlace
    from ..models.mlb_athlete_details_response_college import MlbAthleteDetailsResponseCollege
    from ..models.mlb_athlete_details_response_contracts import MlbAthleteDetailsResponseContracts
    from ..models.mlb_athlete_details_response_debut import MlbAthleteDetailsResponseDebut
    from ..models.mlb_athlete_details_response_draft import MlbAthleteDetailsResponseDraft
    from ..models.mlb_athlete_details_response_experience import MlbAthleteDetailsResponseExperience
    from ..models.mlb_athlete_details_response_headshot import MlbAthleteDetailsResponseHeadshot
    from ..models.mlb_athlete_details_response_links_item import MlbAthleteDetailsResponseLinksItem
    from ..models.mlb_athlete_details_response_position import MlbAthleteDetailsResponsePosition
    from ..models.mlb_athlete_details_response_statistics import MlbAthleteDetailsResponseStatistics
    from ..models.mlb_athlete_details_response_statisticslog import MlbAthleteDetailsResponseStatisticslog
    from ..models.mlb_athlete_details_response_status import MlbAthleteDetailsResponseStatus
    from ..models.mlb_athlete_details_response_team import MlbAthleteDetailsResponseTeam
    from ..models.mlb_athlete_details_response_throws import MlbAthleteDetailsResponseThrows


T = TypeVar("T", bound="MlbAthleteDetailsResponse")


@_attrs_define
class MlbAthleteDetailsResponse:
    """
    Attributes:
        ref (str):
        id (str):
        uid (str):
        guid (UUID):
        type (str):
        alternate_ids (MlbAthleteDetailsResponseAlternateIds):
        first_name (str):
        last_name (str):
        full_name (str):
        display_name (str):
        nickname (str):
        short_name (str):
        weight (float):
        display_weight (str):
        height (float):
        display_height (str):
        age (int):
        date_of_birth (str):
        debut_year (int):
        links (List['MlbAthleteDetailsResponseLinksItem']):
        birth_place (MlbAthleteDetailsResponseBirthPlace):
        college (MlbAthleteDetailsResponseCollege):
        slug (str):
        headshot (MlbAthleteDetailsResponseHeadshot):
        jersey (str):
        position (MlbAthleteDetailsResponsePosition):
        linked (bool):
        team (MlbAthleteDetailsResponseTeam):
        statistics (MlbAthleteDetailsResponseStatistics):
        contracts (MlbAthleteDetailsResponseContracts):
        experience (MlbAthleteDetailsResponseExperience):
        debut (MlbAthleteDetailsResponseDebut):
        active (bool):
        draft (MlbAthleteDetailsResponseDraft):
        status (MlbAthleteDetailsResponseStatus):
        statisticslog (MlbAthleteDetailsResponseStatisticslog):
        awards (MlbAthleteDetailsResponseAwards):
        bats (MlbAthleteDetailsResponseBats):
        throws (MlbAthleteDetailsResponseThrows):
    """

    ref: str
    id: str
    uid: str
    guid: UUID
    type: str
    alternate_ids: "MlbAthleteDetailsResponseAlternateIds"
    first_name: str
    last_name: str
    full_name: str
    display_name: str
    nickname: str
    short_name: str
    weight: float
    display_weight: str
    height: float
    display_height: str
    age: int
    date_of_birth: str
    debut_year: int
    links: List["MlbAthleteDetailsResponseLinksItem"]
    birth_place: "MlbAthleteDetailsResponseBirthPlace"
    college: "MlbAthleteDetailsResponseCollege"
    slug: str
    headshot: "MlbAthleteDetailsResponseHeadshot"
    jersey: str
    position: "MlbAthleteDetailsResponsePosition"
    linked: bool
    team: "MlbAthleteDetailsResponseTeam"
    statistics: "MlbAthleteDetailsResponseStatistics"
    contracts: "MlbAthleteDetailsResponseContracts"
    experience: "MlbAthleteDetailsResponseExperience"
    debut: "MlbAthleteDetailsResponseDebut"
    active: bool
    draft: "MlbAthleteDetailsResponseDraft"
    status: "MlbAthleteDetailsResponseStatus"
    statisticslog: "MlbAthleteDetailsResponseStatisticslog"
    awards: "MlbAthleteDetailsResponseAwards"
    bats: "MlbAthleteDetailsResponseBats"
    throws: "MlbAthleteDetailsResponseThrows"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        id = self.id

        uid = self.uid

        guid = str(self.guid)

        type = self.type

        alternate_ids = self.alternate_ids.to_dict()

        first_name = self.first_name

        last_name = self.last_name

        full_name = self.full_name

        display_name = self.display_name

        nickname = self.nickname

        short_name = self.short_name

        weight = self.weight

        display_weight = self.display_weight

        height = self.height

        display_height = self.display_height

        age = self.age

        date_of_birth = self.date_of_birth

        debut_year = self.debut_year

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        birth_place = self.birth_place.to_dict()

        college = self.college.to_dict()

        slug = self.slug

        headshot = self.headshot.to_dict()

        jersey = self.jersey

        position = self.position.to_dict()

        linked = self.linked

        team = self.team.to_dict()

        statistics = self.statistics.to_dict()

        contracts = self.contracts.to_dict()

        experience = self.experience.to_dict()

        debut = self.debut.to_dict()

        active = self.active

        draft = self.draft.to_dict()

        status = self.status.to_dict()

        statisticslog = self.statisticslog.to_dict()

        awards = self.awards.to_dict()

        bats = self.bats.to_dict()

        throws = self.throws.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "id": id,
                "uid": uid,
                "guid": guid,
                "type": type,
                "alternateIds": alternate_ids,
                "firstName": first_name,
                "lastName": last_name,
                "fullName": full_name,
                "displayName": display_name,
                "nickname": nickname,
                "shortName": short_name,
                "weight": weight,
                "displayWeight": display_weight,
                "height": height,
                "displayHeight": display_height,
                "age": age,
                "dateOfBirth": date_of_birth,
                "debutYear": debut_year,
                "links": links,
                "birthPlace": birth_place,
                "college": college,
                "slug": slug,
                "headshot": headshot,
                "jersey": jersey,
                "position": position,
                "linked": linked,
                "team": team,
                "statistics": statistics,
                "contracts": contracts,
                "experience": experience,
                "debut": debut,
                "active": active,
                "draft": draft,
                "status": status,
                "statisticslog": statisticslog,
                "awards": awards,
                "bats": bats,
                "throws": throws,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.mlb_athlete_details_response_alternate_ids import MlbAthleteDetailsResponseAlternateIds
        from ..models.mlb_athlete_details_response_awards import MlbAthleteDetailsResponseAwards
        from ..models.mlb_athlete_details_response_bats import MlbAthleteDetailsResponseBats
        from ..models.mlb_athlete_details_response_birth_place import MlbAthleteDetailsResponseBirthPlace
        from ..models.mlb_athlete_details_response_college import MlbAthleteDetailsResponseCollege
        from ..models.mlb_athlete_details_response_contracts import MlbAthleteDetailsResponseContracts
        from ..models.mlb_athlete_details_response_debut import MlbAthleteDetailsResponseDebut
        from ..models.mlb_athlete_details_response_draft import MlbAthleteDetailsResponseDraft
        from ..models.mlb_athlete_details_response_experience import MlbAthleteDetailsResponseExperience
        from ..models.mlb_athlete_details_response_headshot import MlbAthleteDetailsResponseHeadshot
        from ..models.mlb_athlete_details_response_links_item import MlbAthleteDetailsResponseLinksItem
        from ..models.mlb_athlete_details_response_position import MlbAthleteDetailsResponsePosition
        from ..models.mlb_athlete_details_response_statistics import MlbAthleteDetailsResponseStatistics
        from ..models.mlb_athlete_details_response_statisticslog import MlbAthleteDetailsResponseStatisticslog
        from ..models.mlb_athlete_details_response_status import MlbAthleteDetailsResponseStatus
        from ..models.mlb_athlete_details_response_team import MlbAthleteDetailsResponseTeam
        from ..models.mlb_athlete_details_response_throws import MlbAthleteDetailsResponseThrows

        d = src_dict.copy()
        ref = d.pop("$ref")

        id = d.pop("id")

        uid = d.pop("uid")

        guid = UUID(d.pop("guid"))

        type = d.pop("type")

        alternate_ids = MlbAthleteDetailsResponseAlternateIds.from_dict(d.pop("alternateIds"))

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        full_name = d.pop("fullName")

        display_name = d.pop("displayName")

        nickname = d.pop("nickname")

        short_name = d.pop("shortName")

        weight = d.pop("weight")

        display_weight = d.pop("displayWeight")

        height = d.pop("height")

        display_height = d.pop("displayHeight")

        age = d.pop("age")

        date_of_birth = d.pop("dateOfBirth")

        debut_year = d.pop("debutYear")

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = MlbAthleteDetailsResponseLinksItem.from_dict(links_item_data)

            links.append(links_item)

        birth_place = MlbAthleteDetailsResponseBirthPlace.from_dict(d.pop("birthPlace"))

        college = MlbAthleteDetailsResponseCollege.from_dict(d.pop("college"))

        slug = d.pop("slug")

        headshot = MlbAthleteDetailsResponseHeadshot.from_dict(d.pop("headshot"))

        jersey = d.pop("jersey")

        position = MlbAthleteDetailsResponsePosition.from_dict(d.pop("position"))

        linked = d.pop("linked")

        team = MlbAthleteDetailsResponseTeam.from_dict(d.pop("team"))

        statistics = MlbAthleteDetailsResponseStatistics.from_dict(d.pop("statistics"))

        contracts = MlbAthleteDetailsResponseContracts.from_dict(d.pop("contracts"))

        experience = MlbAthleteDetailsResponseExperience.from_dict(d.pop("experience"))

        debut = MlbAthleteDetailsResponseDebut.from_dict(d.pop("debut"))

        active = d.pop("active")

        draft = MlbAthleteDetailsResponseDraft.from_dict(d.pop("draft"))

        status = MlbAthleteDetailsResponseStatus.from_dict(d.pop("status"))

        statisticslog = MlbAthleteDetailsResponseStatisticslog.from_dict(d.pop("statisticslog"))

        awards = MlbAthleteDetailsResponseAwards.from_dict(d.pop("awards"))

        bats = MlbAthleteDetailsResponseBats.from_dict(d.pop("bats"))

        throws = MlbAthleteDetailsResponseThrows.from_dict(d.pop("throws"))

        mlb_athlete_details_response = cls(
            ref=ref,
            id=id,
            uid=uid,
            guid=guid,
            type=type,
            alternate_ids=alternate_ids,
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            display_name=display_name,
            nickname=nickname,
            short_name=short_name,
            weight=weight,
            display_weight=display_weight,
            height=height,
            display_height=display_height,
            age=age,
            date_of_birth=date_of_birth,
            debut_year=debut_year,
            links=links,
            birth_place=birth_place,
            college=college,
            slug=slug,
            headshot=headshot,
            jersey=jersey,
            position=position,
            linked=linked,
            team=team,
            statistics=statistics,
            contracts=contracts,
            experience=experience,
            debut=debut,
            active=active,
            draft=draft,
            status=status,
            statisticslog=statisticslog,
            awards=awards,
            bats=bats,
            throws=throws,
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
