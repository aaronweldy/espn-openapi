from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.position import Position


T = TypeVar("T", bound="Athlete")


@_attrs_define
class Athlete:
    """
    Attributes:
        id (Union[Unset, str]):
        uid (Union[Unset, str]):
        guid (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        full_name (Union[Unset, str]):
        display_name (Union[Unset, str]):
        short_name (Union[Unset, str]):
        jersey (Union[Unset, str]):
        position (Union[Unset, Position]):
        headshot (Union[Unset, str]): URL to the athlete's headshot image
        links (Union[Unset, list['Link']]):
        active (Union[Unset, bool]):
    """

    id: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    jersey: Union[Unset, str] = UNSET
    position: Union[Unset, "Position"] = UNSET
    headshot: Union[Unset, str] = UNSET
    links: Union[Unset, list["Link"]] = UNSET
    active: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uid = self.uid

        guid = self.guid

        first_name = self.first_name

        last_name = self.last_name

        full_name = self.full_name

        display_name = self.display_name

        short_name = self.short_name

        jersey = self.jersey

        position: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        headshot = self.headshot

        links: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        active = self.active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
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
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if jersey is not UNSET:
            field_dict["jersey"] = jersey
        if position is not UNSET:
            field_dict["position"] = position
        if headshot is not UNSET:
            field_dict["headshot"] = headshot
        if links is not UNSET:
            field_dict["links"] = links
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.link import Link
        from ..models.position import Position

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uid = d.pop("uid", UNSET)

        guid = d.pop("guid", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        full_name = d.pop("fullName", UNSET)

        display_name = d.pop("displayName", UNSET)

        short_name = d.pop("shortName", UNSET)

        jersey = d.pop("jersey", UNSET)

        _position = d.pop("position", UNSET)
        position: Union[Unset, Position]
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = Position.from_dict(_position)

        headshot = d.pop("headshot", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        active = d.pop("active", UNSET)

        athlete = cls(
            id=id,
            uid=uid,
            guid=guid,
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            display_name=display_name,
            short_name=short_name,
            jersey=jersey,
            position=position,
            headshot=headshot,
            links=links,
            active=active,
        )

        athlete.additional_properties = d
        return athlete

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
