from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.athlete_flag import AthleteFlag
    from ..models.athlete_links import AthleteLinks
    from ..models.link import Link


T = TypeVar("T", bound="Athlete")


@_attrs_define
class Athlete:
    """
    Attributes:
        id (Union[Unset, int]): Athlete identifier (may not be present in some contexts like golf scoreboards) Example:
            15846.
        description (Union[Unset, str]): Athlete name Example: John Jenkins.
        display_name (Union[Unset, str]): Display name of the athlete Example: John Jenkins.
        full_name (Union[Unset, str]): Full name of the athlete Example: John Jenkins.
        short_name (Union[Unset, str]): Shortened name of the athlete Example: J. Jenkins.
        flag (Union[Unset, AthleteFlag]): Country flag information
        links (Union['AthleteLinks', List['Link'], Unset]):
    """

    id: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    flag: Union[Unset, "AthleteFlag"] = UNSET
    links: Union["AthleteLinks", List["Link"], Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.athlete_links import AthleteLinks

        id = self.id

        description = self.description

        display_name = self.display_name

        full_name = self.full_name

        short_name = self.short_name

        flag: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.flag, Unset):
            flag = self.flag.to_dict()

        links: Union[Dict[str, Any], List[Dict[str, Any]], Unset]
        if isinstance(self.links, Unset):
            links = UNSET
        elif isinstance(self.links, AthleteLinks):
            links = self.links.to_dict()
        else:
            links = []
            for links_type_1_item_data in self.links:
                links_type_1_item = links_type_1_item_data.to_dict()
                links.append(links_type_1_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if flag is not UNSET:
            field_dict["flag"] = flag
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.athlete_flag import AthleteFlag
        from ..models.athlete_links import AthleteLinks
        from ..models.link import Link

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        display_name = d.pop("displayName", UNSET)

        full_name = d.pop("fullName", UNSET)

        short_name = d.pop("shortName", UNSET)

        _flag = d.pop("flag", UNSET)
        flag: Union[Unset, AthleteFlag]
        if isinstance(_flag, Unset):
            flag = UNSET
        else:
            flag = AthleteFlag.from_dict(_flag)

        def _parse_links(data: object) -> Union["AthleteLinks", List["Link"], Unset]:
            if isinstance(data, Unset):
                return data
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

        links = _parse_links(d.pop("links", UNSET))

        athlete = cls(
            id=id,
            description=description,
            display_name=display_name,
            full_name=full_name,
            short_name=short_name,
            flag=flag,
            links=links,
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
