from src.colav_protobuf import ControllerFeedback
import pytest


@pytest.fixture
def controller_feedback():
    feedback = ControllerFeedback()
    feedback.mission_tag = "test_feedback"
    feedback.agent_tag = "EF12_WORKBOAT"
    feedback.ctrl_mode = ControllerFeedback.CTRLMode.Value("CRUISE")
    feedback.ctrl_status = ControllerFeedback.CTRLStatus.Value("ACTIVE")
    feedback.ctrl_cmd.velocity = float(15.0)
    feedback.ctrl_cmd.yaw_rate = float(0.2)
    feedback.timestamp = "1708353000"
    feedback.timestep = "000000000012331"

    return feedback


def test_controller_feedback_init():
    feedback = ControllerFeedback()
    assert feedback is not None


def test_controller_feedback_fields(controller_feedback):
    assert controller_feedback.tag == "test_feedback"
    assert controller_feedback.timestamp == "1708353000"
    assert controller_feedback.vessel.tag == "EF12_WORKBOAT"
    assert (
        controller_feedback.vessel.type
        == ControllerFeedback.Vessel.VesselType.HYDROFOIL
    )
    assert controller_feedback.vessel.vessel_constraints.max_acceleration == 2.0
    assert controller_feedback.vessel.vessel_constraints.max_deceleration == -1.0
    assert controller_feedback.vessel.vessel_constraints.max_velocity == 30.0
    assert controller_feedback.vessel.vessel_constraints.min_velocity == 15.0
    assert controller_feedback.vessel.vessel_constraints.max_yaw_rate == 0.2
    assert controller_feedback.vessel.vessel_geometry.safety_threshold == 5

    assert controller_feedback.position.x == pytest.approx(3675900.74, abs=1e-3)
    assert controller_feedback.position.y == pytest.approx(-372412.13, abs=1e-3)
    assert controller_feedback.position.z == pytest.approx(5181577.5, abs=1e-3)

    assert controller_feedback.velocity.x == pytest.approx(0.0, abs=1e-3)
    assert controller_feedback.velocity.y == pytest.approx(0.0, abs=1e-3)
    assert controller_feedback.velocity.z == pytest.approx(0.0, abs=1e-3)

    assert controller_feedback.acceleration.x == pytest.approx(0.0, abs=1e-3)
    assert controller_feedback.acceleration.y == pytest.approx(0.0, abs=1e-3)
    assert controller_feedback.acceleration.z == pytest.approx(0.0, abs=1e-3)

    assert controller_feedback.yaw == pytest.approx(0.0, abs=1e-3)
    assert controller_feedback.yaw_rate == pytest.approx(0.0, abs=1e-3)


def test_serialization_deserialization(controller_feedback):
    serialized_feedback = controller_feedback.SerializeToString()
    deserialized_feedback = ControllerFeedback()
    deserialized_feedback.ParseFromString(serialized_feedback)
    assert deserialized_feedback.tag == controller_feedback.tag
    assert deserialized_feedback.timestamp == controller_feedback.timestamp
    assert deserialized_feedback.vessel.tag == controller_feedback.vessel.tag
    assert deserialized_feedback.vessel.type == controller_feedback.vessel.type
    assert (
        deserialized_feedback.vessel.vessel_constraints.max_acceleration
        == controller_feedback.vessel.vessel_constraints.max_acceleration
    )
    assert (
        deserialized_feedback.vessel.vessel_constraints.max_deceleration
        == controller_feedback.vessel.vessel_constraints.max_deceleration
    )
    assert (
        deserialized_feedback.vessel.vessel_constraints.max_velocity
        == controller_feedback.vessel.vessel_constraints.max_velocity
    )
    assert (
        deserialized_feedback.vessel.vessel_constraints.min_velocity
        == controller_feedback.vessel.vessel_constraints.min_velocity
    )
    assert (
        deserialized_feedback.vessel.vessel_constraints.max_yaw_rate
        == controller_feedback.vessel.vessel_constraints.max_yaw_rate
    )
    assert (
        deserialized_feedback.vessel.vessel_geometry.safety_threshold
        == controller_feedback.vessel.vessel_geometry.safety_threshold
    )
    assert deserialized_feedback.position.x == controller_feedback.position.x
    assert deserialized_feedback.position.y == controller_feedback.position.y
    assert deserialized_feedback.position.z == controller_feedback.position.z
    assert deserialized_feedback.velocity.x == controller_feedback.velocity.x
    assert deserialized_feedback.velocity.y == controller_feedback.velocity.y
    assert deserialized_feedback.velocity.z == controller_feedback.velocity.z
    assert deserialized_feedback.acceleration.x == controller_feedback.acceleration.x
    assert deserialized_feedback.acceleration.y == controller_feedback.acceleration.y
    assert deserialized_feedback.acceleration.z == controller_feedback.acceleration.z
    assert deserialized_feedback.yaw == controller_feedback.yaw
    assert deserialized_feedback.yaw_rate == controller_feedback.yaw_rate
