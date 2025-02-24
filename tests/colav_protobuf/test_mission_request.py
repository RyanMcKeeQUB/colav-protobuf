import pytest
from colav_protobuf import MissionRequest
import math


def _round_up(value, decimals=3):
    factor = 10**decimals
    return math.ceil(value * factor) / factor


@pytest.fixture
def mission_request():
    request = MissionRequest()
    # Static Vessel Information
    request.tag = "test_mission"
    request.mission_start_timestamp = "1708353000"
    request.vessel.tag = "EF12_WORKBOAT"
    request.vessel.type = MissionRequest.Vessel.VesselType.HYDROFOIL
    request.vessel.vessel_constraints.max_acceleration = 2.0
    request.vessel.vessel_constraints.max_deceleration = -1.0
    request.vessel.vessel_constraints.max_velocity = 30.0
    request.vessel.vessel_constraints.min_velocity = 15.0
    request.vessel.vessel_constraints.max_yaw_rate = 0.2
    request.vessel.vessel_geometry.safety_threshold = 5

    # Earth-Centered, Earth-Fixed) Cartesian Coordinates North Belfast Lough in meters
    request.mission_init_position.x = float(3675900.74)
    request.mission_init_position.y = float(-372412.13)
    request.mission_init_position.z = float(5181577.5)

    # Earth-Centered, Earth-Fixed) Cartesian Coordinates South France near Marseille in meters WON'T USE THIS METRIC IN LOCAL MOTION PLANNER! GOOD FOR GLOBAL PLANNING
    request.mission_goal_position.x = float(4680627.4)
    request.mission_goal_position.z = float(503374.5)
    request.mission_goal_position.y = float(4299351.3)
    # Need to change vessel and obstacle geometry to just consider length and breadth

    # Acceptance radius in meters of the goal waypoint for autonomous navigation.
    request.mission_goal_acceptance_radius = float(5.0)

    return request


def test_mission_request_init():
    request = MissionRequest()
    assert request is not None


def test_mission_request_fields(mission_request):
    assert mission_request.tag == "test_mission"
    assert mission_request.mission_start_timestamp == "1708353000"
    assert mission_request.vessel.tag == "EF12_WORKBOAT"
    assert mission_request.vessel.type == MissionRequest.Vessel.VesselType.HYDROFOIL
    assert _round_up(mission_request.vessel.vessel_constraints.max_acceleration) == 2.0
    assert _round_up(mission_request.vessel.vessel_constraints.max_deceleration) == -1.0
    assert _round_up(mission_request.vessel.vessel_constraints.max_velocity) == 30.0
    assert _round_up(mission_request.vessel.vessel_constraints.min_velocity) == 15.0
    assert _round_up(mission_request.vessel.vessel_constraints.max_yaw_rate) == 0.201
    assert mission_request.vessel.vessel_geometry.safety_threshold == 5
    assert _round_up(mission_request.mission_init_position.x) == pytest.approx(
        3675900.75, abs=1e-3
    )
    assert _round_up(mission_request.mission_init_position.y) == pytest.approx(
        -372412.125, abs=1e-3
    )
    assert _round_up(mission_request.mission_init_position.z) == pytest.approx(
        5181577.50, abs=1e-3
    )
    assert _round_up(mission_request.mission_goal_position.x) == pytest.approx(
        4680627.5, abs=1e-3
    )
    assert _round_up(mission_request.mission_goal_position.z) == pytest.approx(
        503374.5, abs=1e-3
    )
    assert _round_up(mission_request.mission_goal_position.y) == pytest.approx(
        4299351.5, abs=1e-3
    )
    assert _round_up(mission_request.mission_goal_acceptance_radius) == pytest.approx(
        5.0, abs=1e-3
    )


def test_serialization_deserialization(mission_request):
    serialized_data = mission_request.SerializeToString()
    deserialized_update = MissionRequest()
    deserialized_update.ParseFromString(serialized_data)

    assert deserialized_update.tag == "test_mission"
    assert mission_request.mission_start_timestamp == "1708353000"
    assert mission_request.vessel.tag == "EF12_WORKBOAT"
