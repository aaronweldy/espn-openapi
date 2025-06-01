from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fantasy_scoring_play_participants_item_athlete import FantasyScoringPlayParticipantsItemAthlete


T = TypeVar("T", bound="FantasyScoringPlayParticipantsItem")


@_attrs_define
class FantasyScoringPlayParticipantsItem:
    """
    Attributes:
        name (Union[Unset, str]):
        athlete (Union[Unset, FantasyScoringPlayParticipantsItemAthlete]):
    """

    name: Union[Unset, str] = UNSET
    athlete: Union[Unset, "FantasyScoringPlayParticipantsItemAthlete"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        athlete: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.athlete, Unset):
            athlete = self.athlete.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if athlete is not UNSET:
            field_dict["athlete"] = athlete

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fantasy_scoring_play_participants_item_athlete import FantasyScoringPlayParticipantsItemAthlete

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _athlete = d.pop("athlete", UNSET)
        athlete: Union[Unset, FantasyScoringPlayParticipantsItemAthlete]
        if isinstance(_athlete, Unset):
            athlete = UNSET
        else:
            athlete = FantasyScoringPlayParticipantsItemAthlete.from_dict(_athlete)

        fantasy_scoring_play_participants_item = cls(
            name=name,
            athlete=athlete,
        )

        fantasy_scoring_play_participants_item.additional_properties = d
        return fantasy_scoring_play_participants_item

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
