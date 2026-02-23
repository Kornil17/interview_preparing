# Реализуйте функцию merge_sorted_lists(), которая принимает три аргумента в следующем порядке:
# nums1 – отсортированный по неубыванию список целых чисел
# nums2 – отсортированный по неубыванию список целых чисел
# nums3 – отсортированный по неубыванию список целых чисел
# Функция должна объединять списки nums1, nums2 и nums3 в один общий отсортированный по неубыванию список и возвращать полученный результат в виде нового списка.


# def merge_sorted_lists(
#     nums1: list[int],
#     nums2: list[int],
#     nums3: list[int],
# ) -> list[int]:
#     result = []
#     i = j = k = 0
#     while i < len(nums1) and j < len(nums2) and k < len(nums3):
#         if nums1[i] <= nums2[j] and nums3[k] >= nums1[i]:
#             result.append(nums1[i])
#             i += 1
#         elif nums2[j] <= nums1[i] and nums3[k] >= nums2[j]:
#             result.append(nums2[j])
#             j += 1
#         elif nums3[k] <= nums2[j] and nums3[k] <= nums1[i]:
#             result.append(nums3[k])
#             k += 1
#
#     result.extend(nums1[i:])
#     result.extend(nums3[k:])
#     result.extend(nums2[j:])
#     return result

def merge_sorted_lists(nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
    result = []
    i = j = k = 0

    # Пока есть элементы во всех трёх списках, выбираем наименьший
    while i < len(nums1) and j < len(nums2) and k < len(nums3):
        if nums1[i] <= nums2[j] and nums1[i] <= nums3[k]:
            result.append(nums1[i])
            i += 1
        elif nums2[j] <= nums1[i] and nums2[j] <= nums3[k]:
            result.append(nums2[j])
            j += 1
        else:  # nums3[k] — минимальный
            result.append(nums3[k])
            k += 1

    # Обрабатываем оставшиеся элементы: теперь нужно слить оставшиеся два списка
    # (или один, если два уже исчерпаны)

    # Слияние оставшихся nums1 и nums2
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1

    # Слияние оставшихся nums1 и nums3
    while i < len(nums1) and k < len(nums3):
        if nums1[i] <= nums3[k]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums3[k])
            k += 1

    # Слияние оставшихся nums2 и nums3
    while j < len(nums2) and k < len(nums3):
        if nums2[j] <= nums3[k]:
            result.append(nums2[j])
            j += 1
        else:
            result.append(nums3[k])
            k += 1

    # Добавляем хвосты (если какой-то список ещё не пуст)
    result.extend(nums1[i:])
    result.extend(nums2[j:])
    result.extend(nums3[k:])

    return result


print(merge_sorted_lists([1, 4, 6], [2, 4, 7], [2, 3, 5, 6]))
