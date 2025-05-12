from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_details_full_next_event_item import TeamDetailsFullNextEventItem
    from ..models.team_franchise import TeamFranchise
    from ..models.team_groups import TeamGroups
    from ..models.team_link import TeamLink
    from ..models.team_logo import TeamLogo
    from ..models.team_record import TeamRecord


T = TypeVar("T", bound="TeamDetailsFull")


@_attrs_define
class TeamDetailsFull:
    """
    Attributes:
        id (str):  Example: 12.
        display_name (str):  Example: Kansas City Chiefs.
        uid (Union[Unset, str]):  Example: s:20~l:28~t:12.
        slug (Union[Unset, str]):  Example: kansas-city-chiefs.
        location (Union[Unset, str]):  Example: Kansas City.
        name (Union[Unset, str]):  Example: Chiefs.
        nickname (Union[Unset, str]):  Example: Chiefs.
        abbreviation (Union[Unset, str]):  Example: KC.
        short_display_name (Union[Unset, str]):  Example: Chiefs.
        color (Union[Unset, str]):  Example: e31837.
        alternate_color (Union[Unset, str]):  Example: ffb612.
        is_active (Union[Unset, bool]):
        logos (Union[Unset, list['TeamLogo']]):
        record (Union[Unset, TeamRecord]):
        groups (Union[Unset, TeamGroups]):
        links (Union[Unset, list['TeamLink']]):
        franchise (Union[Unset, TeamFranchise]):
        next_event (Union[Unset, list['TeamDetailsFullNextEventItem']]):
        standing_summary (Union[Unset, str]):  Example: 1st in AFC West.
    """

    id: str
    display_name: str
    uid: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    nickname: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    short_display_name: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    alternate_color: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    logos: Union[Unset, list["TeamLogo"]] = UNSET
    record: Union[Unset, "TeamRecord"] = UNSET
    groups: Union[Unset, "TeamGroups"] = UNSET
    links: Union[Unset, list["TeamLink"]] = UNSET
    franchise: Union[Unset, "TeamFranchise"] = UNSET
    next_event: Union[Unset, list["TeamDetailsFullNextEventItem"]] = UNSET
    standing_summary: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        display_name = self.display_name

        uid = self.uid

        slug = self.slug

        location = self.location

        name = self.name

        nickname = self.nickname

        abbreviation = self.abbreviation

        short_display_name = self.short_display_name

        color = self.color

        alternate_color = self.alternate_color

        is_active = self.is_active

        logos: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.logos, Unset):
            logos = []
            for logos_item_data in self.logos:
                logos_item = logos_item_data.to_dict()
                logos.append(logos_item)

        record: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.record, Unset):
            record = self.record.to_dict()

        groups: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups.to_dict()

        links: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        franchise: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.franchise, Unset):
            franchise = self.franchise.to_dict()

        next_event: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.next_event, Unset):
            next_event = []
            for next_event_item_data in self.next_event:
                next_event_item = next_event_item_data.to_dict()
                next_event.append(next_event_item)

        standing_summary = self.standing_summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "displayName": display_name,
            }
        )
        if uid is not UNSET:
            field_dict["uid"] = uid
        if slug is not UNSET:
            field_dict["slug"] = slug
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if short_display_name is not UNSET:
            field_dict["shortDisplayName"] = short_display_name
        if color is not UNSET:
            field_dict["color"] = color
        if alternate_color is not UNSET:
            field_dict["alternateColor"] = alternate_color
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if logos is not UNSET:
            field_dict["logos"] = logos
        if record is not UNSET:
            field_dict["record"] = record
        if groups is not UNSET:
            field_dict["groups"] = groups
        if links is not UNSET:
            field_dict["links"] = links
        if franchise is not UNSET:
            field_dict["franchise"] = franchise
        if next_event is not UNSET:
            field_dict["nextEvent"] = next_event
        if standing_summary is not UNSET:
            field_dict["standingSummary"] = standing_summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_details_full_next_event_item import TeamDetailsFullNextEventItem
        from ..models.team_franchise import TeamFranchise
        from ..models.team_groups import TeamGroups
        from ..models.team_link import TeamLink
        from ..models.team_logo import TeamLogo
        from ..models.team_record import TeamRecord

        d = dict(src_dict)
        id = d.pop("id")

        display_name = d.pop("displayName")

        uid = d.pop("uid", UNSET)

        slug = d.pop("slug", UNSET)

        location = d.pop("location", UNSET)

        name = d.pop("name", UNSET)

        nickname = d.pop("nickname", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        short_display_name = d.pop("shortDisplayName", UNSET)

        color = d.pop("color", UNSET)

        alternate_color = d.pop("alternateColor", UNSET)

        is_active = d.pop("isActive", UNSET)

        logos = []
        _logos = d.pop("logos", UNSET)
        for logos_item_data in _logos or []:
            logos_item = TeamLogo.from_dict(logos_item_data)

            logos.append(logos_item)

        _record = d.pop("record", UNSET)
        record: Union[Unset, TeamRecord]
        if isinstance(_record, Unset):
            record = UNSET
        else:
            record = TeamRecord.from_dict(_record)

        _groups = d.pop("groups", UNSET)
        groups: Union[Unset, TeamGroups]
        if isinstance(_groups, Unset):
            groups = UNSET
        else:
            groups = TeamGroups.from_dict(_groups)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = TeamLink.from_dict(links_item_data)

            links.append(links_item)

        _franchise = d.pop("franchise", UNSET)
        franchise: Union[Unset, TeamFranchise]
        if isinstance(_franchise, Unset):
            franchise = UNSET
        else:
            franchise = TeamFranchise.from_dict(_franchise)

        next_event = []
        _next_event = d.pop("nextEvent", UNSET)
        for next_event_item_data in _next_event or []:
            next_event_item = TeamDetailsFullNextEventItem.from_dict(next_event_item_data)

            next_event.append(next_event_item)

        standing_summary = d.pop("standingSummary", UNSET)

        team_details_full = cls(
            id=id,
            display_name=display_name,
            uid=uid,
            slug=slug,
            location=location,
            name=name,
            nickname=nickname,
            abbreviation=abbreviation,
            short_display_name=short_display_name,
            color=color,
            alternate_color=alternate_color,
            is_active=is_active,
            logos=logos,
            record=record,
            groups=groups,
            links=links,
            franchise=franchise,
            next_event=next_event,
            standing_summary=standing_summary,
        )

        team_details_full.additional_properties = d
        return team_details_full

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
