from colav_protobuf.examples import mission_request
from colav_protobuf.examples import mission_response
from colav_protobuf.examples import agent_update
from colav_protobuf.examples import obstacles_update
from colav_protobuf.examples import controller_feedback


def main():
    print(mission_request)
    print(mission_response)

    print(agent_update)
    print(obstacles_update)

    print(controller_feedback)


if __name__ == "__main__":
    main()
