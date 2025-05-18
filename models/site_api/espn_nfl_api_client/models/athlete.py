from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.athlete_links import AthleteLinks
    from ..models.link import Link


T = TypeVar("T", bound="Athlete")


@_attrs_define
class Athlete:
    """
    Attributes:
        id (int): Athlete identifier Example: 15846.
        links (Union['AthleteLinks', List['Link']]):
        description (Union[Unset, str]): Athlete name Example: John Jenkins.
    """

    id: int
    links: Union["AthleteLinks", List["Link"]]
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.athlete_links import AthleteLinks

        id = self.id

        links: Union[Dict[str, Any], List[Dict[str, Any]]]
        if isinstance(self.links, AthleteLinks):
            links = self.links.to_dict()
        else:
            links = []
            for links_type_1_item_data in self.links:
                links_type_1_item = links_type_1_item_data.to_dict()
                links.append(links_type_1_item)

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "links": links,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.athlete_links import AthleteLinks
        from ..models.link import Link

        d = src_dict.copy()
        id = d.pop("id")

        def _parse_links(data: object) -> Union["AthleteLinks", List["Link"]]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                links_type_0 = AthleteLinks.from_dict(data)

                return links_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, list):
                raise TypeError()
            links_type_1 = []
            _links_type_1 = data
            for links_type_1_item_data in _links_type_1:
                links_type_1_item = Link.from_dict(links_type_1_item_data)

                links_type_1.append(links_type_1_item)

            return links_type_1

        links = _parse_links(d.pop("links"))

        description = d.pop("description", UNSET)

        athlete = cls(
            id=id,
            links=links,
            description=description,
        )

        athlete.additional_properties = d
        return athlete

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
