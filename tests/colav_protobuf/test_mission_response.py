import pytest
from colav_protobuf import MissionResponse
import math


@pytest.fixture
def mission_response():
    res = MissionResponse()
    res.mission_tag = "COLAV_MISSION_NORTH_BELFAST_TO_SOUTH_FRANCE"
    res.mission_start_timestamp = "1708353005"
    res.mission_response = MissionResponse.MissionResponseEnum.Value("MISSION_STARTING")
    res.mission_response_details = "Mission has started. Now Navigating to South"
    return res


def test_mission_response_init():
    res = MissionResponse()
    assert res is not None


def test_mission_response_fields(mission_response):
    assert mission_response.mission_tag == "COLAV_MISSION_NORTH_BELFAST_TO_SOUTH_FRANCE"
    assert mission_response.mission_start_timestamp == "1708353005"
    assert (
        mission_response.mission_response
        == MissionResponse.MissionResponseEnum.Value("MISSION_STARTING")
    )
    assert (
        mission_response.mission_response_details
        == "Mission has started. Now Navigating to South"
    )


def test_serialization_deserialization(mission_response):
    serialized = mission_response.SerializeToString()
    deserialized = MissionResponse()
    deserialized.ParseFromString(serialized)
    assert mission_response == deserialized
    assert mission_response.mission_tag == deserialized.mission_tag
    assert (
        mission_response.mission_start_timestamp == deserialized.mission_start_timestamp
    )
    assert mission_response.mission_response == deserialized.mission_response
    assert (
        mission_response.mission_response_details
        == deserialized.mission_response_details
    )
