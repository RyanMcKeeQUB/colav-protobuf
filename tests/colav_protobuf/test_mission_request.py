import pytest
from colav_protobuf import MissionRequest


@pytest.fixture
def mission_request():
    request = MissionRequest()
    # Static Vessel Information
    request.tag = "test_mission"
    request.timestamp = "1708353000"
    request.vessel.tag = "EF12_WORKBOAT"
    request.vessel.type = MissionRequest.Vessel.VesselType.HYDROFOIL
    request.vessel.constraints.max_acceleration = 2.0
    request.vessel.constraints.max_deceleration = -1.0
    request.vessel.constraints.max_velocity = 30.0
    request.vessel.constraints.min_velocity = 15.0
    request.vessel.constraints.max_yaw_rate = 0.2
    request.vessel.geometry.loa = 2.0
    request.vessel.geometry.beam = 0.5
    request.vessel.geometry.safety_radius = 5.0

    # Earth-Centered, Earth-Fixed) Cartesian Coordinates North Belfast Lough in meters
    request.init_position.x = float(3675900.74)
    request.init_position.y = float(-372412.13)
    request.init_position.z = float(5181577.5)

    # Earth-Centered, Earth-Fixed) Cartesian Coordinates South France near Marseille in meters WON'T USE THIS METRIC IN LOCAL MOTION PLANNER! GOOD FOR GLOBAL PLANNING
    request.goal_waypoint.position.x = float(4680627.4)
    request.goal_waypoint.position.y = float(4299351.3)
    request.goal_waypoint.position.z = float(503374.5)

    # Need to change vessel and obstacle geometry to just consider length and breadth

    # Acceptance radius in meters of the goal waypoint for autonomous navigation.
    request.goal_waypoint.safety_radius = float(5.0)

    return request


def test_mission_request_init():
    request = MissionRequest()
    assert request is not None


def test_mission_request_fields(mission_request):
    assert mission_request.tag == "test_mission"
    assert mission_request.timestamp == "1708353000"
    assert mission_request.vessel.tag == "EF12_WORKBOAT"
    assert mission_request.vessel.type == MissionRequest.Vessel.VesselType.HYDROFOIL
    assert (mission_request.vessel.constraints.max_acceleration) == 2.0
    assert (mission_request.vessel.constraints.max_deceleration) == -1.0
    assert (mission_request.vessel.constraints.max_velocity) == 30.0
    assert (mission_request.vessel.constraints.min_velocity) == pytest.approx(
        15.0, abs=1e-3
    )
    assert (mission_request.vessel.constraints.max_yaw_rate) == pytest.approx(
        0.2, abs(1e-3)
    )
    assert mission_request.vessel.geometry.safety_radius == 5
    assert (mission_request.init_position.x) == pytest.approx(3675900.75, abs=1e-3)
    assert (mission_request.init_position.y) == pytest.approx(-372412.125, abs=1e-3)
    assert (mission_request.init_position.z) == pytest.approx(5181577.5, abs=1e-3)
    assert (mission_request.goal_waypoint.position.x) == pytest.approx(
        4680627.5, abs=1e-3
    )
    assert (mission_request.goal_waypoint.position.y) == pytest.approx(
        4299351.5, abs=1e-3
    )
    assert (mission_request.goal_waypoint.position.z) == pytest.approx(
        503374.5, abs=1e-3
    )
    assert mission_request.goal_waypoint.safety_radius == 5.0


def test_serialization_deserialization(mission_request):
    serialized_data = mission_request.SerializeToString()
    deserialized_update = MissionRequest()
    deserialized_update.ParseFromString(serialized_data)

    assert deserialized_update.tag == "test_mission"
    assert mission_request.timestamp == "1708353000"
    assert mission_request.vessel.tag == "EF12_WORKBOAT"
