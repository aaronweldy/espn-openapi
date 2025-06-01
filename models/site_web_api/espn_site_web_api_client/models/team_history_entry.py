from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="TeamHistoryEntry")


@_attrs_define
class TeamHistoryEntry:
    """
    Attributes:
        id (str): Team ID
        display_name (str): Full team name
        seasons (str): Seasons played (e.g., "2017-CURRENT" or "2015-2017")
        uid (Union[Unset, str]): Unique identifier
        slug (Union[Unset, str]): URL slug
        logo (Union[Unset, str]): Team logo URL
        links (Union[Unset, List['Link']]):
        season_count (Union[Unset, str]): Number of seasons with team
        is_active (Union[Unset, bool]): Whether currently on this team
    """

    id: str
    display_name: str
    seasons: str
    uid: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    logo: Union[Unset, str] = UNSET
    links: Union[Unset, List["Link"]] = UNSET
    season_count: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        display_name = self.display_name

        seasons = self.seasons

        uid = self.uid

        slug = self.slug

        logo = self.logo

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        season_count = self.season_count

        is_active = self.is_active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "displayName": display_name,
                "seasons": seasons,
            }
        )
        if uid is not UNSET:
            field_dict["uid"] = uid
        if slug is not UNSET:
            field_dict["slug"] = slug
        if logo is not UNSET:
            field_dict["logo"] = logo
        if links is not UNSET:
            field_dict["links"] = links
        if season_count is not UNSET:
            field_dict["seasonCount"] = season_count
        if is_active is not UNSET:
            field_dict["isActive"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link import Link

        d = src_dict.copy()
        id = d.pop("id")

        display_name = d.pop("displayName")

        seasons = d.pop("seasons")

        uid = d.pop("uid", UNSET)

        slug = d.pop("slug", UNSET)

        logo = d.pop("logo", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        season_count = d.pop("seasonCount", UNSET)

        is_active = d.pop("isActive", UNSET)

        team_history_entry = cls(
            id=id,
            display_name=display_name,
            seasons=seasons,
            uid=uid,
            slug=slug,
            logo=logo,
            links=links,
            season_count=season_count,
            is_active=is_active,
        )

        team_history_entry.additional_properties = d
        return team_history_entry

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
