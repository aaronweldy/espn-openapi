from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scoreboard_link import ScoreboardLink


T = TypeVar("T", bound="ScoreboardTicket")


@_attrs_define
class ScoreboardTicket:
    """
    Attributes:
        summary (Union[Unset, str]):
        number_available (Union[Unset, int]):
        links (Union[Unset, List['ScoreboardLink']]):
    """

    summary: Union[Unset, str] = UNSET
    number_available: Union[Unset, int] = UNSET
    links: Union[Unset, List["ScoreboardLink"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        summary = self.summary

        number_available = self.number_available

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if summary is not UNSET:
            field_dict["summary"] = summary
        if number_available is not UNSET:
            field_dict["numberAvailable"] = number_available
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scoreboard_link import ScoreboardLink

        d = src_dict.copy()
        summary = d.pop("summary", UNSET)

        number_available = d.pop("numberAvailable", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = ScoreboardLink.from_dict(links_item_data)

            links.append(links_item)

        scoreboard_ticket = cls(
            summary=summary,
            number_available=number_available,
            links=links,
        )

        scoreboard_ticket.additional_properties = d
        return scoreboard_ticket

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
