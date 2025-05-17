from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.logo import Logo
    from ..models.nfl_draft_athlete_analysis import NflDraftAthleteAnalysis
    from ..models.nfl_draft_athlete_attribute import NflDraftAthleteAttribute
    from ..models.position import Position
    from ..models.reference import Reference


T = TypeVar("T", bound="NflDraftAthleteResponse")


@_attrs_define
class NflDraftAthleteResponse:
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
        college (Reference):
        position (Position):
        positions (List['Position']):
        team (Reference):
        attributes (List['NflDraftAthleteAttribute']):
        analysis (List['NflDraftAthleteAnalysis']):
        pick (Reference):
        athlete (Reference):
        logo (Logo):
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
    college: "Reference"
    position: "Position"
    positions: List["Position"]
    team: "Reference"
    attributes: List["NflDraftAthleteAttribute"]
    analysis: List["NflDraftAthleteAnalysis"]
    pick: "Reference"
    athlete: "Reference"
    logo: "Logo"
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

        college = self.college.to_dict()

        position = self.position.to_dict()

        positions = []
        for positions_item_data in self.positions:
            positions_item = positions_item_data.to_dict()
            positions.append(positions_item)

        team = self.team.to_dict()

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
                "college": college,
                "position": position,
                "positions": positions,
                "team": team,
                "attributes": attributes,
                "analysis": analysis,
                "pick": pick,
                "athlete": athlete,
                "logo": logo,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link import Link
        from ..models.logo import Logo
        from ..models.nfl_draft_athlete_analysis import NflDraftAthleteAnalysis
        from ..models.nfl_draft_athlete_attribute import NflDraftAthleteAttribute
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

        college = Reference.from_dict(d.pop("college"))

        position = Position.from_dict(d.pop("position"))

        positions = []
        _positions = d.pop("positions")
        for positions_item_data in _positions:
            positions_item = Position.from_dict(positions_item_data)

            positions.append(positions_item)

        team = Reference.from_dict(d.pop("team"))

        attributes = []
        _attributes = d.pop("attributes")
        for attributes_item_data in _attributes:
            attributes_item = NflDraftAthleteAttribute.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        analysis = []
        _analysis = d.pop("analysis")
        for analysis_item_data in _analysis:
            analysis_item = NflDraftAthleteAnalysis.from_dict(analysis_item_data)

            analysis.append(analysis_item)

        pick = Reference.from_dict(d.pop("pick"))

        athlete = Reference.from_dict(d.pop("athlete"))

        logo = Logo.from_dict(d.pop("logo"))

        nfl_draft_athlete_response = cls(
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
            college=college,
            position=position,
            positions=positions,
            team=team,
            attributes=attributes,
            analysis=analysis,
            pick=pick,
            athlete=athlete,
            logo=logo,
        )

        nfl_draft_athlete_response.additional_properties = d
        return nfl_draft_athlete_response

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
