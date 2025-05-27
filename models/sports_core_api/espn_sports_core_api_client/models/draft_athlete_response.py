from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.draft_athlete_analysis import DraftAthleteAnalysis
    from ..models.draft_athlete_attribute import DraftAthleteAttribute
    from ..models.draft_athlete_headshot import DraftAthleteHeadshot
    from ..models.link import Link
    from ..models.logo import Logo
    from ..models.position import Position
    from ..models.reference import Reference


T = TypeVar("T", bound="DraftAthleteResponse")


@_attrs_define
class DraftAthleteResponse:
    """
    Attributes:
        ref (str):
        id (str):
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
        links (List['Link']):
        position (Position):
        positions (List['Position']):
        attributes (List['DraftAthleteAttribute']):
        analysis (List['DraftAthleteAnalysis']):
        pick (Reference):
        athlete (Reference):
        logo (Logo):
        college (Union[Unset, Reference]):
        team (Union[Unset, Reference]):
        headshot (Union[Unset, DraftAthleteHeadshot]):
        league_affiliation (Union[Unset, str]):
    """

    ref: str
    id: str
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
    links: List["Link"]
    position: "Position"
    positions: List["Position"]
    attributes: List["DraftAthleteAttribute"]
    analysis: List["DraftAthleteAnalysis"]
    pick: "Reference"
    athlete: "Reference"
    logo: "Logo"
    college: Union[Unset, "Reference"] = UNSET
    team: Union[Unset, "Reference"] = UNSET
    headshot: Union[Unset, "DraftAthleteHeadshot"] = UNSET
    league_affiliation: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        id = self.id

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

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        position = self.position.to_dict()

        positions = []
        for positions_item_data in self.positions:
            positions_item = positions_item_data.to_dict()
            positions.append(positions_item)

        attributes = []
        for attributes_item_data in self.attributes:
            attributes_item = attributes_item_data.to_dict()
            attributes.append(attributes_item)

        analysis = []
        for analysis_item_data in self.analysis:
            analysis_item = analysis_item_data.to_dict()
            analysis.append(analysis_item)

        pick = self.pick.to_dict()

        athlete = self.athlete.to_dict()

        logo = self.logo.to_dict()

        college: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.college, Unset):
            college = self.college.to_dict()

        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        headshot: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headshot, Unset):
            headshot = self.headshot.to_dict()

        league_affiliation = self.league_affiliation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "id": id,
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
                "links": links,
                "position": position,
                "positions": positions,
                "attributes": attributes,
                "analysis": analysis,
                "pick": pick,
                "athlete": athlete,
                "logo": logo,
            }
        )
        if college is not UNSET:
            field_dict["college"] = college
        if team is not UNSET:
            field_dict["team"] = team
        if headshot is not UNSET:
            field_dict["headshot"] = headshot
        if league_affiliation is not UNSET:
            field_dict["leagueAffiliation"] = league_affiliation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.draft_athlete_analysis import DraftAthleteAnalysis
        from ..models.draft_athlete_attribute import DraftAthleteAttribute
        from ..models.draft_athlete_headshot import DraftAthleteHeadshot
        from ..models.link import Link
        from ..models.logo import Logo
        from ..models.position import Position
        from ..models.reference import Reference

        d = src_dict.copy()
        ref = d.pop("$ref")

        id = d.pop("id")

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

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        position = Position.from_dict(d.pop("position"))

        positions = []
        _positions = d.pop("positions")
        for positions_item_data in _positions:
            positions_item = Position.from_dict(positions_item_data)

            positions.append(positions_item)

        attributes = []
        _attributes = d.pop("attributes")
        for attributes_item_data in _attributes:
            attributes_item = DraftAthleteAttribute.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        analysis = []
        _analysis = d.pop("analysis")
        for analysis_item_data in _analysis:
            analysis_item = DraftAthleteAnalysis.from_dict(analysis_item_data)

            analysis.append(analysis_item)

        pick = Reference.from_dict(d.pop("pick"))

        athlete = Reference.from_dict(d.pop("athlete"))

        logo = Logo.from_dict(d.pop("logo"))

        _college = d.pop("college", UNSET)
        college: Union[Unset, Reference]
        if isinstance(_college, Unset):
            college = UNSET
        else:
            college = Reference.from_dict(_college)

        _team = d.pop("team", UNSET)
        team: Union[Unset, Reference]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = Reference.from_dict(_team)

        _headshot = d.pop("headshot", UNSET)
        headshot: Union[Unset, DraftAthleteHeadshot]
        if isinstance(_headshot, Unset):
            headshot = UNSET
        else:
            headshot = DraftAthleteHeadshot.from_dict(_headshot)

        league_affiliation = d.pop("leagueAffiliation", UNSET)

        draft_athlete_response = cls(
            ref=ref,
            id=id,
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
            links=links,
            position=position,
            positions=positions,
            attributes=attributes,
            analysis=analysis,
            pick=pick,
            athlete=athlete,
            logo=logo,
            college=college,
            team=team,
            headshot=headshot,
            league_affiliation=league_affiliation,
        )

        draft_athlete_response.additional_properties = d
        return draft_athlete_response

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
