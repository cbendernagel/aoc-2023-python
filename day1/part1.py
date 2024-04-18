def main():
    input = open('./day1/input.txt', 'r')
    sum = 0
    for line in input:
        nums = [int(i) for i in line if i.isdigit()]
        temp = nums[0] * 10 + nums[len(nums) - 1]
        sum += temp
        
    print(sum)
    
if __name__ == '__main__':
    main()