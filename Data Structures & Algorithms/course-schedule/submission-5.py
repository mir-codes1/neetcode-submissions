class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # create hashmap of prerequisites
        prereq = defaultdict(set)
        nxt = defaultdict(set)
        for x, y in prerequisites:
            prereq[x].add(y)
            nxt[y].add(x)

        # find starting points (all courses with no prereqs)
        q = collections.deque(c for c in range(numCourses) if not prereq[c])

        visited = set()
        while q:
            node = q.popleft()
            if node not in visited:
                visited.add(node)
                for i in nxt[node]:
                    prereq[i].discard(node)
                    if not prereq[i]:
                        q.append(i)

        return len(visited) == numCourses