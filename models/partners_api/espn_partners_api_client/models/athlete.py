from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alternate_ids import AlternateIds
    from ..models.draft import Draft
    from ..models.injury import Injury
    from ..models.position import Position
    from ..models.status import Status
    from ..models.team import Team


T = TypeVar("T", bound="Athlete")


@_attrs_define
class Athlete:
    """
    Attributes:
        id (str): Unique athlete identifier Example: 4429202.
        display_name (str): Full display name Example: Israel Abanikanda.
        first_name (Union[Unset, str]): Athlete's first name Example: Israel.
        last_name (Union[Unset, str]): Athlete's last name Example: Abanikanda.
        weight (Union[Unset, float]): Athlete's weight in pounds Example: 216.0.
        height (Union[Unset, float]): Athlete's height in inches Example: 70.0.
        age (Union[Unset, int]): Athlete's age Example: 22.
        team (Union[Unset, Team]):
        jersey (Union[Unset, str]): Jersey number Example: 47.
        position (Union[Unset, Position]):
        draft (Union[Unset, Draft]):
        status (Union[Unset, Status]):
        alternate_ids (Union[Unset, AlternateIds]):
        injuries (Union[Unset, List['Injury']]):
    """

    id: str
    display_name: str
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    weight: Union[Unset, float] = UNSET
    height: Union[Unset, float] = UNSET
    age: Union[Unset, int] = UNSET
    team: Union[Unset, "Team"] = UNSET
    jersey: Union[Unset, str] = UNSET
    position: Union[Unset, "Position"] = UNSET
    draft: Union[Unset, "Draft"] = UNSET
    status: Union[Unset, "Status"] = UNSET
    alternate_ids: Union[Unset, "AlternateIds"] = UNSET
    injuries: Union[Unset, List["Injury"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        display_name = self.display_name

        first_name = self.first_name

        last_name = self.last_name

        weight = self.weight

        height = self.height

        age = self.age

        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        jersey = self.jersey

        position: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        draft: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.draft, Unset):
            draft = self.draft.to_dict()

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        alternate_ids: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.alternate_ids, Unset):
            alternate_ids = self.alternate_ids.to_dict()

        injuries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.injuries, Unset):
            injuries = []
            for injuries_item_data in self.injuries:
                injuries_item = injuries_item_data.to_dict()
                injuries.append(injuries_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "displayName": display_name,
            }
        )
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if weight is not UNSET:
            field_dict["weight"] = weight
        if height is not UNSET:
            field_dict["height"] = height
        if age is not UNSET:
            field_dict["age"] = age
        if team is not UNSET:
            field_dict["team"] = team
        if jersey is not UNSET:
            field_dict["jersey"] = jersey
        if position is not UNSET:
            field_dict["position"] = position
        if draft is not UNSET:
            field_dict["draft"] = draft
        if status is not UNSET:
            field_dict["status"] = status
        if alternate_ids is not UNSET:
            field_dict["alternateIds"] = alternate_ids
        if injuries is not UNSET:
            field_dict["injuries"] = injuries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.alternate_ids import AlternateIds
        from ..models.draft import Draft
        from ..models.injury import Injury
        from ..models.position import Position
        from ..models.status import Status
        from ..models.team import Team

        d = src_dict.copy()
        id = d.pop("id")

        display_name = d.pop("displayName")

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        weight = d.pop("weight", UNSET)

        height = d.pop("height", UNSET)

        age = d.pop("age", UNSET)

        _team = d.pop("team", UNSET)
        team: Union[Unset, Team]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = Team.from_dict(_team)

        jersey = d.pop("jersey", UNSET)

        _position = d.pop("position", UNSET)
        position: Union[Unset, Position]
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = Position.from_dict(_position)

        _draft = d.pop("draft", UNSET)
        draft: Union[Unset, Draft]
        if isinstance(_draft, Unset):
            draft = UNSET
        else:
            draft = Draft.from_dict(_draft)

        _status = d.pop("status", UNSET)
        status: Union[Unset, Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = Status.from_dict(_status)

        _alternate_ids = d.pop("alternateIds", UNSET)
        alternate_ids: Union[Unset, AlternateIds]
        if isinstance(_alternate_ids, Unset):
            alternate_ids = UNSET
        else:
            alternate_ids = AlternateIds.from_dict(_alternate_ids)

        injuries = []
        _injuries = d.pop("injuries", UNSET)
        for injuries_item_data in _injuries or []:
            injuries_item = Injury.from_dict(injuries_item_data)

            injuries.append(injuries_item)

        athlete = cls(
            id=id,
            display_name=display_name,
            first_name=first_name,
            last_name=last_name,
            weight=weight,
            height=height,
            age=age,
            team=team,
            jersey=jersey,
            position=position,
            draft=draft,
            status=status,
            alternate_ids=alternate_ids,
            injuries=injuries,
        )

        athlete.additional_properties = d
        return athlete

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
