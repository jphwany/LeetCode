class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
# 파이썬에서 클래스의 메소드를 정의할 때 
# self, 객체 인스턴스를 명시해야한다 (객체 자기 자신을 참조하는 매개변수)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
# for i range(): 
# for 반복문은 리스트, 배열, 문자열 또는 range() 안에 있는 모든 값들에 대한 코드 블록을 반복
# for 반복문 작성을 간소화하기 위해 range() 사용 가능
# for i in range(start, stop)
# 여기서 만약 매개변수가 하나라면 start = 0 으로 간주

# for i in range(len(nums)):
# i가 0부터(start 0) nums 배열 길이만큼 순회
# nums를 전부 순회하면서 두 인덱스 요소의 합이 타겟과 같은 것을 찾아야 한다

# for j in range(i+1, len(nums)):
# j가 i+1부터 nums 배열의 길이만큼 순회
# 위에서 nums 전체를 i가 한 번 순회할 때, 인덱스 i+1번째부터 i+2 ... nums 배열 길이까지 순회

# 예를 들어 nums = [2, 7, 11, 15] 이고 target = 18 라고 하면
# 2, 7 탐색 -> 2+7은 18인가? 아님. 다음 순회로
# 2, 11 탐색 -> 2+11은 18인가? 아님. 다음 순회로
# 2, 15 탐색 -> 2+15는 18인가? 아님. 다음 순회로
# 7, 11 탐색 -> 7+11은 18인가? 맞음. 리턴

# 근데 이렇게 하면 Time Limit Exceeded, 다른 방법을 찾아야 한다
        
        cache = {}

        for i in range(len(nums)):
            # a+b = target을 찾는다
            a = nums[i]
            b = target - a
            
            if b in cache:
                return [i, cache[b]]

            else: cache[a] = i
            
            
            