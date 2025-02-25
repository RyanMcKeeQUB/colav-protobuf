import pytest
from colav_protobuf import MissionResponse
import math


@pytest.fixture
def mission_response():
    res = MissionResponse()
    res.tag = "COLAV_MISSION_NORTH_BELFAST_TO_SOUTH_FRANCE"
    res.timestamp = "1708353005"
    res.response.type = MissionResponse.MissionResponseMsg.ResponseTypeEnum.Value(
        "MISSION_STARTING"
    )
    res.response.details = "Mission has started. Now Navigating to South"
    return res


def test_mission_response_init():
    res = MissionResponse()
    assert res is not None


def test_mission_response_fields(mission_response):
    assert mission_response.tag == "COLAV_MISSION_NORTH_BELFAST_TO_SOUTH_FRANCE"
    assert mission_response.timestamp == "1708353005"
    assert (
        mission_response.response.type
        == MissionResponse.MissionResponseMsg.ResponseTypeEnum.Value("MISSION_STARTING")
    )
    assert (
        mission_response.response.details
        == "Mission has started. Now Navigating to South"
    )


def test_serialization_deserialization(mission_response):
    serialized = mission_response.SerializeToString()
    deserialized = MissionResponse()
    deserialized.ParseFromString(serialized)
    assert mission_response == deserialized
    assert mission_response.tag == deserialized.tag
    assert mission_response.timestamp == deserialized.timestamp
    assert mission_response.response.type == deserialized.response.type
    assert mission_response.response.details == deserialized.response.details
