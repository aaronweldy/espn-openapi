"""Contains all the data models used in inputs/outputs"""

from .address import Address
from .alternate_ids import AlternateIDS
from .athlete_contract import AthleteContract
from .athlete_contract_base_year_compensation import AthleteContractBaseYearCompensation
from .athlete_contract_poison_pill_provision import AthleteContractPoisonPillProvision
from .athlete_contract_trade_kicker import AthleteContractTradeKicker
from .athlete_contracts_response import AthleteContractsResponse
from .athlete_details_response import AthleteDetailsResponse
from .athlete_details_response_alternate_ids import AthleteDetailsResponseAlternateIds
from .athlete_details_response_experience import AthleteDetailsResponseExperience
from .athlete_reference import AthleteReference
from .athlete_statistics_by_category_response import AthleteStatisticsByCategoryResponse
from .athlete_statistics_by_category_response_splits import AthleteStatisticsByCategoryResponseSplits
from .athlete_statistics_log_response import AthleteStatisticsLogResponse
from .athlete_statistics_response import AthleteStatisticsResponse
from .athlete_statistics_response_splits import AthleteStatisticsResponseSplits
from .athlete_status import AthleteStatus
from .athletes_list_response import AthletesListResponse
from .ats_record_type import AtsRecordType
from .attendance_category import AttendanceCategory
from .attendance_stat import AttendanceStat
from .betting_odds import BettingOdds
from .betting_odds_team_odds import BettingOddsTeamOdds
from .betting_provider import BettingProvider
from .broadcast_logo import BroadcastLogo
from .broadcast_market import BroadcastMarket
from .broadcast_media import BroadcastMedia
from .broadcast_type import BroadcastType
from .calendar_list_response import CalendarListResponse
from .coach_details_response import CoachDetailsResponse
from .coach_details_response_birth_place import CoachDetailsResponseBirthPlace
from .coach_details_response_records_item import CoachDetailsResponseRecordsItem
from .competition_athlete_statistics_response import CompetitionAthleteStatisticsResponse
from .competition_athlete_statistics_response_splits import CompetitionAthleteStatisticsResponseSplits
from .competition_broadcast import CompetitionBroadcast
from .competition_broadcast_item import CompetitionBroadcastItem
from .competition_broadcasts_response import CompetitionBroadcastsResponse
from .competition_competitor import CompetitionCompetitor
from .competition_competitor_leaders_type_1 import CompetitionCompetitorLeadersType1
from .competition_competitor_linescores_type_1 import CompetitionCompetitorLinescoresType1
from .competition_competitor_record_type_1 import CompetitionCompetitorRecordType1
from .competition_competitor_roster_type_1 import CompetitionCompetitorRosterType1
from .competition_competitor_score_type_1 import CompetitionCompetitorScoreType1
from .competition_competitor_statistics_type_1 import CompetitionCompetitorStatisticsType1
from .competition_competitor_team_type_1 import CompetitionCompetitorTeamType1
from .competition_detail import CompetitionDetail
from .competition_detail_notes_item import CompetitionDetailNotesItem
from .competition_format import CompetitionFormat
from .competition_leader import CompetitionLeader
from .competition_leaders_category import CompetitionLeadersCategory
from .competition_leaders_response import CompetitionLeadersResponse
from .competition_official_item import CompetitionOfficialItem
from .competition_officials_response import CompetitionOfficialsResponse
from .competition_overtime import CompetitionOvertime
from .competition_situation_response import CompetitionSituationResponse
from .competition_source import CompetitionSource
from .competition_status import CompetitionStatus
from .competition_status_type import CompetitionStatusType
from .competition_type import CompetitionType
from .core_nfl_season_team_response import CoreNflSeasonTeamResponse
from .draft_athlete_analysis import DraftAthleteAnalysis
from .draft_athlete_attribute import DraftAthleteAttribute
from .draft_athlete_headshot import DraftAthleteHeadshot
from .draft_athlete_response import DraftAthleteResponse
from .drive import Drive
from .drive_clock import DriveClock
from .drive_field_position import DriveFieldPosition
from .drive_period import DrivePeriod
from .drive_source import DriveSource
from .drive_time_elapsed import DriveTimeElapsed
from .drives_list_response import DrivesListResponse
from .error_response import ErrorResponse
from .error_response_error import ErrorResponseError
from .event_detail import EventDetail
from .event_detail_competitions_item_type_1 import EventDetailCompetitionsItemType1
from .event_detail_league_type_1 import EventDetailLeagueType1
from .event_detail_season_type_1 import EventDetailSeasonType1
from .event_detail_season_type_type_1 import EventDetailSeasonTypeType1
from .event_detail_venues_item_type_1 import EventDetailVenuesItemType1
from .event_detail_week_type_1 import EventDetailWeekType1
from .event_reference import EventReference
from .future_book import FutureBook
from .future_item import FutureItem
from .future_item_type import FutureItemType
from .future_provider import FutureProvider
from .futures_response import FuturesResponse
from .get_athlete_statistics_seasontype import GetAthleteStatisticsSeasontype
from .get_league_season_corrections_season_type import GetLeagueSeasonCorrectionsSeasonType
from .get_league_season_group_details_season_type import GetLeagueSeasonGroupDetailsSeasonType
from .get_league_season_groups_season_type import GetLeagueSeasonGroupsSeasonType
from .get_league_season_weeks_season_type import GetLeagueSeasonWeeksSeasonType
from .get_nfl_conference_standings_seasontype import GetNFLConferenceStandingsSeasontype
from .group_details_response import GroupDetailsResponse
from .head_to_heads import HeadToHeads
from .head_to_heads_list_response import HeadToHeadsListResponse
from .last_play_reference import LastPlayReference
from .leader_category import LeaderCategory
from .league_enum import LeagueEnum
from .league_info_response import LeagueInfoResponse
from .league_season import LeagueSeason
from .link import Link
from .logo import Logo
from .mlb_athlete_details_response import MlbAthleteDetailsResponse
from .mlb_athlete_details_response_alternate_ids import MlbAthleteDetailsResponseAlternateIds
from .mlb_athlete_details_response_awards import MlbAthleteDetailsResponseAwards
from .mlb_athlete_details_response_bats import MlbAthleteDetailsResponseBats
from .mlb_athlete_details_response_birth_place import MlbAthleteDetailsResponseBirthPlace
from .mlb_athlete_details_response_college import MlbAthleteDetailsResponseCollege
from .mlb_athlete_details_response_contracts import MlbAthleteDetailsResponseContracts
from .mlb_athlete_details_response_debut import MlbAthleteDetailsResponseDebut
from .mlb_athlete_details_response_draft import MlbAthleteDetailsResponseDraft
from .mlb_athlete_details_response_experience import MlbAthleteDetailsResponseExperience
from .mlb_athlete_details_response_headshot import MlbAthleteDetailsResponseHeadshot
from .mlb_athlete_details_response_links_item import MlbAthleteDetailsResponseLinksItem
from .mlb_athlete_details_response_position import MlbAthleteDetailsResponsePosition
from .mlb_athlete_details_response_statistics import MlbAthleteDetailsResponseStatistics
from .mlb_athlete_details_response_statisticslog import MlbAthleteDetailsResponseStatisticslog
from .mlb_athlete_details_response_status import MlbAthleteDetailsResponseStatus
from .mlb_athlete_details_response_team import MlbAthleteDetailsResponseTeam
from .mlb_athlete_details_response_throws import MlbAthleteDetailsResponseThrows
from .news_category import NewsCategory
from .news_headline import NewsHeadline
from .news_image import NewsImage
from .news_link_amp import NewsLinkAmp
from .news_link_api import NewsLinkApi
from .news_link_item import NewsLinkItem
from .news_link_mobile import NewsLinkMobile
from .news_link_web import NewsLinkWeb
from .news_links import NewsLinks
from .news_metric import NewsMetric
from .news_related import NewsRelated
from .news_related_links import NewsRelatedLinks
from .news_response import NewsResponse
from .news_video import NewsVideo
from .news_video_ad import NewsVideoAd
from .news_video_links import NewsVideoLinks
from .nfl_athlete_eventlog_response import NflAthleteEventlogResponse
from .nfl_athlete_eventlog_response_events import NflAthleteEventlogResponseEvents
from .nfl_athlete_eventlog_response_events_items_item import NflAthleteEventlogResponseEventsItemsItem
from .nfl_athlete_eventlog_response_teams import NflAthleteEventlogResponseTeams
from .nfl_athlete_eventlog_response_teams_additional_property import NflAthleteEventlogResponseTeamsAdditionalProperty
from .nfl_athlete_injury import NflAthleteInjury
from .nfl_athlete_injury_athlete_type_1 import NflAthleteInjuryAthleteType1
from .nfl_athlete_injury_source import NflAthleteInjurySource
from .nfl_athlete_injury_team_type_1 import NflAthleteInjuryTeamType1
from .nfl_athlete_injury_type import NflAthleteInjuryType
from .nfl_conference_standings_item import NflConferenceStandingsItem
from .nfl_conference_standings_response import NflConferenceStandingsResponse
from .nfl_draft_athlete_analysis import NflDraftAthleteAnalysis
from .nfl_draft_athlete_attribute import NflDraftAthleteAttribute
from .nfl_draft_athlete_response import NflDraftAthleteResponse
from .nfl_draft_pick import NflDraftPick
from .nfl_draft_pick_status import NflDraftPickStatus
from .nfl_draft_position import NflDraftPosition
from .nfl_draft_response import NflDraftResponse
from .nfl_draft_round import NflDraftRound
from .nfl_draft_round_detail import NflDraftRoundDetail
from .nfl_draft_round_status import NflDraftRoundStatus
from .nfl_draft_rounds_response import NflDraftRoundsResponse
from .nfl_draft_team import NflDraftTeam
from .nfl_draft_team_need import NflDraftTeamNeed
from .nfl_leader import NflLeader
from .nfl_leaders_category import NflLeadersCategory
from .nfl_leaders_response import NflLeadersResponse
from .nfl_team_depthchart_athlete import NflTeamDepthchartAthlete
from .nfl_team_depthchart_group import NflTeamDepthchartGroup
from .nfl_team_depthchart_group_positions import NflTeamDepthchartGroupPositions
from .nfl_team_depthchart_position import NflTeamDepthchartPosition
from .nfl_team_depthchart_response import NflTeamDepthchartResponse
from .odds_detail import OddsDetail
from .odds_item import OddsItem
from .odds_item_current import OddsItemCurrent
from .odds_provider import OddsProvider
from .odds_record_stat import OddsRecordStat
from .odds_response import OddsResponse
from .odds_team_current import OddsTeamCurrent
from .odds_value import OddsValue
from .odds_value_with_outcome import OddsValueWithOutcome
from .odds_value_with_outcome_outcome import OddsValueWithOutcomeOutcome
from .odds_value_with_outcome_outcome_type import OddsValueWithOutcomeOutcomeType
from .official_position import OfficialPosition
from .paginated_reference_list_response import PaginatedReferenceListResponse
from .play import Play
from .play_clock import PlayClock
from .play_field_position import PlayFieldPosition
from .play_participant import PlayParticipant
from .play_participant_athlete_type_1 import PlayParticipantAthleteType1
from .play_participant_position_type_1 import PlayParticipantPositionType1
from .play_participant_statistics_type_1 import PlayParticipantStatisticsType1
from .play_period import PlayPeriod
from .play_probability_type_1 import PlayProbabilityType1
from .play_stat import PlayStat
from .play_type import PlayType
from .plays_list_response import PlaysListResponse
from .position import Position
from .positions_list_response import PositionsListResponse
from .predictor_response import PredictorResponse
from .predictor_statistic import PredictorStatistic
from .predictor_team import PredictorTeam
from .probabilities_list_response import ProbabilitiesListResponse
from .probability_item import ProbabilityItem
from .probability_source import ProbabilitySource
from .provider_details import ProviderDetails
from .providers_list_response import ProvidersListResponse
from .reference import Reference
from .season import Season
from .season_type import SeasonType
from .season_types_list import SeasonTypesList
from .season_week import SeasonWeek
from .split_stats import SplitStats
from .sport_enum import SportEnum
from .spread_record import SpreadRecord
from .stat_category import StatCategory
from .stat_correction import StatCorrection
from .stat_corrections_response import StatCorrectionsResponse
from .stat_item import StatItem
from .statistic import Statistic
from .statistic_category import StatisticCategory
from .statistics_log_entry import StatisticsLogEntry
from .statistics_reference import StatisticsReference
from .statistics_type_entry import StatisticsTypeEntry
from .team import Team
from .team_ats_record import TeamAtsRecord
from .team_ats_records_response import TeamAtsRecordsResponse
from .team_attendance_response import TeamAttendanceResponse
from .team_leader import TeamLeader
from .team_leaders_response import TeamLeadersResponse
from .team_odds import TeamOdds
from .team_odds_record import TeamOddsRecord
from .team_odds_records_response import TeamOddsRecordsResponse
from .team_reference import TeamReference
from .transactions_list_response import TransactionsListResponse
from .transactions_list_response_items_item import TransactionsListResponseItemsItem
from .venue import Venue

__all__ = (
    "Address",
    "AlternateIDS",
    "AthleteContract",
    "AthleteContractBaseYearCompensation",
    "AthleteContractPoisonPillProvision",
    "AthleteContractsResponse",
    "AthleteContractTradeKicker",
    "AthleteDetailsResponse",
    "AthleteDetailsResponseAlternateIds",
    "AthleteDetailsResponseExperience",
    "AthleteReference",
    "AthletesListResponse",
    "AthleteStatisticsByCategoryResponse",
    "AthleteStatisticsByCategoryResponseSplits",
    "AthleteStatisticsLogResponse",
    "AthleteStatisticsResponse",
    "AthleteStatisticsResponseSplits",
    "AthleteStatus",
    "AtsRecordType",
    "AttendanceCategory",
    "AttendanceStat",
    "BettingOdds",
    "BettingOddsTeamOdds",
    "BettingProvider",
    "BroadcastLogo",
    "BroadcastMarket",
    "BroadcastMedia",
    "BroadcastType",
    "CalendarListResponse",
    "CoachDetailsResponse",
    "CoachDetailsResponseBirthPlace",
    "CoachDetailsResponseRecordsItem",
    "CompetitionAthleteStatisticsResponse",
    "CompetitionAthleteStatisticsResponseSplits",
    "CompetitionBroadcast",
    "CompetitionBroadcastItem",
    "CompetitionBroadcastsResponse",
    "CompetitionCompetitor",
    "CompetitionCompetitorLeadersType1",
    "CompetitionCompetitorLinescoresType1",
    "CompetitionCompetitorRecordType1",
    "CompetitionCompetitorRosterType1",
    "CompetitionCompetitorScoreType1",
    "CompetitionCompetitorStatisticsType1",
    "CompetitionCompetitorTeamType1",
    "CompetitionDetail",
    "CompetitionDetailNotesItem",
    "CompetitionFormat",
    "CompetitionLeader",
    "CompetitionLeadersCategory",
    "CompetitionLeadersResponse",
    "CompetitionOfficialItem",
    "CompetitionOfficialsResponse",
    "CompetitionOvertime",
    "CompetitionSituationResponse",
    "CompetitionSource",
    "CompetitionStatus",
    "CompetitionStatusType",
    "CompetitionType",
    "CoreNflSeasonTeamResponse",
    "DraftAthleteAnalysis",
    "DraftAthleteAttribute",
    "DraftAthleteHeadshot",
    "DraftAthleteResponse",
    "Drive",
    "DriveClock",
    "DriveFieldPosition",
    "DrivePeriod",
    "DrivesListResponse",
    "DriveSource",
    "DriveTimeElapsed",
    "ErrorResponse",
    "ErrorResponseError",
    "EventDetail",
    "EventDetailCompetitionsItemType1",
    "EventDetailLeagueType1",
    "EventDetailSeasonType1",
    "EventDetailSeasonTypeType1",
    "EventDetailVenuesItemType1",
    "EventDetailWeekType1",
    "EventReference",
    "FutureBook",
    "FutureItem",
    "FutureItemType",
    "FutureProvider",
    "FuturesResponse",
    "GetAthleteStatisticsSeasontype",
    "GetLeagueSeasonCorrectionsSeasonType",
    "GetLeagueSeasonGroupDetailsSeasonType",
    "GetLeagueSeasonGroupsSeasonType",
    "GetLeagueSeasonWeeksSeasonType",
    "GetNFLConferenceStandingsSeasontype",
    "GroupDetailsResponse",
    "HeadToHeads",
    "HeadToHeadsListResponse",
    "LastPlayReference",
    "LeaderCategory",
    "LeagueEnum",
    "LeagueInfoResponse",
    "LeagueSeason",
    "Link",
    "Logo",
    "MlbAthleteDetailsResponse",
    "MlbAthleteDetailsResponseAlternateIds",
    "MlbAthleteDetailsResponseAwards",
    "MlbAthleteDetailsResponseBats",
    "MlbAthleteDetailsResponseBirthPlace",
    "MlbAthleteDetailsResponseCollege",
    "MlbAthleteDetailsResponseContracts",
    "MlbAthleteDetailsResponseDebut",
    "MlbAthleteDetailsResponseDraft",
    "MlbAthleteDetailsResponseExperience",
    "MlbAthleteDetailsResponseHeadshot",
    "MlbAthleteDetailsResponseLinksItem",
    "MlbAthleteDetailsResponsePosition",
    "MlbAthleteDetailsResponseStatistics",
    "MlbAthleteDetailsResponseStatisticslog",
    "MlbAthleteDetailsResponseStatus",
    "MlbAthleteDetailsResponseTeam",
    "MlbAthleteDetailsResponseThrows",
    "NewsCategory",
    "NewsHeadline",
    "NewsImage",
    "NewsLinkAmp",
    "NewsLinkApi",
    "NewsLinkItem",
    "NewsLinkMobile",
    "NewsLinks",
    "NewsLinkWeb",
    "NewsMetric",
    "NewsRelated",
    "NewsRelatedLinks",
    "NewsResponse",
    "NewsVideo",
    "NewsVideoAd",
    "NewsVideoLinks",
    "NflAthleteEventlogResponse",
    "NflAthleteEventlogResponseEvents",
    "NflAthleteEventlogResponseEventsItemsItem",
    "NflAthleteEventlogResponseTeams",
    "NflAthleteEventlogResponseTeamsAdditionalProperty",
    "NflAthleteInjury",
    "NflAthleteInjuryAthleteType1",
    "NflAthleteInjurySource",
    "NflAthleteInjuryTeamType1",
    "NflAthleteInjuryType",
    "NflConferenceStandingsItem",
    "NflConferenceStandingsResponse",
    "NflDraftAthleteAnalysis",
    "NflDraftAthleteAttribute",
    "NflDraftAthleteResponse",
    "NflDraftPick",
    "NflDraftPickStatus",
    "NflDraftPosition",
    "NflDraftResponse",
    "NflDraftRound",
    "NflDraftRoundDetail",
    "NflDraftRoundsResponse",
    "NflDraftRoundStatus",
    "NflDraftTeam",
    "NflDraftTeamNeed",
    "NflLeader",
    "NflLeadersCategory",
    "NflLeadersResponse",
    "NflTeamDepthchartAthlete",
    "NflTeamDepthchartGroup",
    "NflTeamDepthchartGroupPositions",
    "NflTeamDepthchartPosition",
    "NflTeamDepthchartResponse",
    "OddsDetail",
    "OddsItem",
    "OddsItemCurrent",
    "OddsProvider",
    "OddsRecordStat",
    "OddsResponse",
    "OddsTeamCurrent",
    "OddsValue",
    "OddsValueWithOutcome",
    "OddsValueWithOutcomeOutcome",
    "OddsValueWithOutcomeOutcomeType",
    "OfficialPosition",
    "PaginatedReferenceListResponse",
    "Play",
    "PlayClock",
    "PlayFieldPosition",
    "PlayParticipant",
    "PlayParticipantAthleteType1",
    "PlayParticipantPositionType1",
    "PlayParticipantStatisticsType1",
    "PlayPeriod",
    "PlayProbabilityType1",
    "PlaysListResponse",
    "PlayStat",
    "PlayType",
    "Position",
    "PositionsListResponse",
    "PredictorResponse",
    "PredictorStatistic",
    "PredictorTeam",
    "ProbabilitiesListResponse",
    "ProbabilityItem",
    "ProbabilitySource",
    "ProviderDetails",
    "ProvidersListResponse",
    "Reference",
    "Season",
    "SeasonType",
    "SeasonTypesList",
    "SeasonWeek",
    "SplitStats",
    "SportEnum",
    "SpreadRecord",
    "StatCategory",
    "StatCorrection",
    "StatCorrectionsResponse",
    "Statistic",
    "StatisticCategory",
    "StatisticsLogEntry",
    "StatisticsReference",
    "StatisticsTypeEntry",
    "StatItem",
    "Team",
    "TeamAtsRecord",
    "TeamAtsRecordsResponse",
    "TeamAttendanceResponse",
    "TeamLeader",
    "TeamLeadersResponse",
    "TeamOdds",
    "TeamOddsRecord",
    "TeamOddsRecordsResponse",
    "TeamReference",
    "TransactionsListResponse",
    "TransactionsListResponseItemsItem",
    "Venue",
)
