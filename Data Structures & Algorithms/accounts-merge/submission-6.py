class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        #email -> account index
        emailToAcc = {}

        # Step 1: Union accounts sharing an email
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAcc:
                    uf.union(i, emailToAcc[email])
                else:
                    emailToAcc[email] = i
        
        #Step 2: Group emails by root account
        emailGroup = defaultdict(list)

        for email, idx in emailToAcc.items():
            leader = uf.find(idx)
            emailGroup[leader].append(email)

        # Step 3: Build result
        res = []

        for idx, emails in emailGroup.items():
            name = accounts[idx][0]
            res.append([name] + sorted(emails))
        return res
