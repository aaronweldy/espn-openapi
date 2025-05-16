from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scoreboard_competition import ScoreboardCompetition
    from ..models.scoreboard_status import ScoreboardStatus
    from ..models.scoreboard_week import ScoreboardWeek


T = TypeVar("T", bound="ScoreboardEvent")


@_attrs_define
class ScoreboardEvent:
    """
    Attributes:
        date (Union[Unset, str]):
        uid (Union[Unset, str]):
        week (Union[Unset, ScoreboardWeek]):
        name (Union[Unset, str]):
        competitions (Union[Unset, List['ScoreboardCompetition']]):
        short_name (Union[Unset, str]):
        status (Union[Unset, ScoreboardStatus]):
    """

    date: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    week: Union[Unset, "ScoreboardWeek"] = UNSET
    name: Union[Unset, str] = UNSET
    competitions: Union[Unset, List["ScoreboardCompetition"]] = UNSET
    short_name: Union[Unset, str] = UNSET
    status: Union[Unset, "ScoreboardStatus"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date = self.date

        uid = self.uid

        week: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.week, Unset):
            week = self.week.to_dict()

        name = self.name

        competitions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.competitions, Unset):
            competitions = []
            for competitions_item_data in self.competitions:
                competitions_item = competitions_item_data.to_dict()
                competitions.append(competitions_item)

        short_name = self.short_name

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if uid is not UNSET:
            field_dict["uid"] = uid
        if week is not UNSET:
            field_dict["week"] = week
        if name is not UNSET:
            field_dict["name"] = name
        if competitions is not UNSET:
            field_dict["competitions"] = competitions
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scoreboard_competition import ScoreboardCompetition
        from ..models.scoreboard_status import ScoreboardStatus
        from ..models.scoreboard_week import ScoreboardWeek

        d = src_dict.copy()
        date = d.pop("date", UNSET)

        uid = d.pop("uid", UNSET)

        _week = d.pop("week", UNSET)
        week: Union[Unset, ScoreboardWeek]
        if isinstance(_week, Unset):
            week = UNSET
        else:
            week = ScoreboardWeek.from_dict(_week)

        name = d.pop("name", UNSET)

        competitions = []
        _competitions = d.pop("competitions", UNSET)
        for competitions_item_data in _competitions or []:
            competitions_item = ScoreboardCompetition.from_dict(competitions_item_data)

            competitions.append(competitions_item)

        short_name = d.pop("shortName", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ScoreboardStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ScoreboardStatus.from_dict(_status)

        scoreboard_event = cls(
            date=date,
            uid=uid,
            week=week,
            name=name,
            competitions=competitions,
            short_name=short_name,
            status=status,
        )

        scoreboard_event.additional_properties = d
        return scoreboard_event

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
