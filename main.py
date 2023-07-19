import math


# Calculating illumination using formula
def calculate_illumination(distance):
    return 3 ** (-(distance / 100) ** 2)


def find_index_of_darkest_street_light(road_length: int, not_working_street_lights: list[int]) -> tuple:
    """

    :param road_length: user should provide in what range (road length) should be find darkest light indexes (max 2 mil)
    :param not_working_street_lights: list of indexes that has not working light bulbs
    :return: tuple of darkest_light_index and bulbs that has to be replaced because illumination intencity is
    less than 1.
    """
    if not road_length > 2000000:
        lowest_illumination = math.inf
        darkest_light_index = -1
        bulb_replacements = 0

        # Checking each road lamp cause every 20 meters is a lamp.
        for i in range(road_length // 20 + 1):
            if i in not_working_street_lights:
                illumination = 0

                # Calculate the illumination from neighbor working lights
                for light in range(i - 1, i + 2):
                    if light < 0 or light >= road_length // 20 + 1 or light in not_working_street_lights:
                        continue
                    distance = i * 20 - light * 20
                    illumination += calculate_illumination(distance)

                # Checking lowest illumination
                if illumination < lowest_illumination:
                    lowest_illumination = illumination
                    darkest_light_index = i
                    if illumination < 1:
                        bulb_replacements += 1
        return darkest_light_index, bulb_replacements
    else:
        print(f'The provided road length is greater that 2 million you provided {road_length}')


if __name__ == "__main__":
    road_length = 200
    non_working_street_lights = [4, 5, 6]

    darkest_index, bulb_replacements = find_index_of_darkest_street_light(road_length, non_working_street_lights)

    assert darkest_index == 5
    assert bulb_replacements == 2

    print("ALL TESTS PASSED")
