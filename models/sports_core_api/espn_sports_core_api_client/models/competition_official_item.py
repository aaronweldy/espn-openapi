from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.official_position import OfficialPosition


T = TypeVar("T", bound="CompetitionOfficialItem")


@_attrs_define
class CompetitionOfficialItem:
    """
    Attributes:
        ref (str):
        id (str):
        first_name (str):
        last_name (str):
        full_name (str):
        display_name (str):
        position (OfficialPosition):
        order (int):
    """

    ref: str
    id: str
    first_name: str
    last_name: str
    full_name: str
    display_name: str
    position: "OfficialPosition"
    order: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        id = self.id

        first_name = self.first_name

        last_name = self.last_name

        full_name = self.full_name

        display_name = self.display_name

        position = self.position.to_dict()

        order = self.order

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "id": id,
                "firstName": first_name,
                "lastName": last_name,
                "fullName": full_name,
                "displayName": display_name,
                "position": position,
                "order": order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.official_position import OfficialPosition

        d = src_dict.copy()
        ref = d.pop("$ref")

        id = d.pop("id")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        full_name = d.pop("fullName")

        display_name = d.pop("displayName")

        position = OfficialPosition.from_dict(d.pop("position"))

        order = d.pop("order")

        competition_official_item = cls(
            ref=ref,
            id=id,
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            display_name=display_name,
            position=position,
            order=order,
        )

        competition_official_item.additional_properties = d
        return competition_official_item

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
