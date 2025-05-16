from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scoreboard_venue_address import ScoreboardVenueAddress


T = TypeVar("T", bound="ScoreboardVenue")


@_attrs_define
class ScoreboardVenue:
    """
    Attributes:
        address (Union[Unset, ScoreboardVenueAddress]):
        full_name (Union[Unset, str]):
        indoor (Union[Unset, bool]):
        id (Union[Unset, str]):
        city (Union[Unset, str]):
        state (Union[Unset, str]):
        country (Union[Unset, str]):
    """

    address: Union[Unset, "ScoreboardVenueAddress"] = UNSET
    full_name: Union[Unset, str] = UNSET
    indoor: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        full_name = self.full_name

        indoor = self.indoor

        id = self.id

        city = self.city

        state = self.state

        country = self.country

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if indoor is not UNSET:
            field_dict["indoor"] = indoor
        if id is not UNSET:
            field_dict["id"] = id
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scoreboard_venue_address import ScoreboardVenueAddress

        d = src_dict.copy()
        _address = d.pop("address", UNSET)
        address: Union[Unset, ScoreboardVenueAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = ScoreboardVenueAddress.from_dict(_address)

        full_name = d.pop("fullName", UNSET)

        indoor = d.pop("indoor", UNSET)

        id = d.pop("id", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        country = d.pop("country", UNSET)

        scoreboard_venue = cls(
            address=address,
            full_name=full_name,
            indoor=indoor,
            id=id,
            city=city,
            state=state,
            country=country,
        )

        scoreboard_venue.additional_properties = d
        return scoreboard_venue

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
