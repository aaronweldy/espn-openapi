import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coach_details_response_birth_place import CoachDetailsResponseBirthPlace
    from ..models.coach_details_response_records_item import CoachDetailsResponseRecordsItem
    from ..models.reference import Reference


T = TypeVar("T", bound="CoachDetailsResponse")


@_attrs_define
class CoachDetailsResponse:
    """
    Attributes:
        id (str):  Example: 17751.
        first_name (str):  Example: Jonathan.
        last_name (str):  Example: Gannon.
        ref (Union[Unset, str]):  Example:
            http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2024/coaches/17751?lang=en&region=us.
        uid (Union[Unset, str]):  Example: s:20~l:28~co:17751.
        date_of_birth (Union[Unset, datetime.datetime]):  Example: 1983-04-04T08:00Z.
        birth_place (Union[Unset, CoachDetailsResponseBirthPlace]):
        college (Union[Unset, Reference]):
        person (Union[Unset, Reference]):
        team (Union[Unset, Reference]):
        experience (Union[Unset, int]):  Example: 1.
        records (Union[Unset, List['CoachDetailsResponseRecordsItem']]):
    """

    id: str
    first_name: str
    last_name: str
    ref: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    date_of_birth: Union[Unset, datetime.datetime] = UNSET
    birth_place: Union[Unset, "CoachDetailsResponseBirthPlace"] = UNSET
    college: Union[Unset, "Reference"] = UNSET
    person: Union[Unset, "Reference"] = UNSET
    team: Union[Unset, "Reference"] = UNSET
    experience: Union[Unset, int] = UNSET
    records: Union[Unset, List["CoachDetailsResponseRecordsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        first_name = self.first_name

        last_name = self.last_name

        ref = self.ref

        uid = self.uid

        date_of_birth: Union[Unset, str] = UNSET
        if not isinstance(self.date_of_birth, Unset):
            date_of_birth = self.date_of_birth.isoformat()

        birth_place: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.birth_place, Unset):
            birth_place = self.birth_place.to_dict()

        college: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.college, Unset):
            college = self.college.to_dict()

        person: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.person, Unset):
            person = self.person.to_dict()

        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        experience = self.experience

        records: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.records, Unset):
            records = []
            for records_item_data in self.records:
                records_item = records_item_data.to_dict()
                records.append(records_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "firstName": first_name,
                "lastName": last_name,
            }
        )
        if ref is not UNSET:
            field_dict["$ref"] = ref
        if uid is not UNSET:
            field_dict["uid"] = uid
        if date_of_birth is not UNSET:
            field_dict["dateOfBirth"] = date_of_birth
        if birth_place is not UNSET:
            field_dict["birthPlace"] = birth_place
        if college is not UNSET:
            field_dict["college"] = college
        if person is not UNSET:
            field_dict["person"] = person
        if team is not UNSET:
            field_dict["team"] = team
        if experience is not UNSET:
            field_dict["experience"] = experience
        if records is not UNSET:
            field_dict["records"] = records

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.coach_details_response_birth_place import CoachDetailsResponseBirthPlace
        from ..models.coach_details_response_records_item import CoachDetailsResponseRecordsItem
        from ..models.reference import Reference

        d = src_dict.copy()
        id = d.pop("id")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        ref = d.pop("$ref", UNSET)

        uid = d.pop("uid", UNSET)

        _date_of_birth = d.pop("dateOfBirth", UNSET)
        date_of_birth: Union[Unset, datetime.datetime]
        if isinstance(_date_of_birth, Unset):
            date_of_birth = UNSET
        else:
            date_of_birth = isoparse(_date_of_birth)

        _birth_place = d.pop("birthPlace", UNSET)
        birth_place: Union[Unset, CoachDetailsResponseBirthPlace]
        if isinstance(_birth_place, Unset):
            birth_place = UNSET
        else:
            birth_place = CoachDetailsResponseBirthPlace.from_dict(_birth_place)

        _college = d.pop("college", UNSET)
        college: Union[Unset, Reference]
        if isinstance(_college, Unset):
            college = UNSET
        else:
            college = Reference.from_dict(_college)

        _person = d.pop("person", UNSET)
        person: Union[Unset, Reference]
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = Reference.from_dict(_person)

        _team = d.pop("team", UNSET)
        team: Union[Unset, Reference]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = Reference.from_dict(_team)

        experience = d.pop("experience", UNSET)

        records = []
        _records = d.pop("records", UNSET)
        for records_item_data in _records or []:
            records_item = CoachDetailsResponseRecordsItem.from_dict(records_item_data)

            records.append(records_item)

        coach_details_response = cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            ref=ref,
            uid=uid,
            date_of_birth=date_of_birth,
            birth_place=birth_place,
            college=college,
            person=person,
            team=team,
            experience=experience,
            records=records,
        )

        coach_details_response.additional_properties = d
        return coach_details_response

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
