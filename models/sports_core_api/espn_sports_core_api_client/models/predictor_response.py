import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.predictor_team import PredictorTeam


T = TypeVar("T", bound="PredictorResponse")


@_attrs_define
class PredictorResponse:
    """
    Attributes:
        name (str): Full name of the game Example: Baltimore Ravens at Jacksonville Jaguars.
        short_name (str): Short name of the game Example: BAL @ JAX.
        home_team (PredictorTeam):
        away_team (PredictorTeam):
        ref (Union[Unset, str]): Reference URL to this predictor data
        last_modified (Union[Unset, datetime.datetime]): Last modification timestamp
    """

    name: str
    short_name: str
    home_team: "PredictorTeam"
    away_team: "PredictorTeam"
    ref: Union[Unset, str] = UNSET
    last_modified: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        short_name = self.short_name

        home_team = self.home_team.to_dict()

        away_team = self.away_team.to_dict()

        ref = self.ref

        last_modified: Union[Unset, str] = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "shortName": short_name,
                "homeTeam": home_team,
                "awayTeam": away_team,
            }
        )
        if ref is not UNSET:
            field_dict["$ref"] = ref
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.predictor_team import PredictorTeam

        d = src_dict.copy()
        name = d.pop("name")

        short_name = d.pop("shortName")

        home_team = PredictorTeam.from_dict(d.pop("homeTeam"))

        away_team = PredictorTeam.from_dict(d.pop("awayTeam"))

        ref = d.pop("$ref", UNSET)

        _last_modified = d.pop("lastModified", UNSET)
        last_modified: Union[Unset, datetime.datetime]
        if isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = isoparse(_last_modified)

        predictor_response = cls(
            name=name,
            short_name=short_name,
            home_team=home_team,
            away_team=away_team,
            ref=ref,
            last_modified=last_modified,
        )

        predictor_response.additional_properties = d
        return predictor_response

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
