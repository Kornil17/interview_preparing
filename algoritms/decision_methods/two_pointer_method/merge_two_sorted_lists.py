def merge_sorted_lists(nums1, nums2):
    result = []
    i = j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1

    while i < len(nums1):
        result.append(nums1[i])
        i += 1

    while j < len(nums2):
        result.append(nums2[j])
        j += 1

    return result

print(merge_sorted_lists(
    [1, 4, 6,],
    [2, 3, 5, 7, 8, 9]
))