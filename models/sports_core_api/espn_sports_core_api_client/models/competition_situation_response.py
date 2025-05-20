from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.last_play_reference import LastPlayReference


T = TypeVar("T", bound="CompetitionSituationResponse")


@_attrs_define
class CompetitionSituationResponse:
    """
    Attributes:
        ref (str):
        last_play (LastPlayReference):
        down (int):
        yard_line (int):
        distance (int):
        is_red_zone (bool):
        home_timeouts (int):
        away_timeouts (int):
    """

    ref: str
    last_play: "LastPlayReference"
    down: int
    yard_line: int
    distance: int
    is_red_zone: bool
    home_timeouts: int
    away_timeouts: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        last_play = self.last_play.to_dict()

        down = self.down

        yard_line = self.yard_line

        distance = self.distance

        is_red_zone = self.is_red_zone

        home_timeouts = self.home_timeouts

        away_timeouts = self.away_timeouts

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "lastPlay": last_play,
                "down": down,
                "yardLine": yard_line,
                "distance": distance,
                "isRedZone": is_red_zone,
                "homeTimeouts": home_timeouts,
                "awayTimeouts": away_timeouts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.last_play_reference import LastPlayReference

        d = src_dict.copy()
        ref = d.pop("$ref")

        last_play = LastPlayReference.from_dict(d.pop("lastPlay"))

        down = d.pop("down")

        yard_line = d.pop("yardLine")

        distance = d.pop("distance")

        is_red_zone = d.pop("isRedZone")

        home_timeouts = d.pop("homeTimeouts")

        away_timeouts = d.pop("awayTimeouts")

        competition_situation_response = cls(
            ref=ref,
            last_play=last_play,
            down=down,
            yard_line=yard_line,
            distance=distance,
            is_red_zone=is_red_zone,
            home_timeouts=home_timeouts,
            away_timeouts=away_timeouts,
        )

        competition_situation_response.additional_properties = d
        return competition_situation_response

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
