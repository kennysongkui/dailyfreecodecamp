'''
Idea Rankings
Given a 2D array where each inner array contains (in this order) an idea name, an optimistic estimate, a realistic estimate, and a pessimistic estimate (in days), return an array of the idea names sorted by expected time to completion, shortest first.

Calculate the expected time to completion for each idea using the following formula:

expected = ((optimistic + 4 * realistic + pessimistic) / 6) * length of idea name

'''


def analyze_ideas(ideas):
    # ideas_value = {}
    # for idea in ideas:
    #     print(idea)
    #
    #     value = (idea[1] + 4 * idea[2] + idea[3] / 6) / len(idea[0])
    #     ideas_value[idea[0]] = value
    #
    # print(ideas_value)
    # # result = dict(sorted(ideas_value.items(), key=lambda kv: kv[1]))
    # result = sorted(ideas_value, key=value)
    # print(result)
    #
    # ideas = list(result.keys())

    def expected_time(idea):
        name, optimistic, realistic, pessimistic = idea
        return ((optimistic + 4 * realistic + pessimistic) / 6) * len(name)

    result = [idea[0] for idea in sorted(ideas, key=expected_time)]
    print(result)

    ideas = result
    return ideas


# t = analyze_ideas([["Add logging", 2, 5, 15], ["SEO optimization", 4, 8, 20], ["Fix bug", 1, 3, 5]])
# print(t)

t1 = analyze_ideas([["Dark mode", 1, 3, 8], ["Real-time collaboration feature", 6, 12, 20], ["Add tooltip", 1, 2, 4]])
print(t1)
