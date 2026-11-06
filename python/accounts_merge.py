# 721. Accounts Merge (Medium)
# Given a list of accounts, each a list [name, email1, email2, ...], merge accounts that share
# at least one email (two accounts sharing an email belong to the same person). Return the
# merged accounts, each with the name first, followed by that person's sorted, deduplicated
# emails.
# Approach: union-find over email strings; union every pair of emails within the same account,
# then group all emails by their root parent, sort each group, and attach the owner's name
# (looked up via an email-to-name map). Time O(N log N) for sorting (N = total emails), space
# O(N).

from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        email_to_name = {}

        def find(x: str) -> str:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x: str, y: str) -> None:
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                parent[root_x] = root_y

        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
            for email in emails[1:]:
                union(emails[0], email)

        groups = defaultdict(list)
        for email in parent:
            groups[find(email)].append(email)

        result = []
        for root, emails in groups.items():
            result.append([email_to_name[root]] + sorted(emails))
        return result


if __name__ == "__main__":
    accounts = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    result = Solution().accountsMerge(accounts)
    merged_sets = {frozenset(acc[1:]) for acc in result}
    expected_sets = {
        frozenset(["johnsmith@mail.com", "john_newyork@mail.com", "john00@mail.com"]),
        frozenset(["mary@mail.com"]),
        frozenset(["johnnybravo@mail.com"]),
    }
    assert merged_sets == expected_sets
    for acc in result:
        assert acc[1:] == sorted(acc[1:])
    print("All tests passed.")
