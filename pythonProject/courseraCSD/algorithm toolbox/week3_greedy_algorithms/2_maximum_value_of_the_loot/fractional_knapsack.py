# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    #10,[3,4,5],[100,20,30]
    weight_count=len(weights)
    value_per_pound=((values[index]/weights[index],index) for index in range(weight_count)) # tính trung bình giá mỗi pound, đồng thời lưu số lượng củ nó
    per_pound=sorted(value_per_pound,reverse=True)
    # [(33.333333333333336, 0), (6.0, 2), (5.0, 1)]
    print(per_pound)
    loot=0
    for value, index in per_pound:
        if capacity<weights[index]:
            loot+=capacity*value
            return loot
        else:
            loot+=weights[index]*value
        capacity-=weights[index]
        if capacity==0:
            return loot
# nếu ít, giá cao thì trung bình mỗi pound cao
# print(get_optimal_value(50,[50, 20, 30],[60, 100, 120]))

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
