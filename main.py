def calculate_illumination(distance):
    return 3 ** (-(distance / 100) ** 2)


def find_index_of_darkest_street_light(road_length: int, not_working_street_lights: list[int]) -> int:
    lowest_illumination = float('inf')
    darkest_light_index = -1

    for i in range(road_length // 20 + 1):
        if i not in not_working_street_lights:
            distance = i * 20
            illumination = 3 ** (-(distance / 100) ** 2)

            if illumination < lowest_illumination and illumination >= 0.01:
                lowest_illumination = illumination
                darkest_light_index = i

    return darkest_light_index


road_length = 200
not_working_street_lights = [4, 5, 6]
print(find_index_of_darkest_street_light(road_length, not_working_street_lights))