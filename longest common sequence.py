def get_longest_sequence(user_a, user_b):
    worktab = [[0] * (len(user_b) + 1) for _ in range(len(user_a) + 1)]
    #0 is the longest common subsequence length, #1 is the index of the last item found so far in user_a
    longest_info = (0, 0)
    for i, ca in enumerate(user_a, 1):
        for j, cb in enumerate(user_b, 1):
            if ca == cb:
                worktab[i][j] = worktab[i - 1][j - 1] + 1
                if worktab[i][j] > longest_info[0]:
                    longest_info = (worktab[i][j], i)
    if longest_info[0] > 0:
        start = longest_info[1] - longest_info[0]
        end = longest_info[1]
        return user_a[start:end]
    return []

# START TEST CASES
#
# You can add test cases below. Each test case should be a dict of the format:
#
# {
#     "name": "my custom test",
#     "user_a": ...,
#     "user_b": ...,
#     "expected_output": ...
# }


tests = [
    {
        "name": "sample input #1",
        "user_a": ["/nine.html", "/four.html", "/six.html", "/seven.html", "/one.html"],
        "user_b": ["/nine.html", "/two.html", "/three.html", "/four.html", "/six.html", "/seven.html"],
        "expected_output": ["/four.html", "/six.html", "/seven.html"]
    },
    {
        "name": "sample input #2",
        "user_a": ["/one.html", "/two.html", "/three.html", "/four.html", "/six.html"],
        "user_b": ["/nine.html", "/two.html", "/three.html", "/four.html", "/six.html", "/seven.html"],
        "expected_output": ["/two.html", "/three.html", "/four.html", "/six.html"]
    },
    {
        "name": "sample input #3",
        "user_a": ["/nine.html", "/four.html", "/six.html", "/seven.html", "/one.html"],
        "user_b": ["/three.html", "/eight.html"],
        "expected_output": []
    },
    {
        "name": "sample input #4",
        "user_a": ["/one.html", "/two.html", "/three.html", "/four.html", "/six.html"],
        "user_b": ["/three.html", "/eight.html"],
        "expected_output": ["/three.html"]
    }
];

# END TEST CASES
# DO NOT MODIFY BELOW THIS LINE

def main():
    def equal_outputs(a, b):
        return a == b

    passed = 0

    for test in tests:
        try:
            print("==> Testing {}...".format(test['name']))
            actual_output = get_longest_sequence(test['user_a'], test['user_b'])
            if equal_outputs(actual_output, test['expected_output']):
                print("PASS")
                passed += 1
            else:
                print("FAIL")
                print("Expected output: {}".format(test['expected_output']))
                print("Actual output: {}".format(actual_output))
        except Exception as e:
            print("FAIL")
            print(e)

    print("==> Passed {} of {} tests".format(passed, len(tests)))

if __name__ == '__main__':
    main()