import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.athlete_overview_experience import AthleteOverviewExperience
    from ..models.athlete_overview_headshot import AthleteOverviewHeadshot
    from ..models.athlete_status import AthleteStatus
    from ..models.birth_place import BirthPlace
    from ..models.college import College
    from ..models.draft_info import DraftInfo


T = TypeVar("T", bound="AthleteOverview")


@_attrs_define
class AthleteOverview:
    """
    Attributes:
        id (str):  Example: 3139477.
        full_name (str):  Example: Patrick Mahomes.
        uid (Union[Unset, str]):  Example: s:20~l:28~a:3139477.
        guid (Union[Unset, str]):  Example: b8464d14e3f517b3b34f7881c4334353.
        first_name (Union[Unset, str]):  Example: Patrick.
        last_name (Union[Unset, str]):  Example: Mahomes.
        display_name (Union[Unset, str]):  Example: Patrick Mahomes.
        short_name (Union[Unset, str]):  Example: P. Mahomes.
        weight (Union[Unset, int]):  Example: 225.
        display_weight (Union[Unset, str]):  Example: 225 lbs.
        height (Union[Unset, int]):  Example: 75.
        display_height (Union[Unset, str]):  Example: 6' 3".
        age (Union[Unset, int]):  Example: 28.
        date_of_birth (Union[Unset, datetime.datetime]):  Example: 1995-09-17T00:00:00Z.
        birth_place (Union[Unset, BirthPlace]):
        jersey (Union[Unset, str]):  Example: 15.
        headshot (Union[Unset, AthleteOverviewHeadshot]):
        experience (Union[Unset, AthleteOverviewExperience]):
        draft (Union[Unset, DraftInfo]):
        college (Union[Unset, College]):
        status (Union[Unset, AthleteStatus]):
    """

    id: str
    full_name: str
    uid: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    weight: Union[Unset, int] = UNSET
    display_weight: Union[Unset, str] = UNSET
    height: Union[Unset, int] = UNSET
    display_height: Union[Unset, str] = UNSET
    age: Union[Unset, int] = UNSET
    date_of_birth: Union[Unset, datetime.datetime] = UNSET
    birth_place: Union[Unset, "BirthPlace"] = UNSET
    jersey: Union[Unset, str] = UNSET
    headshot: Union[Unset, "AthleteOverviewHeadshot"] = UNSET
    experience: Union[Unset, "AthleteOverviewExperience"] = UNSET
    draft: Union[Unset, "DraftInfo"] = UNSET
    college: Union[Unset, "College"] = UNSET
    status: Union[Unset, "AthleteStatus"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        full_name = self.full_name

        uid = self.uid

        guid = self.guid

        first_name = self.first_name

        last_name = self.last_name

        display_name = self.display_name

        short_name = self.short_name

        weight = self.weight

        display_weight = self.display_weight

        height = self.height

        display_height = self.display_height

        age = self.age

        date_of_birth: Union[Unset, str] = UNSET
        if not isinstance(self.date_of_birth, Unset):
            date_of_birth = self.date_of_birth.isoformat()

        birth_place: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.birth_place, Unset):
            birth_place = self.birth_place.to_dict()

        jersey = self.jersey

        headshot: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headshot, Unset):
            headshot = self.headshot.to_dict()

        experience: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.experience, Unset):
            experience = self.experience.to_dict()

        draft: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.draft, Unset):
            draft = self.draft.to_dict()

        college: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.college, Unset):
            college = self.college.to_dict()

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "fullName": full_name,
            }
        )
        if uid is not UNSET:
            field_dict["uid"] = uid
        if guid is not UNSET:
            field_dict["guid"] = guid
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if weight is not UNSET:
            field_dict["weight"] = weight
        if display_weight is not UNSET:
            field_dict["displayWeight"] = display_weight
        if height is not UNSET:
            field_dict["height"] = height
        if display_height is not UNSET:
            field_dict["displayHeight"] = display_height
        if age is not UNSET:
            field_dict["age"] = age
        if date_of_birth is not UNSET:
            field_dict["dateOfBirth"] = date_of_birth
        if birth_place is not UNSET:
            field_dict["birthPlace"] = birth_place
        if jersey is not UNSET:
            field_dict["jersey"] = jersey
        if headshot is not UNSET:
            field_dict["headshot"] = headshot
        if experience is not UNSET:
            field_dict["experience"] = experience
        if draft is not UNSET:
            field_dict["draft"] = draft
        if college is not UNSET:
            field_dict["college"] = college
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.athlete_overview_experience import AthleteOverviewExperience
        from ..models.athlete_overview_headshot import AthleteOverviewHeadshot
        from ..models.athlete_status import AthleteStatus
        from ..models.birth_place import BirthPlace
        from ..models.college import College
        from ..models.draft_info import DraftInfo

        d = src_dict.copy()
        id = d.pop("id")

        full_name = d.pop("fullName")

        uid = d.pop("uid", UNSET)

        guid = d.pop("guid", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        display_name = d.pop("displayName", UNSET)

        short_name = d.pop("shortName", UNSET)

        weight = d.pop("weight", UNSET)

        display_weight = d.pop("displayWeight", UNSET)

        height = d.pop("height", UNSET)

        display_height = d.pop("displayHeight", UNSET)

        age = d.pop("age", UNSET)

        _date_of_birth = d.pop("dateOfBirth", UNSET)
        date_of_birth: Union[Unset, datetime.datetime]
        if isinstance(_date_of_birth, Unset):
            date_of_birth = UNSET
        else:
            date_of_birth = isoparse(_date_of_birth)

        _birth_place = d.pop("birthPlace", UNSET)
        birth_place: Union[Unset, BirthPlace]
        if isinstance(_birth_place, Unset):
            birth_place = UNSET
        else:
            birth_place = BirthPlace.from_dict(_birth_place)

        jersey = d.pop("jersey", UNSET)

        _headshot = d.pop("headshot", UNSET)
        headshot: Union[Unset, AthleteOverviewHeadshot]
        if isinstance(_headshot, Unset):
            headshot = UNSET
        else:
            headshot = AthleteOverviewHeadshot.from_dict(_headshot)

        _experience = d.pop("experience", UNSET)
        experience: Union[Unset, AthleteOverviewExperience]
        if isinstance(_experience, Unset):
            experience = UNSET
        else:
            experience = AthleteOverviewExperience.from_dict(_experience)

        _draft = d.pop("draft", UNSET)
        draft: Union[Unset, DraftInfo]
        if isinstance(_draft, Unset):
            draft = UNSET
        else:
            draft = DraftInfo.from_dict(_draft)

        _college = d.pop("college", UNSET)
        college: Union[Unset, College]
        if isinstance(_college, Unset):
            college = UNSET
        else:
            college = College.from_dict(_college)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AthleteStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AthleteStatus.from_dict(_status)

        athlete_overview = cls(
            id=id,
            full_name=full_name,
            uid=uid,
            guid=guid,
            first_name=first_name,
            last_name=last_name,
            display_name=display_name,
            short_name=short_name,
            weight=weight,
            display_weight=display_weight,
            height=height,
            display_height=display_height,
            age=age,
            date_of_birth=date_of_birth,
            birth_place=birth_place,
            jersey=jersey,
            headshot=headshot,
            experience=experience,
            draft=draft,
            college=college,
            status=status,
        )

        athlete_overview.additional_properties = d
        return athlete_overview

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
