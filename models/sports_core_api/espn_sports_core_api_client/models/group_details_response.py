from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reference import Reference


T = TypeVar("T", bound="GroupDetailsResponse")


@_attrs_define
class GroupDetailsResponse:
    """Detailed information about a specific group (conference/division) in a league season.

    Attributes:
        ref (str): Reference URL to this group resource Example:
            http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2024/types/2/groups/7?lang=en&region=us.
        uid (str): Unique identifier for the group Example: s:20~l:28~g:7.
        id (str): The group ID Example: 7.
        name (str): The full name of the group Example: National Football Conference.
        abbreviation (str): The abbreviated name of the group Example: NFC.
        season (Reference):
        children (Reference):
        parent (Reference):
        standings (Reference):
        is_conference (bool): Whether this group represents a conference Example: True.
        slug (str): URL-friendly slug for the group Example: national-football-conference.
        teams (Reference):
    """

    ref: str
    uid: str
    id: str
    name: str
    abbreviation: str
    season: "Reference"
    children: "Reference"
    parent: "Reference"
    standings: "Reference"
    is_conference: bool
    slug: str
    teams: "Reference"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        uid = self.uid

        id = self.id

        name = self.name

        abbreviation = self.abbreviation

        season = self.season.to_dict()

        children = self.children.to_dict()

        parent = self.parent.to_dict()

        standings = self.standings.to_dict()

        is_conference = self.is_conference

        slug = self.slug

        teams = self.teams.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "uid": uid,
                "id": id,
                "name": name,
                "abbreviation": abbreviation,
                "season": season,
                "children": children,
                "parent": parent,
                "standings": standings,
                "isConference": is_conference,
                "slug": slug,
                "teams": teams,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reference import Reference

        d = src_dict.copy()
        ref = d.pop("$ref")

        uid = d.pop("uid")

        id = d.pop("id")

        name = d.pop("name")

        abbreviation = d.pop("abbreviation")

        season = Reference.from_dict(d.pop("season"))

        children = Reference.from_dict(d.pop("children"))

        parent = Reference.from_dict(d.pop("parent"))

        standings = Reference.from_dict(d.pop("standings"))

        is_conference = d.pop("isConference")

        slug = d.pop("slug")

        teams = Reference.from_dict(d.pop("teams"))

        group_details_response = cls(
            ref=ref,
            uid=uid,
            id=id,
            name=name,
            abbreviation=abbreviation,
            season=season,
            children=children,
            parent=parent,
            standings=standings,
            is_conference=is_conference,
            slug=slug,
            teams=teams,
        )

        group_details_response.additional_properties = d
        return group_details_response

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
