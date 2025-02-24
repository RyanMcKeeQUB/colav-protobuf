import pytest
from colav_protobuf import ObstaclesUpdate


def test_obstacles_update_init():
    obstacles_update = ObstaclesUpdate()
    assert obstacles_update is not None


def test_obstacles_update_fields(obstacles_update):
    pass


def test_serialization_deserialization(obstacles_update):
    serialized_obstacles_update = obstacles_update.SerializeToString()
    deserialized_obstacles_update = ObstaclesUpdate()
    deserialized_obstacles_update.ParseFromString(serialized_obstacles_update)
    assert deserialized_obstacles_update.tag == obstacles_update.tag
