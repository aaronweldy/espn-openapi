from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.birth_place import BirthPlace
    from ..models.headshot import Headshot
    from ..models.link import Link
    from ..models.position import Position


T = TypeVar("T", bound="LeaderAthlete")


@_attrs_define
class LeaderAthlete:
    """
    Attributes:
        id (str): Athlete ID
        display_name (str): Display name
        uid (Union[Unset, str]): Unique identifier
        guid (Union[Unset, str]): Global unique identifier
        first_name (Union[Unset, str]): First name
        last_name (Union[Unset, str]): Last name
        full_name (Union[Unset, str]): Full name
        short_name (Union[Unset, str]): Short name
        jersey (Union[Unset, str]): Jersey number
        links (Union[Unset, List['Link']]):
        headshot (Union[Unset, Headshot]):
        position (Union[Unset, Position]):
        birth_place (Union[Unset, BirthPlace]):
    """

    id: str
    display_name: str
    uid: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    jersey: Union[Unset, str] = UNSET
    links: Union[Unset, List["Link"]] = UNSET
    headshot: Union[Unset, "Headshot"] = UNSET
    position: Union[Unset, "Position"] = UNSET
    birth_place: Union[Unset, "BirthPlace"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        display_name = self.display_name

        uid = self.uid

        guid = self.guid

        first_name = self.first_name

        last_name = self.last_name

        full_name = self.full_name

        short_name = self.short_name

        jersey = self.jersey

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        headshot: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headshot, Unset):
            headshot = self.headshot.to_dict()

        position: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        birth_place: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.birth_place, Unset):
            birth_place = self.birth_place.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "displayName": display_name,
            }
        )
        if uid is not UNSET:
            field_dict["uid"] = uid
        if guid is not UNSET:
            field_dict["guid"] = guid
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if jersey is not UNSET:
            field_dict["jersey"] = jersey
        if links is not UNSET:
            field_dict["links"] = links
        if headshot is not UNSET:
            field_dict["headshot"] = headshot
        if position is not UNSET:
            field_dict["position"] = position
        if birth_place is not UNSET:
            field_dict["birthPlace"] = birth_place

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.birth_place import BirthPlace
        from ..models.headshot import Headshot
        from ..models.link import Link
        from ..models.position import Position

        d = src_dict.copy()
        id = d.pop("id")

        display_name = d.pop("displayName")

        uid = d.pop("uid", UNSET)

        guid = d.pop("guid", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        full_name = d.pop("fullName", UNSET)

        short_name = d.pop("shortName", UNSET)

        jersey = d.pop("jersey", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        _headshot = d.pop("headshot", UNSET)
        headshot: Union[Unset, Headshot]
        if isinstance(_headshot, Unset):
            headshot = UNSET
        else:
            headshot = Headshot.from_dict(_headshot)

        _position = d.pop("position", UNSET)
        position: Union[Unset, Position]
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = Position.from_dict(_position)

        _birth_place = d.pop("birthPlace", UNSET)
        birth_place: Union[Unset, BirthPlace]
        if isinstance(_birth_place, Unset):
            birth_place = UNSET
        else:
            birth_place = BirthPlace.from_dict(_birth_place)

        leader_athlete = cls(
            id=id,
            display_name=display_name,
            uid=uid,
            guid=guid,
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            short_name=short_name,
            jersey=jersey,
            links=links,
            headshot=headshot,
            position=position,
            birth_place=birth_place,
        )

        leader_athlete.additional_properties = d
        return leader_athlete

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
