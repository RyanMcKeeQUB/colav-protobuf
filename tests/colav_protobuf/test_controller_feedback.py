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

    return feedback


def test_controller_feedback_init():
    feedback = ControllerFeedback()
    assert feedback is not None


def test_controller_feedback_fields(controller_feedback):
    assert controller_feedback.mission_tag == "test_feedback"

    assert controller_feedback.ctrl_mode == ControllerFeedback.CTRLMode.Value("CRUISE")
    assert controller_feedback.ctrl_status == ControllerFeedback.CTRLStatus.Value(
        "ACTIVE"
    )
    assert controller_feedback.ctrl_cmd.velocity == pytest.approx(15.0, abs=1e-3)
    assert controller_feedback.ctrl_cmd.yaw_rate == pytest.approx(0.2, abs=1e-3)

    assert controller_feedback.timestamp == "1708353000"


def test_serialization_deserialization(controller_feedback):
    # Serialize the controller_feedback to a string
    serialized_feedback = controller_feedback.SerializeToString()

    # Deserialize the string back to a ControllerFeedback object
    deserialized_feedback = ControllerFeedback()
    deserialized_feedback.ParseFromString(serialized_feedback)

    # Verify that the deserialized object matches the original
    assert deserialized_feedback.mission_tag == controller_feedback.mission_tag
    assert deserialized_feedback.agent_tag == controller_feedback.agent_tag
    assert deserialized_feedback.ctrl_mode == controller_feedback.ctrl_mode
    assert deserialized_feedback.ctrl_status == controller_feedback.ctrl_status
    assert deserialized_feedback.ctrl_cmd.velocity == pytest.approx(
        controller_feedback.ctrl_cmd.velocity, abs=1e-3
    )
    assert deserialized_feedback.ctrl_cmd.yaw_rate == pytest.approx(
        controller_feedback.ctrl_cmd.yaw_rate, abs=1e-3
    )
    assert deserialized_feedback.timestamp == controller_feedback.timestamp
