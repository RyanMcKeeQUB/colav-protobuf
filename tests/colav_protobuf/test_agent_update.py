import pytest
from colav_protobuf import AgentUpdate
import math


def _round_up(value, decimals=3):
    factor = 10**decimals
    return math.ceil(value * factor) / factor


@pytest.fixture
def agent_update():
    update = AgentUpdate(
        mission_tag="test_mission",
        agent_tag="agent_001",
        timestamp="1234567890",
    )
    update.state.pose.position.x = 1.000
    update.state.pose.position.y = 2.000
    update.state.pose.position.z = 3.000
    update.state.pose.orientation.x = 0.000
    update.state.pose.orientation.y = 0.000
    update.state.pose.orientation.z = 0.000
    update.state.pose.orientation.w = 1.000
    update.state.velocity = 5.000
    update.state.yaw_rate = 0.100
    update.state.acceleration = 0.200
    return update


def test_agent_update_init():
    agent_update = AgentUpdate()
    assert agent_update is not None


def test_agent_update_fields(agent_update):
    assert agent_update.mission_tag == "test_mission"
    assert agent_update.agent_tag == "agent_001"
    assert agent_update.timestamp == "1234567890"
    assert _round_up(agent_update.state.pose.position.x) == 1.000
    assert _round_up(agent_update.state.pose.position.y) == 2.000
    assert _round_up(agent_update.state.pose.position.z) == 3.000
    assert _round_up(agent_update.state.pose.orientation.x) == 0.000
    assert _round_up(agent_update.state.pose.orientation.y) == 0.000
    assert _round_up(agent_update.state.pose.orientation.z) == 0.000
    assert _round_up(agent_update.state.pose.orientation.w) == 1.000
    assert _round_up(agent_update.state.velocity) == 5.000
    assert _round_up(agent_update.state.yaw_rate) == 0.101
    assert _round_up(agent_update.state.acceleration) == 0.201


def test_serialization_deserialization(agent_update):
    serialized_data = agent_update.SerializeToString()
    deserialized_update = AgentUpdate()
    deserialized_update.ParseFromString(serialized_data)

    assert deserialized_update.mission_tag == "test_mission"
    assert deserialized_update.agent_tag == "agent_001"
    assert deserialized_update.timestamp == "1234567890"
    assert deserialized_update.state.pose.position.x == 1.0
    assert deserialized_update.state.pose.position.y == 2.0
    assert deserialized_update.state.pose.position.z == 3.0
    assert deserialized_update.state.pose.orientation.x == 0.0
    assert deserialized_update.state.pose.orientation.y == 0.0
    assert deserialized_update.state.pose.orientation.z == 0.0
    assert deserialized_update.state.pose.orientation.w == 1.0
    assert deserialized_update.state.velocity == 5.0
    assert deserialized_update.state.yaw_rate == 0.10000000149011612
    assert deserialized_update.state.acceleration == 0.20000000298023224
