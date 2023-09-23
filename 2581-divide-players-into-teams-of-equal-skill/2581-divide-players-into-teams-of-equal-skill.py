class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        lower_skill = skill[:int(len(skill)/2)]
        upper_skill = skill[int(len(skill)/2):]

        upper_skill.sort(reverse = True)

        result = 0
        sum_skill = lower_skill[0] + upper_skill[0]
        for i in range(len(lower_skill)):
            if lower_skill[i] + upper_skill[i] != sum_skill:
                return -1
            result += lower_skill[i] * upper_skill[i]

        return result
        