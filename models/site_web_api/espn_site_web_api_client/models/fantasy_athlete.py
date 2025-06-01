from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fantasy_athlete_headshot import FantasyAthleteHeadshot
    from ..models.fantasy_athlete_position import FantasyAthletePosition
    from ..models.link import Link


T = TypeVar("T", bound="FantasyAthlete")


@_attrs_define
class FantasyAthlete:
    """
    Attributes:
        id (Union[Unset, str]):
        uid (Union[Unset, str]):
        guid (Union[Unset, str]):
        last_name (Union[Unset, str]):
        full_name (Union[Unset, str]):
        display_name (Union[Unset, str]):
        short_name (Union[Unset, str]):
        links (Union[Unset, List['Link']]):
        headshot (Union[Unset, FantasyAthleteHeadshot]):
        jersey (Union[Unset, str]):
        position (Union[Unset, FantasyAthletePosition]):
    """

    id: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    links: Union[Unset, List["Link"]] = UNSET
    headshot: Union[Unset, "FantasyAthleteHeadshot"] = UNSET
    jersey: Union[Unset, str] = UNSET
    position: Union[Unset, "FantasyAthletePosition"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        uid = self.uid

        guid = self.guid

        last_name = self.last_name

        full_name = self.full_name

        display_name = self.display_name

        short_name = self.short_name

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        headshot: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headshot, Unset):
            headshot = self.headshot.to_dict()

        jersey = self.jersey

        position: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uid is not UNSET:
            field_dict["uid"] = uid
        if guid is not UNSET:
            field_dict["guid"] = guid
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if links is not UNSET:
            field_dict["links"] = links
        if headshot is not UNSET:
            field_dict["headshot"] = headshot
        if jersey is not UNSET:
            field_dict["jersey"] = jersey
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fantasy_athlete_headshot import FantasyAthleteHeadshot
        from ..models.fantasy_athlete_position import FantasyAthletePosition
        from ..models.link import Link

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        uid = d.pop("uid", UNSET)

        guid = d.pop("guid", UNSET)

        last_name = d.pop("lastName", UNSET)

        full_name = d.pop("fullName", UNSET)

        display_name = d.pop("displayName", UNSET)

        short_name = d.pop("shortName", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        _headshot = d.pop("headshot", UNSET)
        headshot: Union[Unset, FantasyAthleteHeadshot]
        if isinstance(_headshot, Unset):
            headshot = UNSET
        else:
            headshot = FantasyAthleteHeadshot.from_dict(_headshot)

        jersey = d.pop("jersey", UNSET)

        _position = d.pop("position", UNSET)
        position: Union[Unset, FantasyAthletePosition]
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = FantasyAthletePosition.from_dict(_position)

        fantasy_athlete = cls(
            id=id,
            uid=uid,
            guid=guid,
            last_name=last_name,
            full_name=full_name,
            display_name=display_name,
            short_name=short_name,
            links=links,
            headshot=headshot,
            jersey=jersey,
            position=position,
        )

        fantasy_athlete.additional_properties = d
        return fantasy_athlete

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
