def two_sum_brute_force(nums, target):
    """
    الحل بطريقة البحث القسري (مناسب للمبتدئين)
    التعقيد الزمني: O(n^2)
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]  # إرجاع الفهارس
    return []  # لا ينبغي الوصول إلى هنا حسب نص المسألة


def two_sum_optimized(nums, target):
    """
    الحل المحسن باستخدام قاموس (للمحترفين)
    التعقيد الزمني: O(n)
    """
    num_map = {}  # قاموس لتخزين الأرقام وفهارسها
    for i, num in enumerate(nums):
        complement = target - num  # حساب الرقم المكمل
        if complement in num_map:
            return [num_map[complement], i]  # إرجاع الفهارس
        num_map[num] = i  # تخزين الرقم وفهرسه
    return []  # لا ينبغي الوصول إلى هنا حسب نص المسألة


# أمثلة للاختبار
def main():
    nums = [2, 7, 11, 15]
    target = 18
    
    print("الحل بالبحث القسري:", two_sum_brute_force(nums, target))
    print("الحل المحسن:", two_sum_optimized(nums, target))


if __name__ == "__main__":
    main()
