from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.nfl_draft_position import NflDraftPosition
    from ..models.nfl_draft_round import NflDraftRound
    from ..models.nfl_draft_team_need import NflDraftTeamNeed


T = TypeVar("T", bound="NflDraftResponse")


@_attrs_define
class NflDraftResponse:
    """
    Attributes:
        ref (str):
        uid (str):
        year (int):
        number_of_rounds (int):
        display_name (str):
        short_display_name (str):
        status (NflDraftRound):
        athletes (NflDraftRound):
        rounds (NflDraftRound):
        positions (List['NflDraftPosition']):
        needs (List['NflDraftTeamNeed']):
        links (List['Link']):
    """

    ref: str
    uid: str
    year: int
    number_of_rounds: int
    display_name: str
    short_display_name: str
    status: "NflDraftRound"
    athletes: "NflDraftRound"
    rounds: "NflDraftRound"
    positions: List["NflDraftPosition"]
    needs: List["NflDraftTeamNeed"]
    links: List["Link"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        uid = self.uid

        year = self.year

        number_of_rounds = self.number_of_rounds

        display_name = self.display_name

        short_display_name = self.short_display_name

        status = self.status.to_dict()

        athletes = self.athletes.to_dict()

        rounds = self.rounds.to_dict()

        positions = []
        for positions_item_data in self.positions:
            positions_item = positions_item_data.to_dict()
            positions.append(positions_item)

        needs = []
        for needs_item_data in self.needs:
            needs_item = needs_item_data.to_dict()
            needs.append(needs_item)

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "uid": uid,
                "year": year,
                "numberOfRounds": number_of_rounds,
                "displayName": display_name,
                "shortDisplayName": short_display_name,
                "status": status,
                "athletes": athletes,
                "rounds": rounds,
                "positions": positions,
                "needs": needs,
                "links": links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link import Link
        from ..models.nfl_draft_position import NflDraftPosition
        from ..models.nfl_draft_round import NflDraftRound
        from ..models.nfl_draft_team_need import NflDraftTeamNeed

        d = src_dict.copy()
        ref = d.pop("$ref")

        uid = d.pop("uid")

        year = d.pop("year")

        number_of_rounds = d.pop("numberOfRounds")

        display_name = d.pop("displayName")

        short_display_name = d.pop("shortDisplayName")

        status = NflDraftRound.from_dict(d.pop("status"))

        athletes = NflDraftRound.from_dict(d.pop("athletes"))

        rounds = NflDraftRound.from_dict(d.pop("rounds"))

        positions = []
        _positions = d.pop("positions")
        for positions_item_data in _positions:
            positions_item = NflDraftPosition.from_dict(positions_item_data)

            positions.append(positions_item)

        needs = []
        _needs = d.pop("needs")
        for needs_item_data in _needs:
            needs_item = NflDraftTeamNeed.from_dict(needs_item_data)

            needs.append(needs_item)

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        nfl_draft_response = cls(
            ref=ref,
            uid=uid,
            year=year,
            number_of_rounds=number_of_rounds,
            display_name=display_name,
            short_display_name=short_display_name,
            status=status,
            athletes=athletes,
            rounds=rounds,
            positions=positions,
            needs=needs,
            links=links,
        )

        nfl_draft_response.additional_properties = d
        return nfl_draft_response

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
