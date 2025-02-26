import pytest
from colav_protobuf import ObstaclesUpdate

# from colav_protobuf.examples import ObstaclesUpdate as ObstaclesUpdateExample


def create_sample_obstacles_update():
    obstacles_update = ObstaclesUpdate(
        mission_tag="test_mission", timestamp="2025-02-24T12:00:00Z"
    )

    dynamic_obstacle = obstacles_update.dynamic_obstacles.add()
    dynamic_obstacle.tag = "obstacle_1"
    dynamic_obstacle.type = ObstaclesUpdate.DynamicObstacleType.VESSEL

    dynamic_obstacle.state.pose.position.x = 10.0
    dynamic_obstacle.state.pose.position.y = 20.0
    dynamic_obstacle.state.pose.position.z = 0.0

    dynamic_obstacle.state.pose.orientation.x = 0.0
    dynamic_obstacle.state.pose.orientation.y = 0.0
    dynamic_obstacle.state.pose.orientation.z = 0.0
    dynamic_obstacle.state.pose.orientation.w = 1.0

    dynamic_obstacle.state.velocity = 5.0
    dynamic_obstacle.state.yaw_rate = 0.1

    dynamic_obstacle.geometry.loa = 10.0
    dynamic_obstacle.geometry.beam = 2.0
    dynamic_obstacle.geometry.safety_radius = 2.0

    polyshape_point = dynamic_obstacle.geometry.polyshape_points.add()
    polyshape_point.position.x = 10.0
    polyshape_point.position.y = 20.0
    polyshape_point.position.z = 0.0

    static_obstacle = obstacles_update.static_obstacles.add()
    static_obstacle.tag = "obstacle_2"
    static_obstacle.type = ObstaclesUpdate.StaticObstacleType.LAND_MASS

    static_obstacle.pose.position.x = 30.0
    static_obstacle.pose.position.y = 40.0
    static_obstacle.pose.position.z = 0.0

    static_obstacle.pose.orientation.x = 0.0
    static_obstacle.pose.orientation.y = 0.0
    static_obstacle.pose.orientation.z = 0.0
    static_obstacle.pose.orientation.w = 1.0

    static_obstacle.geometry.inflation_radius = 5.0

    return obstacles_update


@pytest.fixture
def obstacles_update():
    return create_sample_obstacles_update()


def test_obstacles_update_init():
    obstacles_update = ObstaclesUpdate()
    assert obstacles_update is not None


# def test_obstacles_update_fields(obstacles_update):
#     assert obstacles_update.mission_tag == "test_mission"
#     assert obstacles_update.timestamp == "2025-02-24T12:00:00Z"
#     assert obstacles_update.timestep == "100"

#     assert len(obstacles_update.dynamic_obstacles) == 1
#     assert len(obstacles_update.static_obstacles) == 1

#     dynamic_obstacle = obstacles_update.dynamic_obstacles[0]
#     assert dynamic_obstacle.id.tag == "obstacle_1"
#     assert dynamic_obstacle.id.type == ObstaclesUpdate.ObstacleType.VESSEL
#     assert dynamic_obstacle.state.velocity == 5.0
#     assert dynamic_obstacle.state.yaw_rate == 0.1

#     static_obstacle = obstacles_update.static_obstacles[0]
#     assert static_obstacle.id.tag == "obstacle_2"
#     assert static_obstacle.id.type == ObstaclesUpdate.ObstacleType.LAND_MASS
#     assert static_obstacle.geometry.acceptance_radius == 5.0


# Need to finish this
# def test_serialization_deserialization():
#     obstacle_update = ObstaclesUpdateExample()
#     serialized_data = obstacle_update.SerializeToString()
#     deserialized_obstacles_update = ObstaclesUpdate()
#     deserialized_obstacles_update.ParseFromString(serialized_data)

#     # assert deserialized_obstacles_update.mission_tag == obstacles_update.mission_tag
#     # assert deserialized_obstacles_update.timestamp == obstacles_update.timestamp
#     # assert deserialized_obstacles_update.timestep == obstacles_update.timestep
#     # assert len(deserialized_obstacles_update.dynamic_obstacles) == len(
#     #     obstacles_update.dynamic_obstacles
#     # )
#     # assert len(deserialized_obstacles_update.static_obstacles) == len(
#     #     obstacles_update.static_obstacles
#     # )
