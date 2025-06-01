from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fantasy_competitor_home_away import FantasyCompetitorHomeAway
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fantasy_competitor_records_item import FantasyCompetitorRecordsItem
    from ..models.fantasy_leader import FantasyLeader
    from ..models.fantasy_probable import FantasyProbable


T = TypeVar("T", bound="FantasyCompetitor")


@_attrs_define
class FantasyCompetitor:
    """
    Attributes:
        id (Union[Unset, str]):
        uid (Union[Unset, str]):
        home_away (Union[Unset, FantasyCompetitorHomeAway]):
        winner (Union[Unset, bool]):
        name (Union[Unset, str]):
        abbreviation (Union[Unset, str]):
        display_name (Union[Unset, str]):
        logo (Union[Unset, str]):
        score (Union[Unset, str]):
        records (Union[Unset, List['FantasyCompetitorRecordsItem']]):
        leaders (Union[Unset, List['FantasyLeader']]):
        probables (Union[Unset, List['FantasyProbable']]):
    """

    id: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    home_away: Union[Unset, FantasyCompetitorHomeAway] = UNSET
    winner: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    logo: Union[Unset, str] = UNSET
    score: Union[Unset, str] = UNSET
    records: Union[Unset, List["FantasyCompetitorRecordsItem"]] = UNSET
    leaders: Union[Unset, List["FantasyLeader"]] = UNSET
    probables: Union[Unset, List["FantasyProbable"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        uid = self.uid

        home_away: Union[Unset, str] = UNSET
        if not isinstance(self.home_away, Unset):
            home_away = self.home_away.value

        winner = self.winner

        name = self.name

        abbreviation = self.abbreviation

        display_name = self.display_name

        logo = self.logo

        score = self.score

        records: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.records, Unset):
            records = []
            for records_item_data in self.records:
                records_item = records_item_data.to_dict()
                records.append(records_item)

        leaders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.leaders, Unset):
            leaders = []
            for leaders_item_data in self.leaders:
                leaders_item = leaders_item_data.to_dict()
                leaders.append(leaders_item)

        probables: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.probables, Unset):
            probables = []
            for probables_item_data in self.probables:
                probables_item = probables_item_data.to_dict()
                probables.append(probables_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uid is not UNSET:
            field_dict["uid"] = uid
        if home_away is not UNSET:
            field_dict["homeAway"] = home_away
        if winner is not UNSET:
            field_dict["winner"] = winner
        if name is not UNSET:
            field_dict["name"] = name
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if logo is not UNSET:
            field_dict["logo"] = logo
        if score is not UNSET:
            field_dict["score"] = score
        if records is not UNSET:
            field_dict["records"] = records
        if leaders is not UNSET:
            field_dict["leaders"] = leaders
        if probables is not UNSET:
            field_dict["probables"] = probables

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fantasy_competitor_records_item import FantasyCompetitorRecordsItem
        from ..models.fantasy_leader import FantasyLeader
        from ..models.fantasy_probable import FantasyProbable

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        uid = d.pop("uid", UNSET)

        _home_away = d.pop("homeAway", UNSET)
        home_away: Union[Unset, FantasyCompetitorHomeAway]
        if isinstance(_home_away, Unset):
            home_away = UNSET
        else:
            home_away = FantasyCompetitorHomeAway(_home_away)

        winner = d.pop("winner", UNSET)

        name = d.pop("name", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        display_name = d.pop("displayName", UNSET)

        logo = d.pop("logo", UNSET)

        score = d.pop("score", UNSET)

        records = []
        _records = d.pop("records", UNSET)
        for records_item_data in _records or []:
            records_item = FantasyCompetitorRecordsItem.from_dict(records_item_data)

            records.append(records_item)

        leaders = []
        _leaders = d.pop("leaders", UNSET)
        for leaders_item_data in _leaders or []:
            leaders_item = FantasyLeader.from_dict(leaders_item_data)

            leaders.append(leaders_item)

        probables = []
        _probables = d.pop("probables", UNSET)
        for probables_item_data in _probables or []:
            probables_item = FantasyProbable.from_dict(probables_item_data)

            probables.append(probables_item)

        fantasy_competitor = cls(
            id=id,
            uid=uid,
            home_away=home_away,
            winner=winner,
            name=name,
            abbreviation=abbreviation,
            display_name=display_name,
            logo=logo,
            score=score,
            records=records,
            leaders=leaders,
            probables=probables,
        )

        fantasy_competitor.additional_properties = d
        return fantasy_competitor

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
